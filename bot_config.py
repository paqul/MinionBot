# link_bot = https://discord.com/oauth2/authorize?client_id=516283630088093696&permissions=277025613824&integration_type=0&scope=bot

import discord
from discord.ext import tasks, commands
import responses
from params import token
import asyncio
import sys
import time
from pathlib import Path

from admin_commands import handle_admin_mention_command
from autotest import build_summary_message, run_legacy_autotest, run_summary_autotest
from channels_whitelist import channels_on, channels_on_test
from whitelist_storage import ChannelWhitelistStore

key = token
channels_on = channels_on #Imports Withelist from channels_whitelist.py
channels_on_test = channels_on_test #Imports Withelist on test from channels_whitelist.py
bot_self_mention_string = ""
auto_test_task = None  # Define the auto_test_task variable globally

# Hardcoded user IDs allowed to modify channel whitelist through mention commands.
ALLOWED_ADMIN_USER_IDS = {
    608017745346560000,
    179152462232551424,
}

whitelist_store = ChannelWhitelistStore(
    Path(__file__).resolve().parent / "config" / "channel_whitelist.json",
    channels_on,
)


def _extract_mention_body(message_content: str, bot_user_id: int) -> str | None:
    prefixes = (f"<@{bot_user_id}>", f"<@!{bot_user_id}>")
    for prefix in prefixes:
        if message_content.startswith(prefix):
            return message_content[len(prefix):].strip()
    return None


def _is_admin_user(user_id: int) -> bool:
    return user_id in ALLOWED_ADMIN_USER_IDS

# msg.author - uzytkownik ktory pisze do bota
# msg.content - zawartosc wiadomosci np "Hej to ja"
# msg.channel - na ktorym kanale to sie dzieje


def setup_bot():
    intents = discord.Intents.all()  # all/none/default
    client = discord.Client(intents=intents)

    # bot = commands.Bot(command_prefix="!", intents=intents)

    @client.event
    async def on_ready():
        print("Bot working!")
        global bot_self_mention_string
        bot_id = client.user.id
        bot_self_mention_string = f"<@{bot_id}>"

    @client.event
    async def on_message(msg):
        global auto_test_task
        if msg.author == client.user:
            return

        # if msg.author == client.user or msg.author == "@MinonBot":
        # return
        print(
            f"{msg.author} powiedzial '{msg.content}' ({msg.channel}) || {client.user} "
        )
        mention_body = _extract_mention_body(msg.content, client.user.id)

        if mention_body and mention_body.lower().startswith("autotest"):
            if not _is_admin_user(msg.author.id):
                await msg.channel.send("Nie masz uprawnien do uruchamiania autotestu.")
                return

            mode = "summary"
            parts = mention_body.split(maxsplit=1)
            if len(parts) > 1:
                requested_mode = parts[1].strip().lower()
                if requested_mode in {"legacy", "summary"}:
                    mode = requested_mode

            if mode == "legacy":
                if auto_test_task and not auto_test_task.done():
                    auto_test_task.cancel()
                auto_test_task = asyncio.create_task(run_legacy_autotest(msg))
                return

            results, duration = run_summary_autotest(msg.author)
            await msg.channel.send(build_summary_message(results, duration))
            return

        # Cancel the auto_test task if stop msg received
        elif mention_body and mention_body.lower() == "stop":
            if not _is_admin_user(msg.author.id):
                await msg.channel.send("Nie masz uprawnien do zatrzymania autotestu.")
                return

            await msg.channel.send("# ***Przerywam Autotest.***")
            if auto_test_task and not auto_test_task.done():
                auto_test_task.cancel()
        else:
            admin_command_response = handle_admin_mention_command(
                msg,
                client.user.id,
                ALLOWED_ADMIN_USER_IDS,
                whitelist_store,
            )
            if admin_command_response:
                await msg.channel.send(admin_command_response)
                return

            await send_msg(msg, msg.content, bot_self_mention_string, private=False)

    client.run(token)
    # bot.run(token)


async def send_private(member, msg):
    try:
        response = responses.handle_response(msg, member.name, member.id)
        await member.send(response)
    except Exception as E:
        print(E)


async def send_msg(msg, user_msg, bot_self_mention_string, private):
    # print(msg.channel.name)
    # print(msg)
    # print(msg.channel)
    if whitelist_store.is_allowed(msg.channel.id, msg.channel.name):
        if msg.content.startswith(bot_self_mention_string):
            try:
                resp_name = responses.handle_name_response(
                    user_msg, bot_self_mention_string, msg.author
                )
                if resp_name:
                    await msg.channel.send(resp_name)
            except Exception as E:
                print(E)
        else:
            try:
                resp = responses.handle_response(user_msg, msg.author, msg.author.id)
                if resp:
                    (
                        await msg.author.send(resp)
                        if private
                        else await msg.channel.send(resp)
                    )
            except Exception as E:
                print(E)


# asyncio.run(debug_console())
