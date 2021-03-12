import discord
import random
from datetime import datetime
from discord.ext import commands
from main import PREFIX, bot, EMBEDCOLOUR


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
`{PREFIX}`**rps [move]** » Rock paper scissors.
        """, color=EMBEDCOLOUR)
        embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
        embed.timestamp = datetime.now()
        await ctx.send(embed=embed)

    @commands.command(name="coinflip", description="Flip a coin!", usage="")
    async def coinflip(self, ctx):
        choices = ["Heads", "Tails"]
        choice = random.choice(choices)

        try:
            embed = discord.Embed(title=f"🪙 The coin landed on __{choice}__", color=EMBEDCOLOUR)
            embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send(f"**🪙 The coin landed on {choice}**")

    @commands.command(name="dice", description="Roll a six sided dice.", usage="")
    async def dice(self, ctx):
        choice = random.randint(1, 6)

        try:
            embed = discord.Embed(title=f"🎲 The dice rolled __{choice}__", color=EMBEDCOLOUR)
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
            embed = discord.Embed(title=f"🎱 {choice}", color=EMBEDCOLOUR)
            embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send(f"**🎱 {choice}**")

    @commands.command(name="pp", description="Show someone's penis size.", usage=" [@user]")
    async def pp(self, ctx, user: discord.User):
        choice = "8" + "=" * random.randint(1, 12) + "D"

        try:
            embed = discord.Embed(title=f"🍆 {user.name}'s pp size: {choice}", color=EMBEDCOLOUR)
            embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
            embed.timestamp = datetime.now()
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send(f"**🍆 {user.name}'s pp size: {choice}**")

    @commands.command(name="rps", description="Rock paper scissors.", usage=" [move]")
    async def rps(self, ctx, move):
        computerChoices = ["Rock", "Paper", "Scissors"]  # The list of choices the computer can choose from.
        computer = random.choice(computerChoices)  # The move the computer has chosen from a random choice in computerChoices list.
        player = move  # The choice the player is asked to make.

        if move is not None:
            # The if and else statements to check the moves.
            if player == "Rock":
                if computer == "Paper":
                    try:
                        embed = discord.Embed(title=f"You lost. {computer} covers {player}", colour=discord.Color.blue())
                        embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
                        embed.timestamp = datetime.now()
                        await ctx.send(embed=embed)
                    except discord.HTTPException:
                        await ctx.send(f"You lost. {computer} covers {player}.")
                elif computer == "Scissors":
                    try:
                        embed = discord.Embed(title=f"You won! {player} smashes {computer}", colour=discord.Color.blue())
                        embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
                        embed.timestamp = datetime.now()
                        await ctx.send(embed=embed)
                    except discord.HTTPException:
                        await ctx.send(f"You won! {player} smashes {computer}.")
                elif computer == "Rock":
                    try:
                        embed = discord.Embed(title=f"It was a tie!", colour=discord.Color.blue())
                        embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
                        embed.timestamp = datetime.now()
                        await ctx.send(embed=embed)
                    except discord.HTTPException:
                        await ctx.send(f"It was a tie!")

            elif player == "Paper":
                if computer == "Rock":
                    try:
                        embed = discord.Embed(title=f"You won! {player} covers {computer}", colour=discord.Color.blue())
                        embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
                        embed.timestamp = datetime.now()
                        await ctx.send(embed=embed)
                    except discord.HTTPException:
                        await ctx.send(f"You won! {player} covers {computer}.")
                elif computer == "Scissors":
                    try:
                        embed = discord.Embed(title=f"You lost. {computer} cuts {player}", colour=discord.Color.blue())
                        embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
                        embed.timestamp = datetime.now()
                        await ctx.send(embed=embed)
                    except discord.HTTPException:
                        await ctx.send(f"You lost. {computer} cuts {player}.")
                elif computer == "Paper":
                    try:
                        embed = discord.Embed(title=f"It was a tie!", colour=discord.Color.blue())
                        embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
                        embed.timestamp = datetime.now()
                        await ctx.send(embed=embed)
                    except discord.HTTPException:
                        await ctx.send(f"It was a tie!")

            elif player == "Scissors":
                if computer == "Paper":
                    try:
                        embed = discord.Embed(title=f"You won! {player} cuts {computer}", colour=discord.Color.blue())
                        embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
                        embed.timestamp = datetime.now()
                        await ctx.send(embed=embed)
                    except discord.HTTPException:
                        await ctx.send(f"You won! {player} cuts {computer}.")

                elif computer == "Rock":
                    try:
                        embed = discord.Embed(title=f"You lost. {computer} smashes {player}", colour=discord.Color.blue())
                        embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
                        embed.timestamp = datetime.now()
                        await ctx.send(embed=embed)
                    except discord.HTTPException:
                        await ctx.send(f"You lost. {computer} smashes {player}.")
                elif computer == "Scissors":
                    try:
                        embed = discord.Embed(title=f"It was a tie!", colour=discord.Color.blue())
                        embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
                        embed.timestamp = datetime.now()
                        await ctx.send(embed=embed)
                    except discord.HTTPException:
                        await ctx.send(f"It was a tie!")

            # If no move or an invalid move was chosen then print that instead of printing an ugly error.
            else:
                try:
                    embed = discord.Embed(title=f"That was an invalid play!", colour=discord.Color.blue())
                    embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
                    embed.timestamp = datetime.now()
                    await ctx.send(embed=embed)
                except discord.HTTPException:
                    await ctx.send(f"That was an invalid play!")

        else:
            try:
                embed = discord.Embed(title=f"That was an invalid play!", colour=discord.Color.blue())
                embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
                embed.timestamp = datetime.now()
                await ctx.send(embed=embed)
            except discord.HTTPException:
                await ctx.send(f"That was an invalid play!")

def setup(bot):
    bot.add_cog(Fun(bot))
