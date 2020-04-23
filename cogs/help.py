
import discord


from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    #@commands.Cog.listener()  # allows me to make events in cogs.
    @commands.command()
    async def help(self, ctx):

            embed = discord.Embed(title="**<<<< BOT menu >>>>**", description="**__Some useful commands__**", inline=False)
            embed.add_field(name="*happy birthday*", value=" write 'happy birthday' ", inline=False)
            embed.add_field(name="*!coin*", value=" Write 'flip a coin' ", inline=False)
            embed.add_field(name="*hello*", value=" Learn 'hello' in different languages ", inline=False)

            await ctx.send(embed=embed)


    @commands.command()
    async def info(self,ctx):
            file = discord.File("pics/boticon.png", filename="image.png")
            embed = discord.Embed(title="**__About BravoBOT__**", description="",color=0x8000ff, inline=False)
            embed.set_image(url="attachment://boticon.png")
            embed.add_field(name="------------", value="Creator: Erikk", inline=False)
            embed.add_field(name="------------", value="Created: 20/04/2020", inline=False)
            await ctx.send(file=file, embed=embed)

    @commands.command()
    async def AdminCommands(self, ctx):
            file = discord.File("pics/boticon.png", filename="image.png")
            embed = discord.Embed(title="**__Admin commands__**", description="", color=0x8000ff, inline=False)
            embed.set_image(url="attachment://boticon.png")
            embed.add_field(name="------------", value="!kick", inline=False)
            embed.add_field(name="------------", value="!ban", inline=False)
            embed.add_field(name="------------", value="!unban", inline=False)
            embed.add_field(name="------------", value="!clear  - > clear (number) messages <", inline=False)
            await ctx.send(file=file, embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))

