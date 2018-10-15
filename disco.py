import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
    print("Bot is booting...")
    print("Hello", bot.user.name)
    print("Bot is online!")

@bot.command(pass_context = True)
async def cmds():
    await bot.say("```More commands are coming soon! Current commands are: !creator, !emoji, !spam, !rickroll, !rules, !botinfo```")

@bot.command(pass_context = True)
async def commands():
    await bot.say("```More commands are coming soon! Current commands are: !creator, !emoji, !spam, !rickroll, !rules, !botinfo```")

@bot.command(pass_context = True)
async def emoji():
    await bot.say(":grinning:")

@bot.command(pass_context = True)
async def spam():
    for i in range(0,10000000000):
      await bot.say("Spaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaammmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")

@bot.command(pass_context = True)
async def creator():
	await bot.say("The creator of this bot is Xinozz. https://twitter.com/Xinozz_")

@bot.command(pass_context = True)
async def rickroll():
	await bot.say("Watch Rick Roll at: https://www.youtube.com/watch?v=dQw4w9WgXcQ")

@bot.command(pass_context = True)
async def rules():
    await bot.say("""``` 1. Be polite.
2. Respect all users and staff.
3. Obey the law of USA and EU.
4. Don't advertise anything (links etc.)
5. No adult content (pornography, nudity, gore etc.) NSFW (instant lifelong ban)
6. No death threats (instant lifelong ban)
7. Obey the Community Guidelines of Discord (https://discordapp.com/terms)
8. No racism, homophobia, sexism etc.
9. No discussions about religious or politic subjects.
10. Don't spread rumors. ```""")

@bot.command(pass_context = True)
async def botinfo():
    await bot.say("```This is a bot created by Xinozz. This bot is currently in a very early stage. More features are coming soon!```")

bot.run("")
