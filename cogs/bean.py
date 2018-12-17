import discord
import asyncio
from twitch.api import v3 as twitch
from twitch.exceptions import ResourceUnavailableException
from random import randint
import argparse
import os
import requests
import json
import random
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import youtube_dl
from discord.ext import commands
import time
from geopy.geocoders import Nominatim
import logging
from pybooru import Danbooru
import configparser
from datetime import date



class Bean:
    def __init__(self, bot):
        self.bot = bot
        configParser = configparser.RawConfigParser()   
        configfilepath = 'config.txt'
        configParser.read(configfilepath)
        self.danbooruUsername = configParser.get('danbooru', 'username')
        self.danbooruPassword = configParser.get('danbooru', 'password')
        self.fuccboiname = 'bonkery' 
        self.fuccboidate = date(2018, 12, 6)
        
    @commands.command(pass_context=True)
    async def mymmr(self, ctx):
        """Check your true MMR"""
        mmr = randint(0,9999)
        reply_message = 'Hey ' + str(ctx.message.author).split('#', 1)[0] if ctx.message.author.nick == None else 'Hey ' + str(ctx.message.author.nick)
        reply_message += ', your MMR is ' + str(mmr)
        reply_message += ' PogChamp' if  mmr > 5999 else ' LUL'
        await self.bot.say(reply_message)
    
    
    @commands.command(pass_context=True)
    async def gei(self, ctx, *member: discord.User):
        """big gei"""
        gei_percent = 0 if(ctx.message.author.id == "106822120276832256") else randint(0,100)
        if(member):
            if(member[0].id == "106822120276832256"):
                gei_percent = 0
            reply_message = member[0].mention + ' is '
        else:
            reply_message = 'Hey ' + ctx.message.author.mention + ', you are ' 
        reply_message += str(gei_percent) + '% gei'
        reply_message += ' WutFace' if  gei_percent > 50 else ' FeelsOkayMan'
        await self.bot.say(reply_message)

    @commands.command(pass_context=True)
    async def weeb(self, ctx, *member: discord.User):
        """VoHiYo"""
        weeb_percent = 100 if(ctx.message.author.id == "106822120276832256") else randint(0,100)
        if(member):
            if(member[0].id == "106822120276832256"):
                weeb_percent = 100
            reply_message = member[0].mention + ' is '
        else:
            reply_message = 'Hey ' + ctx.message.author.mention + ', you are ' 
        reply_message += str(weeb_percent) + '% weeb'
        reply_message += ' VoHiYo' if  weeb_percent > 50 else ' FeelsGoodMan'
        await self.bot.say(reply_message)


    @commands.command(pass_context=True)
    async def mydong(self, ctx):
        """ur mum knows about it anyway haHAA"""
        dicc = randint(0,25)
        reply_message = 'Hey ' + str(ctx.message.author).split('#', 1)[0] if ctx.message.author.nick == None else 'Hey ' + str(ctx.message.author.nick)
        reply_message = reply_message + ', your dong hangs ' + str(dicc)
        reply_message = reply_message + ' cms low KappaPride' if  dicc > 17 else reply_message + ' cms low Jebaited'
        await self.bot.say(reply_message)


    @commands.command(pass_context=True)
    async def mylove(self, ctx):
        """gachiGASM"""
        if ctx.message.author.nick == None:
            reply_message = 'Hey ' + str(ctx.message.author).split('#', 1)[0]
        else:
            reply_message = 'Hey ' + str(ctx.message.author.nick)
        reply_message = reply_message + ' your true love is '
        server = ctx.message.author.server
        member_list = [x for x in server.members]
        online_member_list = [i for i in member_list if str(i.status) == 'online']
        loveboy = random.choice(online_member_list)
        await self.bot.say(reply_message + loveboy.display_name)

    @commands.command(pass_context=True)
    async def love(self, ctx, *member: discord.User):
        """KappaPride"""
        if member == None:
            reply_message = "You need to mention a name."
        else:
            mmr = randint(0,100)
            reply_message = 'Hey ' + str(ctx.message.author).split('#', 1)[0] if ctx.message.author.nick == None else 'Hey ' + str(ctx.message.author.nick)
            reply_message += ' '.join[', your love for ', member[0].display_name, ' is around ', str(mmr), '%']
            reply_message = reply_message + ' KappaPride' if(mmr > 50) else reply_message + ' FeelsBadMan'
        await self.bot.say(reply_message)
    

    @commands.group(pass_context=True, invoke_without_command=True)
    async def kumiko(self, ctx):
        """ehhhhhh"""
        with open("cogs/res/kumiko.txt", "r+") as f:
            kumiko_img_list = f.read().splitlines()
            reply_message = random.choice(kumiko_img_list)
        await self.bot.say(reply_message)

    @kumiko.command(pass_context=True, name='add')
    async def add_kumiko(self, ctx, *args):
        kumiko_link = list(args)
        link = ' '.join(kumiko_link)
        with open("cogs/res/kumiko.txt", "a+") as f:
            if(ctx.message.author.id in ['106822120276832256', '77462706893881344']):
                f.write(link)
                f.write("\n")
                reply_message = 'Image added'
            else:
                reply_message = "You are not authorized to add rarekumikos"
        await self.bot.say(reply_message)

    @commands.command()
    async def koi(self):
        """bad taste"""
        reply_message = 'https://www.youtube.com/watch?v=DBYDvnAkiao'
        await self.bot.say(reply_message)

    @commands.command()
    async def gorgcblame(self):
        await self.bot.say("Rolling the Gorgc Wheel of Blame")
        time.sleep(2)
        with open("cogs/res/gorgcblame.txt", "r") as f:
            blame = f.readlines()
        await self.bot.say(random.choice(blame))
    @commands.command()
    async def vlecc(self):
        """Retard"""
        await self.bot.say("'my dicc is big' - Vlecxius, 201X")

    @commands.group(pass_context=True, invoke_without_command=True)
    async def grill(self, ctx):
        """not gay"""
        with open("cogs/res/grill_list.txt", "r+") as f:
            trap_list = f.read().splitlines()
            reply_message = random.choice(trap_list)
        await self.bot.say(reply_message)

    @grill.command(pass_context=True, name='add')
    async def add_grill(self, ctx, *, query:str):
        with open("cogs/res/grill_list.txt", "a+") as f:
            if(ctx.message.author.id in ['120473568382418945', '77462706893881344']):
                print(query)
                f.write(query)
                f.write("\n")
                reply_message = 'Image added'
            else:
                reply_message = "You are not authorized to add traps"
        await self.bot.say(reply_message)



    @commands.command()   
    async def explosion(self):
        """EKSUPUROOOOOSHUN"""
        expfile = os.path.join("cogs", "res", "explosion.txt")
        with open(expfile, "r") as f:
            explist = f.readlines()
        await self.bot.say(random.choice(explist))


    @commands.group(pass_context=True, invoke_without_command=True)
    async def smug(self, ctx):
        """no explanation needed"""
        with open("cogs/res/smug.txt", "r+") as f:
            smug_list = f.readlines()
        reply_message = random.choice(smug_list)
        await self.bot.say(reply_message)

    @smug.command(pass_context=True, name='add')
    async def add_smug(self, ctx, *args):
        smug_link = list(args)
        link = ' '.join(smug_link)
        with open("cogs/res/smug.txt", "a+") as f:
            if(ctx.message.author.id in ['106822120276832256', '77462706893881344']):
                f.write(link)
                f.write("\n")
                reply_message = 'Image added'
            else:
                reply_message = "You are not authorized to add rarekumikos"
        await self.bot.say(reply_message)


    @commands.command()
    async def mycolor(self):
        """cmonBruh"""
        colors = ['TriHard', 'C-Word', 'KKona', 'jew', 'pajeet', 'ANELE', 'Ruski']
        reply_message = "You're a " + random.choice(colors)
        await self.bot.say(reply_message)


    @commands.command(pass_context=True)
    async def gender(self, ctx, *args):
        """HotPokket"""
        dir = os.path.join("cogs", "res", "gender.txt")
        with open(dir) as f:
            lines = f.read().splitlines()
        auth = str(ctx.message.author).split('#', 1)[0] if ctx.message.author.nick == None else ctx.message.author.nick
        if(len(args) == 0):
            reply_message = auth + " identifies themselves as " + random.choice(lines)
        else:
            genderlist = list(args)
            gender = ' '.join(genderlist)
            print(gender)
            reply_message = gender + " identifies themselves as " + random.choice(lines) if gender.startswith('<@') or gender.startswith('@') else "Enter a valid username or role"
        await self.bot.say(reply_message)    

    @commands.command(pass_context=True)
    async def avatar(self, ctx, *member: discord.User):
        """the fucc do you need a description for"""
        reply_message = member[0].avatar_url if member else ctx.message.author.avatar_url
        await self.bot.say(reply_message)

    @commands.group(pass_context=True, invoke_without_command=True)
    async def frenzlin(self, ctx):
        """love u m8"""
        dir = os.path.join("cogs", "res", "frenzlin.txt")
        with open(dir) as f:
            lines = [x for x in f.readlines() if "imgur" not in x ]
            await self.bot.say(random.choice(lines))


    @frenzlin.command(pass_context=True, name='add')
    async def add_ritsu(self, ctx, *args):
        ritsu_link = list(args)
        link = ' '.join(ritsu_link)
        with open("cogs/res/frenzlin.txt", "a+") as f:
            if(ctx.message.author.id in ['110840185155010560', '77462706893881344']):
                f.write(link)
                f.write("\n")
                reply_message = 'Image added'
            else:
                reply_message = "You are not authorized to add ritsus"
        await self.bot.say(reply_message)



    @commands.command()
    async def haidomo(self):
        """bacchuaru youtuba"""
        dir = os.path.join("cogs", "res", "kizuna.txt")
        with open(dir) as f:
            lines = f.read().splitlines()
            await self.bot.say(random.choice(lines))

    @commands.command()
    async def havocc(self):
        """gei"""
        dir = os.path.join("cogs", "res", "havok.txt")
        with open(dir) as f:
            lines = f.readlines()
            await self.bot.say(random.choice(lines))


    @commands.command()
    async def bean(self):
        """BEANED"""
        await self.bot.say("http://i0.kym-cdn.com/photos/images/facebook/001/166/993/284.png")
    
    @commands.command(pass_context=True)
    async def danbooru(self, ctx, *query : str):
        banned_terms = ["loli", "kanna_kamui+rating:q", "kanna_kamui+rating:s", "kanna_kamui+rating:e", "kanna_kamui", "kannakamui(dragon)_(maidragon)+rating:q", "kobayashi-san_chi_no_maidragon+white_hair", "rating:q+kanna_kamui", "rating:questionable+kanna_kamui"]
        search_string = query[0]
        if (query and search_string in banned_terms):
            await self.bot.say("https://i.imgur.com/PgN2R1J.png")
        else:
            if "+rating:e" in search_string and ctx.message.channel is not self.bot.get_channel("298289150581538816"):
                search_string = search_string.replace("+rating:e", "+rating:s")
            if "+rating:q" in search_string and ctx.message.channel is not self.bot.get_channel("298289150581538816"):
                search_string = search_string.replace("+rating:q", "+rating:s")
        search_string = ' '.join(search_string.split('+'))
        client = Danbooru('danbooru', username=self.danbooruUsername, api_key=self.danbooruPassword)
        response = client.post_list(tags=search_string, limit=1, random=True)   
        print(response)
        try:
            response_url = response[0]["file_url"]
            if response_url.startswith("https") == False:
                response_url = response_url.replace("/data/", "/data/__")
                response_url = "https://danbooru.donmai.us" + response_url
            await self.bot.say(response_url)
        except:
            await self.bot.say("There's something wrong with your query, because I can't find anything with that tag.")    

    @commands.command(pass_context=True)
    async def nyx(self, ctx):
        img = os.path.join("cogs", "res", "nyx.png")
        await self.bot.send_file(ctx.message.channel, fp=img)
    
    @commands.command(pass_context=True)
    async def nyxkoi(self, ctx):
        await self.bot.say("https://i.imgur.com/xabuEyd.jpg")

    @commands.command()
    async def christmas(self):
        dir = os.path.join("cogs", "res", "padoruids.txt")
        with open(dir) as f:
            lines = f.readlines()
            await self.bot.say("https://imgur.com/" + random.choice(lines))

    @commands.command()
    async def givemetheipofeveryoneinthischat(self):
        reply_message = '.'.join([str(randint(0, 255)) for x in range(4)])
        await self.bot.say(reply_message)
    
    @commands.command(pass_context=True)
    async def fuccboi(self, ctx):
        server = ctx.message.author.server
        member_list = [x for x in server.members]
        self.fuccboiname = random.choice(member_list).display_name if self.fuccboidate != date.today() else self.fuccboiname
        reply_message = "Today's fuccboi is " + self.fuccboiname
        await self.bot.say(reply_message)

def setup(bot):
    bot.add_cog(Bean(bot))
