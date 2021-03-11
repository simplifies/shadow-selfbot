import discord
from datetime import datetime
from discord.ext import commands
from main import PREFIX, bot


class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help", description="Main help command.", usage="help")
    async def help(self, ctx):
        embed = discord.Embed(title="📚 Help",
                              description=f"""Arguments in `[]` are required, arguments in `()` are optional.

`{PREFIX}`**help** » Main help command.
`{PREFIX}`**fun** » All available fun commands.
`{PREFIX}`**misc** » All available misc commands.
`{PREFIX}`**info** » All available info commands.
`{PREFIX}`**moderation** » All available moderation commands.
""",
                              color=discord.Color.blue())
        embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
        embed.timestamp = datetime.now()
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Main(bot))
