import discord
import random
from datetime import datetime
from discord.ext import commands
from main import PREFIX, bot


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="fun", description="All available fun commands.", usage="")
    async def fun(self, ctx):
        embed = discord.Embed(title="🎢 Fun Commands", description=f"""
`{PREFIX}`**coinflip** » Flip a coin!
`{PREFIX}`**dice** » Roll a six sided dice.
`{PREFIX}`**8ball [question]** » Ask the magic eight ball a question.
`{PREFIX}`**pp [@user]** » Show someone's penis size.
        """, color=discord.Color.blue())
        embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
        embed.timestamp = datetime.now()
        await ctx.send(embed=embed)

    @commands.command(name="coinflip", description="Flip a coin!", usage="")
    async def coinflip(self, ctx):
        choices = ["Heads", "Tails"]
        choice = random.choice(choices)

        try:
            embed = discord.Embed(title=f"🪙 The coin landed on __{choice}__", color=discord.Color.blue())
            embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send(f"**🪙 The coin landed on {choice}**")

    @commands.command(name="dice", description="Roll a six sided dice.", usage="")
    async def dice(self, ctx):
        choice = random.randint(1, 6)

        try:
            embed = discord.Embed(title=f"🎲 The dice rolled __{choice}__", color=discord.Color.blue())
            embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send(f"**🎲 The dice rolled {choice}**")

    @commands.command(name="8ball", description="Ask the magic eight ball a question.", usage=" [question]")
    async def eightball(self, ctx, *, question):
        choices = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don’t count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.", "Yes.", "Yes – definitely.", "You may rely on it."]
        choice = random.choice(choices)

        try:
            embed = discord.Embed(title=f"🎱 {choice}", color=discord.Color.blue())
            embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send(f"**🎱 {choice}**")

    @commands.command(name="pp", description="Show someone's penis size.", usage=" [@user]")
    async def pp(self, ctx, user: discord.User):
        choice = "8" + "=" * random.randint(1, 12) + "D"

        try:
            embed = discord.Embed(title=f"🍆 {user.name}'s pp size: {choice}", color=discord.Color.blue())
            embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send(f"**🍆 {user.name}'s pp size: {choice}**")

def setup(bot):
    bot.add_cog(Fun(bot))
