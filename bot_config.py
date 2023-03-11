#link_bot = https://discord.com/api/oauth2/authorize?client_id=1055576642254286938&permissions=3287864568646&scope=bot

import discord
import responses
import roles
import members
import youtube_dl
import asyncio
# import audio
import sys
from discord.ext import commands

token = "MTA1NTU3NjY0MjI1NDI4NjkzOA.Ga5o8-.4RUZOCsrCVmpNLG9AIJk-1wLxRSZaBv5ger02U"
channels_on = ["sala_spotkań", "dział_techcznicny", "warhammer", "darkheresy", "gra", "dungeonsanddragons", "neuroshima", "zew", "rzuty-w-trakcie-sesji", "DD", "ZEW"]
channels_on_test = ["sala_spotkań", "dział_techcznicny", "general"]

# Discord music feature of bot Initialization
key = token
voice_clients = {}
yt_dl_opts = {'format': 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)
ffmpeg_options = {'options': "-vn"}
# End of music feature initialization

# msg.author - uzytkownik ktory pisze do bota
# msg.content - zawartosc wiadomosci np "Hej to ja"
# msg.channel - na ktorym kanale to sie dzieje


def setup_bot():
    intents = discord.Intents.all() #all/none/default
    client = discord.Client(intents=intents)
    # bot = commands.Bot(command_prefix="!", intents=intents)

    @client.event
    async def on_ready():
        print("Bot working!")

    @client.event
    async def on_message(msg):
        if msg.author == client.user:
            return
        print(f"{msg.author} powiedzial '{msg.content}' ({msg.channel}) || {client.user} ")
        await send_msg(msg, msg.content, private=False)

    @client.event
    async def on_member_join(member):
        print(f"{member.name} dołączył do serwera")
        if str(member.name) in members.member_list:
            await get_role(member)
            await send_private(member, "promotion")
        elif str(member.name) in members.black_list:
            await member.kick()
            await send_private(member, "negative")
        else:
            await get_role(member)
            await send_private(member, "welcome")

    client.run(token)
    # bot.run(token)


async def send_private(member, msg):
    try:
        response = responses.handle_response(msg, member.name)
        await member.send(response)
    except Exception as E:
        print(E)


async def send_msg(msg, user_msg, private):
    # print(msg.channel.name)
    # print(msg)
    # print(msg.channel)
    if msg.channel.name in channels_on:
        if msg.content.startswith("<@1055576642254286938>"):
            try:
                resp_name = responses.handle_name_response(user_msg)
                await msg.channel.send(resp_name)
            except Exception as E:
                print(E)
        else:
            try:
                resp = responses.handle_response(user_msg, msg.author)
                await msg.author.send(resp) if private else await msg.channel.send(resp)
            except Exception as E:
                print(E)


async def get_role(member):
    try:
        role_name = roles.handle_roles(member)
        role = discord.utils.get(member.guild.roles, name=role_name)
        await member.add_roles(role)
    except Exception as E:
        print(E)

# asyncio.run(debug_console())