#link_bot = https://discord.com/api/oauth2/authorize?client_id=1055576642254286938&permissions=3287864568646&scope=bot

import discord
from discord.ext import tasks, commands
import responses
import roles
import members
from params import token
import threading
import asyncio
import sys
#import youtube_dl
# import audio

key = token
channels_on = ["sala_spotkań", "dział_techcznicny", "warhammer", "darkheresy",
               "gra", "gra-u-szadka", "dungeonsanddragons", "neuroshima",
               "zew", "rzuty-w-trakcie-sesji", "testy", "DD", "ZEW", "WARHAMMER", "GRA",
               "jednostrzały", "DD 5e", "CYBERPUNKRED", "Sesja publiczna", "SESJA PUBLICZNA"]
channels_on_test = ["sala_spotkań", "dział_techcznicny", "general"]

# Discord music feature of bot Initialization
# key = token
#voice_clients = {}
#yt_dl_opts = {'format': 'bestaudio/best'}
#ytdl = youtube_dl.YoutubeDL(yt_dl_opts)
#ffmpeg_options = {'options': "-vn"}
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
        print(f"{msg.author} powiedzial '{msg.content}' ({msg.channel}) || {client.user} ")
        await send_msg(msg, msg.content, private=False)

    @tasks.loop(seconds=120)
    async def check_role():
        print("CHECK ROLE")
        global members
        guild = client.get_guild(client)
        role = guild.get_role(roles)
        members = [member for member in guild.members if role in member.roles]

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
        response = responses.handle_response(msg, member.name, member.id)
        await member.send(response)
    except Exception as E:
        print(E)


async def send_msg(msg, user_msg, private, client):
    # print(msg.channel.name)
    # print(msg)
    # print(msg.channel)
    if msg.channel.name in channels_on:
        bot_mention = f"<@"+{client.user.id}+">"
        if msg.content.startswith(bot_mention):
            try:
                resp_name = responses.handle_name_response(user_msg)
                await msg.channel.send(resp_name)
            except Exception as E:
                print(E)
        else:
            try:
                resp = responses.handle_response(user_msg, msg.author, msg.author.id)
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
        
#async def autotest():
    #print("TEST")
    #await send_msg("1k10", "1k10".content, private=False)
    # send_msg("1k10", user_msg, private)
    # return "1k10"

#def double_thread(user_msg, author, author_id):
    #th_1 = threading.Thread(responses.handle_response, user_msg, author, author_id)
    #th_2 = threading.Thread(responses.handle_response, user_msg, author, author_id)
    #th_1.start()
    #th_2.start()
    #th_1.join()
    #th_2.join()
    # return th_2
