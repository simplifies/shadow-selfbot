import discord
from datetime import datetime
from discord.ext import commands
from main import PREFIX, bot, EMBEDCOLOUR


class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help", description="Main help command.", usage="")
    async def help(self, ctx, *, command = None):
        if command is None:
            embed = discord.Embed(title="📚 All Commands",
                                  description=f"""Arguments in `[]` are required, arguments in `()` are optional.

`{PREFIX}`**help** » Main help command.
`{PREFIX}`**fun** » All available fun commands.
`{PREFIX}`**text** » All available text commands.
`{PREFIX}`**misc** » All available misc commands.
`{PREFIX}`**info** » All available info commands.
`{PREFIX}`**moderation** » All available moderation commands.

`{PREFIX}`**search [term]** » Search through Shadow.
`{PREFIX}`**help [command]** » Get help with a command.
""",
                                  color=EMBEDCOLOUR)
            embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)

        else:
            for cmd in bot.commands:
                if command == cmd.name:
                    embed = discord.Embed(title=f"📚 {cmd.name}",
                                          color=EMBEDCOLOUR)
                    embed.add_field(name="🧫 Usage", value=f"```{cmd.usage[1:]}```", inline=True)
                    embed.add_field(name="📝 Description", value=f"```{cmd.description}```", inline=True)
                    embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
                    embed.timestamp = datetime.now()
                    await ctx.send(embed=embed)

    @commands.command(name="search", description="Search for a command.", usage=" [term]")
    async def search(self, ctx, command = None):
        if command is not None:
            text = ""
            text2 = ""
            for cmd in bot.commands:
                if command in cmd.name or command in cmd.description:
                    text += f"`{PREFIX}`**{cmd.name}{cmd.usage}** » {cmd.description}\n"
                    text2 += f"{PREFIX}{cmd.name}{cmd.usage} » {cmd.description}\n"

            try:
                embed = discord.Embed(title="🔎 Search results...",
                                      description=f"{text}",
                                      color=EMBEDCOLOUR)
                embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed)
            except discord.HTTPException:
                await ctx.send(f"**🔎 Search results...**\n{text2}")


def setup(bot):
    bot.add_cog(Main(bot))
