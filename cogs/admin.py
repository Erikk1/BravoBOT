import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import asyncio

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx: commands.Context, member: discord.Member):

        await member.kick()
        await ctx.send(f" kicked {member.name}")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx: commands.Context, member:discord.Member, reason="BAN HAMMER"):

        thor_image = [
            discord.File('pics/thorbanhammer.gif'),
        ]
        await member.ban(reason=reason)
        await ctx.send(files=thor_image)
        await ctx.send(f"Member **{member.name}** got hit by a ban hammer!!!!!")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans() #all banned users
        member_name, member_discriminator = member.split('#') #split name and id

        for ban_entry in banned_users: #all banned entries
            user = ban_entry.user #pull  user from ban entry

            if (user.name, user.discriminator) == (member_name, member_discriminator): # checking if user/member matches
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned **{user.mention}**')
                return

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx,amount: int):  # clear  messages
        await ctx.channel.purge(limit=amount + 1)


               # error handlers #
    @unban.error
    async def unban_error(self, ctx, error, amount=1):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed()
            embed.add_field(name="Please specify a username with id", value="Example: !unban testaccount#1234", inline=False)
            msg = await ctx.send(embed=embed)
            await asyncio.sleep(10)
            await msg.channel.purge(limit=amount + 1)

    @clear.error
    async def clear_error(self, ctx, error, amount=1):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed()
            embed.add_field(name="Please specify the amount of numbers you want to delete", value="Example: !clear 5",
                            inline=False)
            msg = await ctx.send(embed=embed)
            await asyncio.sleep(10)
            await msg.channel.purge(limit=amount + 1)
    @kick.error
    async def kick_error(self, ctx, error, amount=1):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed()
            embed.add_field(name="Please specify a username with id", value="Example: !kick testaccount#1234",
                            inline=False)
            msg = await ctx.send(embed=embed)
            await asyncio.sleep(10)
            await msg.channel.purge(limit=amount + 1)

    @ban.error
    async def ban_error(self, ctx, error, amount=1):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed()
            embed.add_field(name="Please specify a username with id", value="Example: !ban testaccount#1234",
                            inline=False)
            msg = await ctx.send(embed=embed)
            await asyncio.sleep(10)
            await msg.channel.purge(limit=amount + 1)

def setup(bot):
    bot.add_cog(Moderation(bot))
