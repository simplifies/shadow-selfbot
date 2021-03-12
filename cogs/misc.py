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

    @commands.command(name="restart", description="Restart Shadow selfbot.", usage="")
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


def setup(bot):
    bot.add_cog(Misc(bot))
