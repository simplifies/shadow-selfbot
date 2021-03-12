import discord
import random
from datetime import datetime
from discord.ext import commands
from main import PREFIX, bot, EMBEDCOLOUR


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="info", description="All available info commands.", usage="")
    async def info(self, ctx):
        embed = discord.Embed(title="💁 Info Commands", description=f"""
`{PREFIX}`**userinfo [@user]** » Show information of a discord user.
`{PREFIX}`**serverinfo** » Show information of the command server.
        """, color=EMBEDCOLOUR)
        embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
        embed.timestamp = datetime.now()
        await ctx.send(embed=embed)

    @commands.command(name="userinfo", description="Show information of a discord user.", usage=" [@user]")
    async def userinfo(self, ctx, user: discord.User):
        try:
            embed = discord.Embed(title=f"🧑‍🦱 {user.name}'s information", color=EMBEDCOLOUR)
            embed.add_field(name="🆔 User ID", value=f"```{user.id}```", inline=True)
            embed.add_field(name="🏷 Username", value=f"```{user.name}```", inline=True)
            embed.add_field(name="🔢 Discriminator", value=f"```{user.discriminator}```", inline=True)
            embed.add_field(name="⏰ Created At", value="```" + str(user.created_at.strftime("%d %B, %Y")) + "```", inline=True)
            embed.set_thumbnail(url=user.avatar_url)
            embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        except discord.HTTPException:
            createdAt = user.created_at.strftime("%d %B, %Y")
            await ctx.send(f"**🧑‍🦱 {user.name}'s information**\nID: {user.id}\nUsername: {user.name}\nDiscriminator: {user.discriminator}\nCreated At: {createdAt}")

    @commands.command(name="serverinfo", description="Show information of the command server.", usage="")
    async def serverinfo(self, ctx):
        guild = ctx.message.guild

        try:
            embed = discord.Embed(title=f"‍🥡 {guild.name}'s information", color=EMBEDCOLOUR)
            embed.add_field(name="🆔 Server ID", value=f"```{guild.id}```", inline=True)
            embed.add_field(name="🏷 Server Name", value=f"```{guild.name}```", inline=True)
            embed.add_field(name="👑 Server Owner", value=f"```{guild.owner}```", inline=True)
            embed.add_field(name="⏰ Created At", value="```" + str(guild.created_at.strftime("%d %B, %Y")) + "```", inline=True)
            embed.set_thumbnail(url=guild.icon_url)
            embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        except discord.HTTPException:
            createdAt = guild.created_at.strftime("%d %B, %Y")
            await ctx.send(f"**🧑‍🦱 {user.name}'s information**\nID: {guild.id}\nName: {guild.name}\nOwner: {guild.owner}\nCreated At: {createdAt}")

def setup(bot):
    bot.add_cog(Info(bot))
