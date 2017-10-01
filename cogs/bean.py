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
from google import google
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import youtube_dl
from discord.ext import commands
import time
from geopy.geocoders import Nominatim
import logging



class Bean:
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, *args):
        """Check if a streamer is online"""
        streamer = None
        if len(args) == 0:
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
            streamer_html = requests.get('https://api.twitch.tv/kraken/streams/sing_sing?client_id=vpmzqjo3ab8dyeslvz2ia3r3yehif3', headers=headers).json()
            streamer = json.loads(json.dumps(streamer_html))
            stream_data  = streamer['stream']
            game = stream_data['game']
            if(stream_data == None):
                reply_message = 'Master Sing is offline. FeelsBadMan'
            else:
                reply_message = 'Master Sing is playing '
                reply_message = reply_message + str(game)
                reply_message = reply_message + ' - http://www.twitch.tv/sing_sing '
                print(reply_message)

                    
        else:
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
            url = 'https://api.twitch.tv/kraken/streams/'
            url = url + str(args[0])
            url= url + '?client_id=vpmzqjo3ab8dyeslvz2ia3r3yehif3'
            streamer_html = requests.get(url, headers=headers).json()
            streamer = json.loads(json.dumps(streamer_html))
            if streamer == None:
                reply_message = 'No such stream found'
            else:  
                stream_data  = streamer['stream']
               
                reply_message = 'http://www.twitch.tv/'
                if stream_data == None:
                    reply_message += args[0]
                    reply_message += ' is offline'
                else:
                    game = stream_data['game']
                    reply_message += args[0]
                    reply_message += ' is playing '
                    reply_message += str(game)

        await self.bot.say(reply_message) #yay







    @commands.command()
    async def streams(self):
        """Top 5 Dota Streams live"""
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        streamer_html = requests.get('https://api.twitch.tv/kraken/streams?game=Dota%202&client_id=vpmzqjo3ab8dyeslvz2ia3r3yehif3&broadcaster_language=en', headers=headers).json()
        streamer = json.loads(json.dumps(streamer_html))
        stream_data = streamer['streams']
        i = 1
        reply_message = """
        Top 5 Dota streams:\n\n"""
        for stream in stream_data[:5]:
            name = stream['channel']['display_name']
            url = "https://www.twitch.tv/" + stream['channel']['name']
            reply_message = reply_message + str(i)
            reply_message = reply_message + ". "
            reply_message = reply_message + name
            reply_message = reply_message + " - <"
            reply_message = reply_message + url
            reply_message = reply_message + ">\n\n"
            i+=1
        em = discord.Embed(title = '', description=reply_message, colour=0x6441A5)
        await self.bot.say(embed=em)




            

    @commands.command(pass_context=True)
    async def mymmr(self, ctx):
        """Check your true MMR"""
        mmr = randint(0,9999)
        if ctx.message.author.nick == None:
            reply_message = 'Hey ' + str(ctx.message.author).split('#', 1)[0]
        else:
            reply_message = 'Hey ' + str(ctx.message.author.nick)
        reply_message = reply_message + ', your MMR is ' + str(mmr)
        if  mmr > 5999:
            reply_message = reply_message + ' PogChamp'
        else:
            reply_message = reply_message + ' LUL'
        await self.bot.say(reply_message)



        

    @commands.command(pass_context=True)
    async def mydong(self, ctx):
        """ur mum knows about it anyway haHAA"""
        mmr = randint(0,25)
        if ctx.message.author.nick == None:
            reply_message = 'Hey ' + str(ctx.message.author).split('#', 1)[0]
        else:
            reply_message = 'Hey ' + str(ctx.message.author.nick)
        reply_message = reply_message + ', your dong hangs ' + str(mmr)
        if  mmr > 17:
            reply_message = reply_message + ' cms low KappaPride'
        else:
            reply_message = reply_message + ' cms low Jebaited'
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
        online_list = [i for i in member_list if str(i.status) == 'online']
        loveboy = random.choice(online_list)
        await self.bot.say(reply_message + loveboy.display_name)

    @commands.command(pass_context=True)
    async def love(self, ctx, *args):
        """Kappapride"""
        if len(args) == 0:
            reply_message = "You need to mention a name."
        else:
            genderlist = list(args)
            gender = ' '.join(genderlist)
            mmr = randint(0,100)
            if ctx.message.author.nick == None:
                reply_message = 'Hey ' + str(ctx.message.author).split('#', 1)[0]
            else:
                reply_message = 'Hey ' + str(ctx.message.author.nick)
            reply_message = reply_message + ', your love for '
            reply_message = reply_message +  gender
            reply_message = reply_message + ' is around '
            reply_message = reply_message + str(mmr)
            if(mmr > 50):
                reply_message = reply_message + '%'
                reply_message = reply_message + ' KappaPride'
            else:
                reply_message = reply_message + '%'
                reply_message = reply_message + ' FeelsBadMan'
        await self.bot.say(reply_message)
    



    @commands.group(pass_context=True, invoke_without_command=True)
    async def kumiko(self, ctx):
        with open("cogs/res/kumiko.txt", "r+") as f:
            kumiko_list = f.read().splitlines();
            reply_message = random.choice(kumiko_list)
        await self.bot.say(reply_message)

    @kumiko.command(pass_context=True, name='add')
    async def addk(self, ctx, *args):
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
    # @commands.command()
    # async def kumiko(self):
    #     dir = os.path.join("cogs", "res", "kumiko.txt")
    #     with open(dir) as f:
    #         lines = f.read().splitlines()
    #         await self.bot.say(random.choice(lines))
   
   
    @commands.group(pass_context=True, invoke_without_command=True)
    async def succ(self, ctx):
        with open("cogs/res/succ.txt", "r+") as f:
            kumiko_list = f.read().splitlines();
            reply_message = random.choice(kumiko_list)
        await self.bot.say(reply_message)

    @succ.command(pass_context=True, name='add')
    async def add(self, ctx, *, query:str):
        with open("cogs/res/succ.txt", "a+") as f:
            if(ctx.message.author.id in ['106822120276832256', '77462706893881344']):
                print(query)
                f.write(query)
                f.write("\n")
                reply_message = 'Image added'
            else:
                reply_message = "You are not authorized to add rarekumikos"
        await self.bot.say(reply_message)


    @commands.command(pass_context=True)
    async def weeb(self, ctx):
        """VoHiYo"""
        if str(ctx.message.author) == 'HERE I AM - Puck 2016#5286':
            reply_message = "You are not allowed to use this command you fake weeb"
        else:
            reply_message = "WEEB VoHiYo THE VoHiYo NORMIES VoHiYo AWAY"

        await self.bot.say(reply_message)





    @commands.command()
    async def koi(self):
        reply_message = 'https://www.youtube.com/watch?v=gK57X6WWi5E'
        await self.bot.say(reply_message)





    @commands.command()
    async def vlecxius(self):
        """Retard"""
        await self.bot.say('http://i3.kym-cdn.com/photos/images/newsfeed/001/242/766/46c.png')




    @commands.command()
    async def wutface(self):
        """HAI DOMO"""
        await self.bot.say('https://cdn.discordapp.com/attachments/259440947434225664/297810508650905611/16998849_993717407439407_6365115539161661315_n.jpg')





    @commands.command()
    async def uniok(self):
        """:ok_hand:"""
        await self.bot.say('http://i.imgur.com/HdxYRqM.png')


        
    @commands.command()
    async def matupls(self):
        """dat ass"""
        await self.bot.say('https://gfycat.com/SlightVastCottonmouth')



    @commands.command()
    async def culture(self):
        """Ah"""
        with open("cogs/res/culture.txt") as f:
            cultlist = f.read().splitlines()
        await self.bot.say(random.choice(cultlist))


    @commands.group(pass_context=True, invoke_without_command=True)
    async def grill(self, ctx):
        with open("cogs/res/grill_list.txt", "r+") as f:
            trap_list = f.read().splitlines();
            reply_message = random.choice(trap_list)
        await self.bot.say(reply_message)

    @grill.command(pass_context=True, name='add')
    async def add(self, ctx, *, query:str):
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
        grill_list = ['https://cdn.discordapp.com/attachments/259440947434225664/299169011030294529/17759703_1225066617591719_652388841780661578_n.jpg',
                                  'https://cdn.discordapp.com/attachments/259440947434225664/299169012317814784/299442.jpg',
                                  'https://cdn.discordapp.com/attachments/259440947434225664/299169014222028810/17795722_10212222788942910_508290901603216617_n.jpg',
                                  'https://cdn.discordapp.com/attachments/259440947434225664/299169016201871360/17796264_1133601226748505_2122562440588666354_n.jpg',
                                  'https://cdn.discordapp.com/attachments/259440947434225664/299169017426477056/17760916_1396122297114761_6981183599349534997_o.jpg',
                                  'https://cdn.discordapp.com/attachments/259440947434225664/299169021318660108/CcmCfJuW8AAtsw8.jpg',
                                  'https://cdn.discordapp.com/attachments/259440947434225664/299169032479703040/flat1000x1000075f.u5.jpg',
                                  'https://cdn.discordapp.com/attachments/259440947434225664/299169034937696266/2HoYcaN.png',
                                  'https://cdn.discordapp.com/attachments/259440947434225664/299169039148646400/Megumin_main_image.png',
                                  'https://cdn.discordapp.com/attachments/259440947434225664/299169053958733825/Konosuba-1.jpg',
                                  'https://cdn.discordapp.com/attachments/259440947434225664/299169075505135626/687474703a2f2f34352e6d656469612e74756d626c722e636f6d2f3166646564303566323938626661646437626633623363.gif',
                                  'https://cdn.discordapp.com/attachments/259440947434225664/299169075760857088/nICa2zf.jpg',
                                  'https://cdn.discordapp.com/attachments/259440947434225664/299169085286252544/wQL7geT.jpg',
                                  'https://cdn.discordapp.com/attachments/259440947434225664/299169092735205386/tumblr_o2ejc7yXPF1s21xzoo1_500.gif',
                                  'https://cdn.discordapp.com/attachments/259440947434225664/299169109202173952/fg6nRds.png',
                                  'https://cdn.discordapp.com/attachments/292869746293211146/303203627697176607/eJwFwUEOgyAQAMC_8ADWBbK43pqe7c30TJCgiQpl8dT07535qrsdalJb71UmgHWXWNqqpZcWctK5lHykUHfRsZwQeg9xO9PVBQyb.png'
                                ]
        random.shuffle(grill_list)
        reply_message = grill_list[0]
        await self.bot.say(reply_message)


    @commands.command(pass_context=True)
    async def smug(self, ctx):
        smug_list = ['https://cdn.discordapp.com/attachments/299190496964771841/299191233245478913/1459243739540.jpg',
                                      'https://cdn.discordapp.com/attachments/299190496964771841/299191240052965376/1444236147368.png',
                                      'https://cdn.discordapp.com/attachments/299190496964771841/299191248886038529/1436640383591-3.png',
                                      'https://cdn.discordapp.com/attachments/299190496964771841/299191250861555712/1436640383572-0.jpg',
                                      'https://cdn.discordapp.com/attachments/299190496964771841/299191287456727043/1376763247995.png',
                                      'https://cdn.discordapp.com/attachments/299190496964771841/299191291697299458/1371730299235.png',
                                      'http://i.imgur.com/1Otx4Td.jpg', #done
                                      'http://i.imgur.com/GnoPQEE.png', #done
                                      'http://i.imgur.com/ft26qTV.png', #done
                                      'http://i.imgur.com/aUDo3cc.jpg', #done
                                      'http://i.imgur.com/41rr3aF.png', #done
                                      'http://i.imgur.com/4cit8Uv.jpg', #done
                                      'http://i.imgur.com/6Nwdbgu.png', #done
                                      'http://i.imgur.com/dVC01Om.jpg', #done
                                      'https://cdn.discordapp.com/attachments/292869746293211146/300994617619513356/1471581644134.png',
                                      'http://i.imgur.com/SKdcPMj.jpg', #done
                                      'http://i.imgur.com/PgrjemU.png', #done
                                      'http://i.imgur.com/NAIlQoc.png', #done
                                      'http://i.imgur.com/gZ6muFD.png',
                                      'https://img.fireden.net/a/image/1460/24/1460248889597.png',
                                      'http://i.imgur.com/54WNmGT.jpg' #done
                                    ]
        random.shuffle(smug_list)
        if str(ctx.message.author) == 'koi#9765':
            reply_message = 'http://i.imgur.com/TAFmyQv.jpg'
        else:
            reply_message = smug_list[0]
        await self.bot.say(reply_message)

    @commands.command()
    async def thinking(self):
        reply_message = 'https://cdn.discordapp.com/attachments/292869746293211146/300253029389565952/a9ef568c4c133ad983e836b5bcb90bcae68feb3190df7e37aa51958678c94134.png'
        await self.bot.say(reply_message)

    @commands.command()
    async def smorc(self):
        await self.bot.say('https://cdn.discordapp.com/attachments/292869746293211146/300989271316365312/')
        
    @commands.command()
    async def roll(self, *args):
        """Rolls a dice in NdN format."""
        limit = 6
        rolls = 1
        for ar in args:
            print(ar)
        if len(args) == 0:
            limit = 6
            rolls = 1
        elif len(args) == 1:
            limit = int(args[0])
            rolls = 1
        elif len(args) == 2:
            limit = int(args[0])
            rolls = int(args[1])
        await self.bot.say(":game_die: Rolling the dice")
        time.sleep(2)
        result = ','. join(str(random.randint(1, limit)) for r in range(rolls))
        await self.bot.say(":game_die: You got " + str(result))

    @commands.command()
    async def mycolor(self):
        colors = ['TriHard', 'MingLee', 'KKona', 'jew', 'pajeet', 'ANELE', 'Ruski']
        reply_message = 'You a ' + random.choice(colors)
        await self.bot.say(reply_message)

    @commands.command(pass_context=True)
    async def gender(self, ctx, *args):
        dir = os.path.join("cogs", "res", "gender.txt")
        with open(dir) as f:
            lines = f.read().splitlines()
        if ctx.message.author.nick == None:
            auth = str(ctx.message.author).split('#', 1)[0]
        else:
            auth = ctx.message.author.nick
        if(len(args) == 0):
            reply_message = auth + " identifies themselves as " + random.choice(lines)
        else:
            genderlist = list(args)
            gender = ' '.join(genderlist)
            print(gender)
            if(gender.startswith('<@') or gender.startswith('@')):
                reply_message = gender + " identifies themselves as " + random.choice(lines)
            else:
                reply_message = "Enter a valid username or role"
        await self.bot.say(reply_message)       

    @commands.command(pass_context=True)
    async def nuke(self, ctx, *args):
        if(len(args) == 0):
            print("no args")
            reply_message = "Enter a location name"
        else:
            addrlist = list(args)
            addr = ' '.join(addrlist)
            if(addr.lower() == 'pyongyang'):
                url = "http://i1.mirror.co.uk/incoming/article7842826.ece/ALTERNATES/s615/Kim-Jong-Un.jpg"
            else:
                geolocator = Nominatim()
                location = geolocator.geocode(addr)
                print("got lat and long")
                reply = str(location.latitude)
                print(location.latitude)
                #options = {"quiet": "", "xvfb": "", "javascript-delay": "30000", "height": "600", "width": "800", "images": ""}
                url = "https://nuclearsecrecy.com/nukemap/?&kt=100000&lat={}&lng={}&hob_opt=1&hob_psi=5&hob_ft=47553&ff=52&zm=9".format(location.latitude, location.longitude)
                #imgkit.from_url(url, dir, options=options)

        #            '''  display = Display(visible=0, size=(800, 600))
        #             display.start()

        #             browser = webdriver.Firefox()
        #             browser.get(url)
        #             browser.save_screenshot(dir)
        #             browser.quit()
        #  '''
                # display.stop()
        await self.bot.say(url)


    @commands.command(pass_context=True)
    async def fuccboi(self, ctx):
        dir = os.path.join("cogs", "res", "fuccboi.json")
        today_date = date.today()
        with open(dir, "r+") as f:
            try:
                j = json.load(f)
            except:
                j = {
                        str(ctx.message.server): {
                            "date": "",
                            "fuccboi": ""
                        }
                    }
            if(j[str(ctx.message.server)]["date"] == str(today_date)):
                fuccboi = await self.bot.get_user_info(j[str(ctx.message.server)]["fuccboi"])
                print(fuccboi)
                print(fuccboi.id)

            else:
                member_list = ctx.message.server.members
                online_list = [i for i in member_list if str(i.status) == 'online']
                fuccboi = random.choice(online_list)
                print(fuccboi.mention)
                j[str(ctx.message.server)]["fuccboi"] = fuccboi.id
                j[str(ctx.message.server)]["date"] = str(today_date)
                f.seek(0)
                json.dump(j, f, indent=4)
                f.truncate()
        await self.bot.say("Today's fuccboi is "+ fuccboi.mention)


    # @commands.command(pass_context=True)
    # async def frenzlin(self, ctx):
    #     func_list = ['gender', 'mydong', 'mymmr', 'mycolor', 'smug', 'fuccboi']
    #     await eval(random.choice(func_list))(self,ctx)

    @commands.command()
    async def haidomo(self):
        dir = os.path.join("cogs", "res", "kizuna.txt")
        with open(dir) as f:
            lines = f.read().splitlines()
            await self.bot.say(random.choice(lines))

    @commands.command()
    async def bean(self):
        await self.bot.say("http://i0.kym-cdn.com/photos/images/facebook/001/166/993/284.png")


    @commands.command(pass_context=True)
    async def tidp(self,ctx):
        tidp_file =  os.path.join("cogs", "res", "tidp.txt")
        f = open(tidp_file)
        message_id = str(f.read())
        print(message_id)
        img = os.path.join("cogs", "res", "unknown.png")

        if(ctx.message.author.id=="298167752017838082"):
            await self.bot.send_file(ctx.message.channel, fp=img)
        else:
            tidp_message = await self.bot.get_message(self.bot.get_channel("292869746293211146"), message_id)
            await self.bot.add_reaction(tidp_message, '🇸')
            await self.bot.add_reaction(tidp_message, '🇹')
            await self.bot.add_reaction(tidp_message, '🇫')
            await self.bot.add_reaction(tidp_message, '🇺')
            await self.bot.add_reaction(tidp_message, '🇰')
            await self.bot.add_reaction(tidp_message, '🇮')
            await self.bot.add_reaction(tidp_message, '🇩')
            await self.bot.add_reaction(tidp_message, '🇵')
        




def setup(bot):
    bot.add_cog(Bean(bot))
