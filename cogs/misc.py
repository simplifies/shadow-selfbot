import discord
import main
from datetime import datetime
from discord.ext import commands
from main import PREFIX, bot, VERSION, EMBEDCOLOUR


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="misc", description="Main misc command.", usage="")
    async def misc(self, ctx):
        embed = discord.Embed(title="🧨 Misc Commands",
                              description=f"""
`{PREFIX}`**settings** » Shows selfbot settings.
`{PREFIX}`**restart** » Restart Shadow selfbot.
`{PREFIX}`**playing [status]** » Set a playing status.
`{PREFIX}`**streaming [status]** » Set a streaming status.
`{PREFIX}`**listening [status]** » Set a listening status.
`{PREFIX}`**watching [status]** » Set a watching status.
`{PREFIX}`**clearstatus** » Clear your status. 
`{PREFIX}`**nick [nickname]** » Change your nickname.
""",
                              color=EMBEDCOLOUR)
        embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
        embed.timestamp = datetime.now()
        await ctx.send(embed=embed)

    @commands.command(name="settings", description="Shows selfbot settings.", usage="")
    async def settings(self, ctx):
        totalcommands = len(bot.commands)

        try:
            embed = discord.Embed(title="⚙ Settings",
                                  color=EMBEDCOLOUR)
            embed.add_field(name="🔧 Commands", value=f"```{totalcommands}```")
            embed.add_field(name="🧩 Prefix", value=f"```{bot.command_prefix}```")
            embed.add_field(name="🧬 Version", value=f"```{VERSION}```")
            embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send(f"**⚙ Settings**\nCommands: {totalcommands}\nPrefix: {Ghost.command_prefix}")

    @commands.command(name="restart", description="Restart Shadow selfbot.", usage="", aliases=["reboot"])
    async def restart(self, ctx):
        try:
            embed = discord.Embed(title="🔁 Restarting...",
                                  color=EMBEDCOLOUR)
            embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send(f"**🔁 Restarting...**")
        main.restart_bot()

    @commands.command(name="playing", description="Set a playing status.", usage=" [status]")
    async def playing(self, ctx, *, status):
        await bot.change_presence(activity=discord.Activity(type=0, name=f"{status}"))
        try:
            embed = discord.Embed(title="🎮 Playing Status",
                                  description=f"Playing status changed to `{status}`",
                                  color=EMBEDCOLOUR)
            embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send(f"**🎮 Playing Status**\nPlaying status changed to `{status}`")

    @commands.command(name="streaming", description="Set a streaming status.", usage=" [status]")
    async def streaming(self, ctx, *, status):
        await bot.change_presence(activity=discord.Activity(type=1, name=f"{status}"))
        try:
            embed = discord.Embed(title="📸 Streaming Status",
                                  description=f"Streaming status changed to `{status}`",
                                  color=EMBEDCOLOUR)
            embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send(f"**📸 Streaming Status**\nStreaming status changed to `{status}`")

    @commands.command(name="listening", description="Set a listening status.", usage=" [status]")
    async def listening(self, ctx, *, status):
        await bot.change_presence(activity=discord.Activity(type=2, name=f"{status}"))
        try:
            embed = discord.Embed(title="🎧 Listening Status",
                                  description=f"Listening status changed to `{status}`",
                                  color=EMBEDCOLOUR)
            embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send(f"**🎧 Listening Status**\nListening status changed to `{status}`")

    @commands.command(name="watching", description="Set a watching status.", usage=" [status]")
    async def watching(self, ctx, *, status):
        await bot.change_presence(activity=discord.Activity(type=3, name=f"{status}"))
        try:
            embed = discord.Embed(title="💻 Watching Status",
                                  description=f"Watching status changed to `{status}`",
                                  color=EMBEDCOLOUR)
            embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send(f"**💻 Watching Status**\nWatching status changed to `{status}`")

    @commands.command(name="clearstatus", description="Clear your custom status.", usage="")
    async def clearstatus(self, ctx):
        await bot.change_presence(activity=discord.Activity(type=-1))
        try:
            embed = discord.Embed(title="🗑 Status Cleared",
                                  color=EMBEDCOLOUR)
            embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send(f"**🗑 Status Cleared**")

    @commands.command(name="nick", description="Change your nickname.", usage=" [nickname]")
    async def nick(self, ctx, nickname="Shadow Selfbot Is The Best"):
        await ctx.author.edit(nick=nickname)
        try:
            embed = discord.Embed(title=f"🏷 Nickname",
                                  description=f"Nickname change to `{nickname}`",
                                  color=EMBEDCOLOUR)
            embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send(f"**🏷 Nickname**\nNickname change to `{nickname}`")


def setup(bot):
    bot.add_cog(Misc(bot))
