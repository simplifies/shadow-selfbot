import discord
import main
import asyncio
from datetime import datetime, timedelta
from discord.ext import commands
from main import PREFIX, bot, EMBEDCOLOUR


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        # Discord Gift sniper
        if 'discord.gift/' in message.content:
            code = message.content[message.content.find('discord.gift/') + 13:40]
            if str(len(code)) in ['16', '19']:
                try:
                    main.print_sniper("Sniper", f"Gift Code Sniper:\n{main.fg.cYellow}Link: {main.fg.cGrey}discord.gift/{code}\n{main.fg.cYellow}Message Author: {main.fg.cGrey}{message.author.name}#{message.author.discriminator}\n{main.fg.cYellow}Channel: {main.fg.cGrey}#{message.channel.name}\n{main.fg.cYellow}Server: {main.fg.cGrey}{message.guild.name}")
                except:
                    main.print_sniper("Sniper", f"Gift Code Sniper:\n{main.fg.cYellow}Link: {main.fg.cGrey}discord.gift/{code}\n{main.fg.cYellow}Message Author: {main.fg.cGrey}{message.author.name}#{message.author.discriminator}\n{main.fg.cYellow}Channel: {main.fg.cGrey}{message.channel}")

        # Giveaway sniper

        if 'GIVEAWAY' in message.content and message.author.bot and message.author.id in main.giveawayBots:
            joinTimePretty = timedelta(0, main.giveawayJoinDelay)
            main.print_sniper("Sniper", f"Giveaway Sniper:\n{main.fg.cYellow}Channel: {main.fg.cGrey}#{message.channel.name}\n{main.fg.cYellow}Server: {main.fg.cGrey}{message.guild.name}\n{main.fg.cYellow}Joining In: {main.fg.cGrey}{joinTimePretty}")
            await asyncio.sleep(main.giveawayJoinDelay)
            await message.add_reaction('\U0001F389')


def setup(bot):
    bot.add_cog(Events(bot))
