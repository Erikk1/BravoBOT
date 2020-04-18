import discord
from discord.ext import commands



class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        #await member.ban(reason=reason)
        await ctx.send(ctx.author.mention + "banhammer")
        if reason != None:
            await ctx.send(f"**User {member.mention} was banned by {ctx.author.mention} for:**")
            await ctx.send(f"*{reason}*")
        else:
            await ctx.send(f"**User {member.mention} was banned by {ctx.author.mention}**")


def setup(bot):
    bot.add_cog(Admin(bot)) # cogs are registered with this

    #bot.message_counter = 0

    #@bot.event
    #async def on_message(message):
        #bot.message_counter += 1
    #@bot.command()
    #async def counter(ctx):
       # print("message count:{}".format(ctx.bot.message_counter))