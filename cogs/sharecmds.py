import discord
import main
from datetime import datetime
from discord.ext import commands
from main import PREFIX, bot, EMBEDCOLOUR, SHAREPREFIX, SHARECOMMANDS


class ShareCmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="share", description="Main share command.", usage="")
    async def help(self, ctx):
        if SHARECOMMANDS is True:
            embed = discord.Embed(title="🤝 Share Commands",
                                  description=f"""
`{SHAREPREFIX}`**bold [message]** » Send messages in bold.
`{SHAREPREFIX}`**italic [message]** » Send messages in italic.
`{SHAREPREFIX}`**secret [message]** » Send messages in secret.
`{SHAREPREFIX}`**code [message]** » Send messages in code.
`{SHAREPREFIX}`**embed [message]** » Send messages in an embedded message.
    """,
                                  color=EMBEDCOLOUR)
        else:
            embed = discord.Embed(title="🤝 Share Commands",
                                  description=f"Share commands are disabled.",
                                  color=EMBEDCOLOUR)
        embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
        embed.timestamp = datetime.now()
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if SHARECOMMANDS is True:
            if message.content.startswith(SHAREPREFIX + "help"):
                main.print_sharecmd(message.author.name, "help")
                try:
                    embed = discord.Embed(title="🤝 Share Commands",
                                          description=f"""
`{SHAREPREFIX}`**bold [message]** » Send messages in bold.
`{SHAREPREFIX}`**italic [message]** » Send messages in italic.
`{SHAREPREFIX}`**secret [message]** » Send messages in secret.
`{SHAREPREFIX}`**code [message]** » Send messages in code.
`{SHAREPREFIX}`**embed [message]** » Send messages in an embedded message.
                    """,
                                          color=EMBEDCOLOUR)
                    embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
                    embed.timestamp = datetime.now()
                    await message.channel.send(embed=embed)
                except discord.HTTPException:
                    await message.channel.send("**🤝 Share Commands**\n")

            if message.content.startswith(SHAREPREFIX + "bold"):
                main.print_sharecmd(message.author.name, "bold")
                arg1 = message.content.split(" ", 1)
                arg1 = arg1[1]
                await message.channel.send(f"**{arg1}**")

            if message.content.startswith(SHAREPREFIX + "italic"):
                main.print_sharecmd(message.author.name, "italic")
                arg1 = message.content.split(" ", 1)
                arg1 = arg1[1]
                await message.channel.send(f"*{arg1}*")

            if message.content.startswith(SHAREPREFIX + "secret"):
                main.print_sharecmd(message.author.name, "secret")
                arg1 = message.content.split(" ", 1)
                arg1 = arg1[1]
                await message.channel.send(f"||{arg1}||")

            if message.content.startswith(SHAREPREFIX + "code"):
                main.print_sharecmd(message.author.name, "code")
                arg1 = message.content.split(" ", 1)
                arg1 = arg1[1]
                await message.channel.send(f"```{arg1}```")

            if message.content.startswith(SHAREPREFIX + "embed"):
                main.print_sharecmd(message.author.name, "embed")
                arg1 = message.content.split(" ", 1)
                arg1 = arg1[1]
                try:
                    embed = discord.Embed(title=arg1, color=EMBEDCOLOUR)
                    await message.channel.send(embed=embed)
                except discord.HTTPException:
                    pass

def setup(bot):
    bot.add_cog(ShareCmds(bot))
