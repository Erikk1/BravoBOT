import discord
import asyncio
import random

from discord.ext import commands

class BackgroundTask( commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bg_task = bot.loop.create_task(self.background_task(bot))  # backround task
   # def __unload(self):
       # self.bg_task.cancel()
            # spam message to one channel every minute  #
    async def background_task(self,bot):
        await bot.wait_until_ready()
        counter = 0
        channel = bot.get_channel(513441119841812480)
        while not bot.is_closed():
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

def setup(bot):
    bot.add_cog(BackgroundTask(bot))