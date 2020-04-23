import time
import discord
import random
import os


from discord.ext import commands
extensions = ["cogs.admin", "cogs.error", "cogs.help", "cogs.background_task"]
prefix = '!'
bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")
@bot.command()
async def load(extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f'cogs.{extension}')

    

@bot.event
async def on_ready():
                     # BOT IS NOW ONLINE #
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(bot.user.name, (f"now logged in!  {time.strftime('%X')}"))
            print(f"BOT ID: {bot.user.id}")
            print(f"prefix: {prefix}")
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                    # Wish happy birthday #
@bot.event
async def on_message(message):

     if message.author == bot.user: #BOT not repeating itself.
         return

     if message.content.startswith('happy birthday'):
        await message.channel.send('happy birthday!!!!  :champagne_glass:')

                       # say hi #

     if 'hello' in message.content.lower():
        rndmsg = ["Russian: Privet!","Spanish: Hola!","Estonian: Tere!","English: Hello!"]
        await message.channel.send(random.choice(rndmsg))


            # flip a coin game  #

     if message.content.startswith("!coin"):
        coins = ["heads", "tails"]
        await message.channel.send(random.choice(coins))

     await bot.process_commands(message)  # Why does on_message make my commands stop working, well this fixed it.

            ############## server join and leave #######
@bot.event
async def on_member_join(member: discord.Member):
        channel = bot.get_channel(513421327864954886)
        await channel.send (f"***{member} joined to my discord server !  :tada: ***")
        print(f"{member} joined the server  {time.strftime('%X')}")  ## koguda txt folderisse logisi ?
@bot.event
async def on_member_remove(member: discord.Member):
        channel = bot.get_channel(513421327864954886)
        await channel.send(f"***{member} has left the server..   🙋 ***")
        print(f"{member} has left the server !  {time.strftime('%X')}")

       ###### access cogs #############

if __name__ == '__main__':
	for extension in extensions:
		try:
			bot.load_extension(extension)
			print(f"Loaded cog: {extension}")
		except Exception as error:
			print(f"{extension} could not be loaded. [{error}]")
bot.run('#insert token here')
