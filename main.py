VERSION = "1.5" # DONT EDIT THIS!

import os
import sys

os.system("cls")
os.system(f"title Loading Shadow v{VERSION}...")

import discord
import random
import asyncio
import json
from datetime import datetime
from discord.ext import commands
from sty import fg, bg, ef, rs, Style, RgbFg

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
THEME = json.load(open("config/config.json"))["theme"]

SHAREPREFIX = json.load(open("config/config.json"))["share_commands"]["prefix"]
SHARECOMMANDS = json.load(open("config/config.json"))["share_commands"]["enabled"]

PUREEMBEDCOLOUR = json.load(open(f"themes/{THEME}.json"))["embed_colour"]
EMBEDCOLOUR = int(PUREEMBEDCOLOUR.replace("#", "0x"), 0)
EMBEDIMAGE = json.load(open(f"themes/{THEME}.json"))["embed_image"]
EMBEDTITLE = json.load(open(f"themes/{THEME}.json"))["embed_title"]
GLOBALEMOJI = json.load(open(f"themes/{THEME}.json"))["global_emoji"]

giveawayBots = [294882584201003009, 716967712844414996, 810270746797670462]
giveawayJoinDelay = 25

bot = commands.Bot(command_prefix=PREFIX, self_bot=True)
bot.remove_command("help")

bot.load_extension("cogs.moderation")
bot.load_extension("cogs.fun")
bot.load_extension("cogs.info")
bot.load_extension("cogs.misc")
bot.load_extension("cogs.text")
bot.load_extension("cogs.sharecmds")
bot.load_extension("cogs.events")
bot.load_extension("cogs.themes")
bot.load_extension("cogs.main")

__consolecolour__ = "#A7A7A7"
fg.consoleColour = Style(RgbFg(int(__consolecolour__[1:3], 16), int(__consolecolour__[3:5], 16), int(__consolecolour__[5:7], 16)))

fg.cRed = Style(RgbFg(255, 81, 69))
fg.cOrange = Style(RgbFg(255, 165, 69))
fg.cYellow = Style(RgbFg(255, 255, 69))
fg.cGreen = Style(RgbFg(35, 222, 57))
fg.cBlue = Style(RgbFg(69, 119, 255))
fg.cPurple = Style(RgbFg(177, 69, 255))
fg.cPink = Style(RgbFg(255, 69, 212))

fg.cGrey = Style(RgbFg(207, 207, 207))
fg.cBrown = Style(RgbFg(199, 100, 58))
fg.cBlack = Style(RgbFg(0, 0, 0))
fg.cWhite = Style(RgbFg(255, 255, 255))

def print_cmd(command):
    print(f"{fg.consoleColour}[{fg.cWhite}" + datetime.now().strftime("%H:%M:%S") + f"{fg.consoleColour}]{fg.cWhite} | {fg.consoleColour}[{fg.cWhite}Command{fg.consoleColour}] {fg.cWhite}{command}")
def print_sharecmd(user, command):
    print(f"{fg.consoleColour}[{fg.cWhite}" + datetime.now().strftime("%H:%M:%S") + f"{fg.consoleColour}]{fg.cWhite} | {fg.consoleColour}[{fg.cWhite}Share Command{fg.consoleColour}] {fg.cWhite}({user}) {command}")
def print_error(error):
    print(f"{fg.consoleColour}[{fg.cWhite}" + datetime.now().strftime("%H:%M:%S") + f"{fg.consoleColour}]{fg.cWhite} | {fg.consoleColour}[{fg.cWhite}Error{fg.consoleColour}] {fg.cWhite}{error}")
def print_sniper(sniper, message):
    print(f"{fg.consoleColour}[{fg.cWhite}" + datetime.now().strftime("%H:%M:%S") + f"{fg.consoleColour}]{fg.cWhite} | {fg.consoleColour}[{fg.cWhite}{sniper}{fg.consoleColour}] {fg.cWhite}{message}")
def restart_bot():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def split(word):
    return list(word)

@bot.event
async def on_ready():
    os.system("cls")
    os.system(f"title Shadow v{VERSION} ─ Logged into {bot.user.name}")
    print(fg.consoleColour + "")
    print(".▄▄ ·  ▄ .▄ ▄▄▄· ·▄▄▄▄        ▄▄▌ ▐ ▄▌".center(os.get_terminal_size().columns))
    print("▐█ ▀. ██▪▐█▐█ ▀█ ██▪ ██ ▪     ██· █▌▐█".center(os.get_terminal_size().columns))
    print("▄▀▀▀█▄██▀▐█▄█▀▀█ ▐█· ▐█▌ ▄█▀▄ ██▪▐█▐▐▌".center(os.get_terminal_size().columns))
    print("▐█▄▪▐███▌▐▀▐█ ▪▐▌██. ██ ▐█▌.▐▌▐█▌██▐█▌".center(os.get_terminal_size().columns))
    print(" ▀▀▀▀ ▀▀▀ · ▀  ▀ ▀▀▀▀▀•  ▀█▄▀▪ ▀▀▀▀ ▀▪".center(os.get_terminal_size().columns))
    print("")
    print(f"Shadow v{VERSION} logged into {bot.user.name}".center(os.get_terminal_size().columns))
    print("")
    print(fg.consoleColour + '─'*os.get_terminal_size().columns)
    print("")

@bot.event
async def on_command(ctx):
    await ctx.message.delete()
    print_cmd(f"{ctx.command.name}")

@bot.event
async def on_command_error(ctx, error):
    print_error(error)
    try:
        await ctx.message.delete()
    except:
        pass

bot.run(TOKEN, bot=False)
