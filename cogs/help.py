import time
import discord
import random
import asyncio

from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.Cog.listener()  # allows me to make events in cogs.
    async def on_message(self,message):
        if message.content == "!help":
            embed = discord.Embed(title="**<<<< BOT menu >>>>**", description="**__Some useful commands__**", inline=False)
            embed.add_field(name="*happy birthday*", value=" write 'happy birthday' ", inline=False)
            embed.add_field(name="*!coin*", value=" write 'flip a coin' ", inline=False)
            embed.add_field(name="*hi*", value=" say 'hi in different languages' ", inline=False)
            await message.channel.send(content=None, embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))