import discord
import asyncio
import argparse
import os
import requests
import json
import random
from discord.ext import commands


class LWA:
    
    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True, invoke_without_command=True)
    async def yay(self, ctx):
        """yay"""
        dir = os.path.join("cogs", "res", "lwa", "yay.txt")
        with open(dir) as f:
            lines = f.read().splitlines()
            await self.bot.say(random.choice(lines))


    @yay.command(pass_context=True, name='add')
    async def add_yay(self, ctx, *args):
        yay_link = list(args)
        link = ' '.join(yay_link)
        with open("cogs/res/lwa/yay.txt", "a+") as f:
            if(ctx.message.author.id in ['256981837056835584', '77462706893881344', '120473568382418945']):
                f.write(link)
                f.write("\n")
                reply_message = 'Image added'
            else:
                reply_message = "You are not authorized to add yays"
        await self.bot.say(reply_message)

    @commands.command(pass_context=True, invoke_without_command=True)
    async def shiny(self, ctx):
        """yay"""
        dir = os.path.join("cogs", "res", "lwa", "shiny.txt")
        with open(dir) as f:
            lines = f.read().splitlines()
            await self.bot.say(random.choice(lines))

def setup(bot):
    bot.add_cog(LWA(bot))