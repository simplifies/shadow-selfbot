import discord
import random
import asyncio
import os
import json
import datetime
from discord.ext import commands

if json.load(open("config/config.json"))["token"] == "":
    os.system("cls")
    print("")
    print("Please input your Discord token below.".center(os.get_terminal_size().columns))
    print("")
    token = input()

    config = json.load(open("config/config.json"))
    config["token"] = (token)
    json.dump(config, open('config/config.json', 'w'), sort_keys=False, indent=4)
if json.load(open("config/config.json"))["prefix"] == "":
    os.system("cls")
    print("")
    print("Please input the prefix you would like to use to run commands below.".center(os.get_terminal_size().columns))
    print("")
    token = input()

    config = json.load(open("config/config.json"))
    config["prefix"] = (token)
    json.dump(config, open('config/config.json', 'w'), sort_keys=False, indent=4)

TOKEN = json.load(open("config/config.json"))["token"]
PREFIX = json.load(open("config/config.json"))["prefix"]
VERSION = "1.0"

bot = commands.Bot(command_prefix=PREFIX, self_bot=True)
bot.remove_command("help")
bot.load_extension("cogs.moderation")
bot.load_extension("cogs.fun")
bot.load_extension("cogs.info")
bot.load_extension("cogs.main")


@bot.event
async def on_ready():
    os.system("cls")
    os.system(f"title v{VERSION} loaded! | Logged into {bot.user.name}!")
    print("")
    print("Selfbot".center(os.get_terminal_size().columns))
    print("")
    print(f">> Logged into {bot.user.name}")
    print(f">> Command Prefix: {bot.command_prefix}")


@bot.event
async def on_command(ctx):
    await ctx.message.delete()
    print("[", datetime.datetime.now().strftime("%H:%M:%S"), "]", ctx.command.name)

bot.run(TOKEN, bot=False)
