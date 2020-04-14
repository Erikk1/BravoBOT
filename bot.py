import time
import discord
import random
import asyncio

from discord.ext import tasks, commands
#channel = self.get_channel(***channel id)

#client = discord.Client()

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs,):
        super().__init__(*args, **kwargs)
        self.bg_task = self.loop.create_task(self.my_background_task()) #backround task



    async def on_ready(self):
                     # BOT IS NOW ONLINE #
            print(client.user.name , (f"now logged in!  {time.strftime('%X')}"))

                    # Wish happy birthday #

    async def on_message(self, message):
            if message.author == client.user: #BOT not repeating itself.
                return

            if message.content.startswith('happy birthday'):
                await message.channel.send('happy birthday!!!!  :champagne_glass:')

                       # say hi #

            if 'hi' in message.content.lower():
                rndmsg = ["Privet!","Hola!","Tere!","Hello!"]
                await message.channel.send(random.choice(rndmsg))

            # help section # ---> ** __ markings are for discord formatting.

            if message.content == "!help":
                embed = discord.Embed(title="**<<<< BOT menu >>>>**", description="**__Some useful commands__**")
                embed.add_field(name="*happy birthday*", value=" write 'happy birthday' ")
                embed.add_field(name="*!coin*", value=" write 'flip a coin' ")
                embed.add_field(name="*hi*", value=" say 'hi in different languages' ")
                await message.channel.send(content=None, embed=embed)

            # flip a coin game  #

            if message.content == "!coin":
                coins = ["heads", "tails"]
                await message.channel.send(random.choice(coins))

                if message.content.startswith('!ban'):
                    for member in client.get_all_members():

                        await message.channel.send(f"Banning {member.display_name}!")

            # spam message to one channel every minute  #
    async def my_background_task(self):
        await self.wait_until_ready()
        counter = 0
        channel = self.get_channel(#***channel id)
        while not self.is_closed():
            counter += 1

            ######################### random office quote post every 180 sec
            the_office_quotes = [
                discord.File("pics/1.png"),
                discord.File('pics/2.png'),
                discord.File('pics/3.png'),
                discord.File('pics/4.png'),
                discord.File('pics/5.png'),
                discord.File('pics/6.png'),
                discord.File('pics/7.png'),
                discord.File('pics/8.png'),
                discord.File('pics/9.png'),
                discord.File('pics/10.png'),

            ]
            await channel.send(file=random.choice(the_office_quotes))
            await asyncio.sleep(360)

            ############## server join and leave #######

    async def on_member_join(self,member: discord.Member):
        channel = self.get_channel(#***channel id)
        await channel.send (f"***{member} joined to my discord server !  :tada: ***")
        print(f"{member} joined the server  {time.strftime('%X')}")  ## koguda txt folderisse logisi ?

    async def on_member_remove(self,member: discord.Member):
        channel = self.get_channel(#***channel id)
        await channel.send(f"***{member} has left the server..   🙋 ***")
        print(f"{member} has left the server !  {time.strftime('%X')}")



    ################## ban / unban system ###########
    #def get_prefix(bot,message):
        #prefixes = ['!']

    @commands.command()
    @commands.has_permissions(ban_members=True, kick_members=True)
    async def ban(self,ctx, member :discord.Member, *, reason=None):
        await member.send(f'You have been banned from ever returning to the Cave. Reason: {reason}. Maybe, just maybe, you can return at a later date.')
        await member.ban(reason=reason)
        await ctx.send(f'{member} has been banned from ever coming down to the Cave. Reason: {reason}')

        #if reason == None:
            #await message.channel.send(file='pics/thorbanhammer.gif')
        #if member == None or member == message.author:
            #await message.channel.send('invalid username')

client = MyClient()
client.run('#bot token')
