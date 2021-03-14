import discord
import main
import os
import json
from datetime import datetime
from discord.ext import commands
from main import PREFIX, bot, VERSION, EMBEDCOLOUR


class Themes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="themes", description="Main themes command.", usage="")
    async def themes(self, ctx):
        themeList = ""
        for theme in os.listdir("themes"):
            if theme.endswith(".json"):
                theme = theme.replace(".json", "")
                themeList += f"{theme}\n"

        try:
            embed = discord.Embed(title="🎨 Themes",
                                  color=EMBEDCOLOUR)
            embed.add_field(name="Current Theme", value=main.THEME, inline=False)
            embed.add_field(name="Theme List", value=themeList, inline=False)
            embed.add_field(name="Commands", value=f"`{PREFIX}`**theme [theme]** » Set a theme.", inline=False)
            embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
            embed.set_thumbnail(url=main.EMBEDIMAGE)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send(f"""**🎨 Themes**

__Current Theme__
{main.Theme}

__Theme List__
{themeList}
                        """)

    @commands.command(name="theme", description="Set a theme.", usage=" [theme]")
    async def theme(self, ctx, *, theme):
        validTheme = False
        if os.path.isfile(f'themes/{theme}.json'):
            validTheme = True

        if validTheme is True:
            config = json.load(open("config/config.json"))
            config["theme"] = (theme)
            json.dump(config, open('config/config.json', 'w'), sort_keys=False, indent=4)

            try:
                embed = discord.Embed(title=f"🎨 Theme", description=f"Theme set to `{theme}`. Restarting to change effect.", color=EMBEDCOLOUR)
                embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
                embed.set_thumbnail(url=main.EMBEDIMAGE)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed)
            except discord.HTTPException:
                await ctx.send(f"**🎨 Theme**\nTheme set to `{theme}`. Restarting to change effect.")

        else:
            main.print_error(f'The theme "{theme}" doesn\'t exist.')

        main.restart_bot()


def setup(bot):
    bot.add_cog(Themes(bot))
