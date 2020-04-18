import time
import discord
import random
import os
import asyncio

from discord.ext import commands

prefix = '!'
bot = commands.Bot(command_prefix=(prefix))

@bot.command()
async def load(ctx,extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f'cogs.{extension}')



@bot.event
async def on_ready():
                     # BOT IS NOW ONLINE #
            print(bot.user.name , (f"now logged in!  {time.strftime('%X')}"))
            print(f"BOT ID: {bot.user.id}")
            print(f"prefix: {prefix}")

                    # Wish happy birthday #
@bot.event
async def on_message(message):

     if message.author == bot.user: #BOT not repeating itself.
         return

     if message.content.startswith('happy birthday'):
        await message.channel.send('happy birthday!!!!  :champagne_glass:')

                       # say hi #

     if 'hi' in message.content.lower():
        rndmsg = ["Privet!","Hola!","Tere!","Hello!"]
        await message.channel.send(random.choice(rndmsg))


            # flip a coin game  #

     if message.content.startswith("!coin"):
        coins = ["heads", "tails"]
        await message.channel.send(random.choice(coins))



        
            ############## server join and leave #######
@bot.event
async def on_member_join(member: discord.Member):
        channel = bot.get_channel(#insert channel id)
        await channel.send (f"***{member} joined to my discord server !  :tada: ***")
        print(f"{member} joined the server  {time.strftime('%X')}")  ## koguda txt folderisse logisi ?

async def on_member_remove(member: discord.Member):
        channel = bot.get_channel(#insert channel id)
        await channel.send(f"***{member} has left the server..   🙋 ***")
        print(f"{member} has left the server !  {time.strftime('%X')}")

       ###### access cogs #############
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}') # removing last 3 characters(.py)

try:
    bot.run('#insert token here')
except discord.LoginFailure:
    print("Invalid token")
    exit(1)  # exit 1 means there was issue or error
