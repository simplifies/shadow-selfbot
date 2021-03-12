import discord
from datetime import datetime
from discord.ext import commands
from main import PREFIX, bot, EMBEDCOLOUR


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="moderation", description="All available moderation commands.", usage="")
    async def moderation(self, ctx):
        embed = discord.Embed(title="👮 Moderation Commands", description=f"""
`{PREFIX}`**ban [@member] (reason)** » Ban a user from the command server.
`{PREFIX}`**kick [@member] (reason)** » Kick a user from the command server.
`{PREFIX}`**mute [@member] (reason)** » Mute a user from the command server.
`{PREFIX}`**unmute [@member] (reason)** » Unmute a user from the command server.
        """, color=EMBEDCOLOUR)
        embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
        embed.timestamp = datetime.now()
        await ctx.send(embed=embed)

    @commands.command(name="ban", description="Ban a user from the command server.", usage=" [@member] (reason)")
    async def ban(self, ctx, member: discord.Member, *, reason = "Undefined"):
        if ctx.author.guild_permissions.ban_members:
            await member.ban()

            try:
                embed = discord.Embed(title=f"🔨 {member.name} was banned!", description = f"Reason: {reason}", color=EMBEDCOLOUR)
                embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed)
            except discord.HTTPException:
                await ctx.send(f"**🔨 {member.name} was banned!**\nReason: {reason}")

    @commands.command(name="kick", description="Kick a user from the command server.", usage=" [@member] (reason)")
    async def kick(self, ctx, member: discord.Member, *, reason = "Undefined"):
        if ctx.author.guild_permissions.kick_members:
            await member.kick(reason=reason)

            try:
                embed = discord.Embed(title=f"👢 {member.name} was kicked!", description = f"Reason: {reason}", color=EMBEDCOLOUR)
                embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed)
            except discord.HTTPException:
                await ctx.send(f"**👢 {member.name} was kicked!**\nReason: {reason}")

    @commands.command(name="mute", description="Mute a user from the command server.", usage=" [@member] (reason)")
    async def mute(self, ctx, member: discord.Member, *, reason = "Undefined"):
        if ctx.author.guild_permissions.mute_members:
            mutedRole = get(ctx.guild.roles, name="Muted")
            await member.add_roles(mutedRole)

            try:
                embed = discord.Embed(title=f"🤐 {member.name} was muted!", description = f"Reason: {reason}", color=EMBEDCOLOUR)
                embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed)
            except discord.HTTPException:
                await ctx.send(f"**🤐 {member.name} was muted!**\nReason: {reason}")

    @commands.command(name="unmute", description="Unmute a user from the command server.", usage=" [@member] (reason)")
    async def unmute(self, ctx, member: discord.Member, *, reason = "Undefined"):
        if ctx.author.guild_permissions.mute_members:
            mutedRole = get(ctx.guild.roles, name="Muted")
            await member.remove_roles(mutedRole)

            try:
                embed = discord.Embed(title=f"😀 {member.name} was unmuted!", description = f"Reason: {reason}", color=EMBEDCOLOUR)
                embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed)
            except discord.HTTPException:
                await ctx.send(f"**😀 {member.name} was unmuted!**\nReason: {reason}")

def setup(bot):
    bot.add_cog(Moderation(bot))
