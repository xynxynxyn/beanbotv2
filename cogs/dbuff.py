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
import youtube_dl
from discord.ext import commands
import time


class DotaBuff:

    def __init__(self, bot):
        self.bot = bot
        self.headers = headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'} 

    @commands.group(pass_context=True)
    async def db(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.say('Incorrect random subcommand passed.')

    @db.command(pass_context=True)
    async def reg(self, ctx, *args):
        print(str(ctx.message.author).split('#', 1)[0] + str(args[0]))
        j = open('cogs/id.json', 'r+')
        json_file = json.load(j)
        key = str(ctx.message.author).split('#', 1)[0]
        if key in json_file:
            await self.bot.say("Your Dotabuff is already registered with Beanbot.")
        else:
            print("inside else")
            json_file[str(ctx.message.author).split('#', 1)[0]] = str(args[0])
            await self.bot.say("Your Dotabuff is now registered with Beanbot")
            print(json.dumps(json_file, indent=4))
            j.seek(0)
            j.truncate()
            json.dump(json_file, j, indent=4)
        j.close()

    @db.command(pass_context=True)
    async def info(self, ctx):
        with open("cogs/id.json", 'r') as j:
            json_file = json.load(j)
            key = str(ctx.message.author).split('#', 1)[0]
            if key in json_file:
                info_url = "https://api.opendota.com/api/players/"
                db_id = json_file[key]
                info_url += db_id
                wl_url = info_url + "/wl"
                info_json = requests.get(info_url, headers=self.headers).json()
                wl_json = requests.get(wl_url, headers=self.headers).json()
                reply_message  = info_json['profile']['personaname'] + '\n\n'
                reply_message += "W/L: " 
                reply_message += str(wl_json['win'])
                reply_message += "/"
                reply_message += str(wl_json['lose'])
                em = discord.Embed(title = '', description=reply_message, colour=0xFF0000)
                em.set_author(name='BEANBot', icon_url=self.bot.user.default_avatar_url)
                await self.bot.say(embed=em)

def setup(bot):
    bot.add_cog(DotaBuff(bot))
        
