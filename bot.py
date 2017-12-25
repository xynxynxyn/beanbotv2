import discord
import asyncio
from twitch.api import v3 as twitch
from twitch.exceptions import ResourceUnavailableException
from random import randint
import argparse
import requests
import json
import random
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import datetime
from discord.ext import commands
import logging
import praw
import os
import configparser

try:
    import uvloop
except ImportError:
    pass
else:
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

initial_extensions = [
    'cogs.bean',
    'cogs.music',
    'cogs.lwa'
]


prefix = ['!']
bot = commands.Bot(command_prefix=prefix)



logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)



@bot.event
async def on_ready():
    print('Logged in as:')
    print('Username: ' + bot.user.name)
    print('ID: ' + bot.user.id)
    print('------')
    if not hasattr(bot, 'uptime'):
        bot.uptime = datetime.datetime.utcnow()


#Check sing is live

# async def check_sing(bot):
#     await bot.wait_until_ready()
#     while not bot.is_closed:
#         headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
#         streamer_html = requests.get('https://api.twitch.tv/kraken/streams/qoivrn?client_id=vpmzqjo3ab8dyeslvz2ia3r3yehif3', headers=headers).json()
#         streamer = json.loads(json.dumps(streamer_html))
#         stream_data  = streamer['stream']
#         if(stream_data is None):
#             reply_message = 'Qoi is offline'
#         else:
#             reply_message = 'Qoi is live'
#         await bot.change_presence(game=discord.Game(name=reply_message, url="http://www.twitch.tv/sing_sing", type=1))
#         await asyncio.sleep(60) # task runs every 60 seconds

async def check_voice(bot):
    await bot.wait_until_ready()
    while not bot.is_closed:
        clients = bot.voice_clients
        for client in clients:
            members = client.channel.voice_members
            print(members)
    await asyncio.sleep(60)
# async def check_update(bot):
#     await bot.wait_until_ready()
#     path_to_file = os.path.join("cogs", "res", "update.txt")
#     f = open(path_to_file, "r+")
#     lastpost_title = f.read()
#     while not bot.is_closed:
#         reddit = praw.Reddit(client_id='iimeQbuD4x6VlQ',
#                      client_secret='rmlfzdxhArp1MpvPK4IBJ8VWTT8',
#                      user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
#         for submission in reddit.redditor('SirBelvedere').submissions.new(limit=1):
#             newpost = submission
#         if newpost.title != lastpost_title:
#             lastpost_title = newpost.title
#             reply_message = "Dota 2 just received an update: " + str(newpost.shortlink)
#             f.seek(0)
#             f.write(lastpost_title)
#             f.truncate()
#             await bot.send_message(destination=bot.get_channel("292869746293211146"), content=reply_message)
#         await asyncio.sleep(60) # task runs every 60 seconds
        


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.author.id=="298167752017838082" :
         tidp_file = os.path.join("cogs", "res", "tidp.txt")
         f = open(tidp_file, "w")
         f.write(message.id) 
    
    
    if message.author.id=="106822120276832256" and message.content.startswith('!'):
        chance = random.randint(0,1)
        if (chance == 0):
            grill_file = os.path.join("cogs", "res", "grill_list.txt")
            with open(grill_file, "r+") as f:
                trap_list = f.read().splitlines()
                reply_message = random.choice(trap_list)
            await bot.send_message(destination=message.channel, content=reply_message)
    await bot.process_commands(message)

if __name__ == '__main__':

    configParser = configparser.RawConfigParser()   
    configfilepath = r'config.txt'
    configParser.read(configfilepath)
    token = configParser.get('Bot', 'token')
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))
    #bot.loop.create_task(check_voice(bot))
    #bot.loop.create_task(check_update(bot))
    bot.run(token)
