import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx: commands.Context, member: discord.Member):
        """kick a member"""
        await member.kick()

        await ctx.send(f" kicked {member.name}")

    



def setup(bot):
    bot.add_cog(Moderation(bot))
