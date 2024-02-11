#link_bot = https://discord.com/api/oauth2/authorize?client_id=1055576642254286938&permissions=3287864568646&scope=bot

import discord
from discord.ext import tasks, commands
import responses
import roles
import members
from params import token
import asyncio
import sys
import time
#import threading
#import youtube_dl
# import audio

key = token
channels_on = ["sala_spotkań", "dział_techcznicny", "warhammer", "darkheresy",
               "gra", "gra-u-szadka", "dungeonsanddragons", "neuroshima",
               "zew", "rzuty-w-trakcie-sesji", "testy", "DD", "ZEW", "WARHAMMER", "GRA",
               "jednostrzały", "DD 5e", "CYBERPUNKRED", "Sesja publiczna", "SESJA PUBLICZNA", "generau-czat"]
channels_on_test = ["sala_spotkań", "dział_techcznicny", "general"]
bot_self_mention_string = ""
auto_test_task = None  # Define the auto_test_task variable globally

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
        global bot_self_mention_string 
        bot_id = client.user.id
        bot_self_mention_string = f"<@{bot_id}>"

    @client.event
    async def on_message(msg):
        global auto_test_task
        print(f"{msg.author} powiedzial '{msg.content}' ({msg.channel}) || {client.user} ")
        if msg.content == bot_self_mention_string+" autotest":
        # Cancel the existing autotest task, if any running to avoid parallelization
            if auto_test_task and not auto_test_task.done():
                auto_test_task.cancel()
        # Create an asyncio task and invoke autotest func        
            auto_test_task = asyncio.create_task(auto_test(msg)) 
        # Cancel the auto_test task if stop msg received   
        elif msg.content == bot_self_mention_string + " stop":
            await msg.channel.send("Przerywam Autotest.")
            if auto_test_task and not auto_test_task.done():
                auto_test_task.cancel() 
        else:
            await send_msg(msg, msg.content, bot_self_mention_string, private=False)

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


async def send_msg(msg, user_msg,bot_self_mention_string, private):
    # print(msg.channel.name)
    # print(msg)
    # print(msg.channel)
    if msg.channel.name in channels_on:
        if msg.content.startswith(bot_self_mention_string):
            try:
                resp_name = responses.handle_name_response(user_msg, bot_self_mention_string)
                if resp_name:
                    await msg.channel.send(resp_name)
            except Exception as E:
                print(E)
        else:
            try:
                resp = responses.handle_response(user_msg, msg.author, msg.author.id)
                if resp:
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

async def auto_test(msg):
    # Predefined lists of amount of rolls and dice
    rolls = [1, 10, 1000]  # Example rolls
    dice = ["2", "3", "4", "6", "8", "10", "12", "16", "20", "24", "30", "66", "100", "1000","20a", "20d", "100kk", "100kp", "100pk", "100k", "100p", "20*2", "20+2", "20-2", "10+2+2+5-3*2"]   # Example dice      
    # Iterate through the lists
    for roll in rolls:
        for die in dice:
            await msg.channel.send(f"{roll}d{die}")
            # Delay to avoid rate limiting by Discord
            await asyncio.sleep(2.5)
    # Send a final message indicating the completion of the auto test
    await msg.channel.send("statystyki_dnd")
    await msg.channel.send("help")
    await msg.channel.send("Zakończono Autotest.")

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
