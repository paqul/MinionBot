# link_bot = https://discord.com/api/oauth2/authorize?client_id=1055576642254286938&permissions=3287864568646&scope=bot

import discord
from discord.ext import tasks, commands
import responses
import members
from params import token
import asyncio
import sys
import time
from channels_whitelist import channels_on, channels_on_test
key = token
channels_on = channels_on #Imports Withelist from channels_whitelist.py
channels_on_test = channels_on_test #Imports Withelist on test from channels_whitelist.py
bot_self_mention_string = ""
auto_test_task = None  # Define the auto_test_task variable globally

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
        # if msg.author == client.user or msg.author == "@MinonBot":
        # return
        print(
            f"{msg.author} powiedzial '{msg.content}' ({msg.channel}) || {client.user} "
        )
        if msg.content == bot_self_mention_string + " autotest":
            # Cancel the existing autotest task, if any running to avoid parallelization
            if auto_test_task and not auto_test_task.done():
                auto_test_task.cancel()
            # Create an asyncio task and invoke autotest func
            auto_test_task = asyncio.create_task(auto_test(msg))
        # Cancel the auto_test task if stop msg received
        elif msg.content == bot_self_mention_string + " stop":
            await msg.channel.send("# ***Przerywam Autotest.***")
            if auto_test_task and not auto_test_task.done():
                auto_test_task.cancel()
        else:
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
    if msg.channel.name in channels_on:
        if msg.content.startswith(bot_self_mention_string):
            try:
                resp_name = responses.handle_name_response(
                    user_msg, bot_self_mention_string
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


async def auto_test(msg):
    # Predefined lists of amount of rolls and dice
    rolls = [1, 10, 1000, 99999]  # Example rolls
    dice = [
        "2",
        "3",
        "4",
        "6",
        "8",
        "10",
        "11",
        "12",
        "16",
        "20",
        "24",
        "30",
        "66",
        "100",
        "1000",
        "20a",
        "20d",
        "100kk",
        "100pp",
        "100kp",
        "100pk",
        "100k",
        "100p",
        "20*2",
        "20+2",
        "20-2",
        "10+2+2+5-3*2",
        "20a+100",
        "20d+100",
    ]  # Example dice
    # Iterate through the lists
    for roll in rolls:
        for die in dice:
            await msg.channel.send(f"{roll}d{die}")
            # Delay to avoid rate limiting by Discord
            await asyncio.sleep(2.5)
    # Send a final message indicating the completion of the auto test
    await msg.channel.send("statystyki_dnd")
    await asyncio.sleep(2.5)
    await msg.channel.send("help")
    await asyncio.sleep(2.5)
    await msg.channel.send("# ***Zakończono Autotest.***")


# asyncio.run(debug_console())
