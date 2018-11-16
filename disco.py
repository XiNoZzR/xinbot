import discord
import youtube_dl
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix = "!")
hello = "Hello"

@bot.event
async def on_ready():
    print("Bot is booting...")
    print("Hello", bot.user.name)
    print("Bot is online!")

@bot.command(pass_context = True)
async def hlp():
    await bot.say("Do you need help on something with this bot or server? Contact Xinozz for help. Twitter.com/Xinozz_")

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

@bot.command(pass_context = True)
async def hello(message):
    await bot.say("Hello!")

@bot.command(pass_context = True)
async def member_join(member):
    await member.send("Hello, welcome to the server. Enjoy your time here")

@bot.command(pass_context = True)
async def hi():
    await bot.say("Hi!")
@bot.command(pass_context = True)
async def memes():
    await bot.say("Memes are coming soon!")

@bot.command(pass_context = True)
async def sup():
    await bot.say("Sup!")

@bot.command(pass_context = True)
async def whatsup():
    await bot.say("What's up?")

@bot.command(pass_context = True)
async def howsitgoing():
    await bot.say("How's it going?")

@bot.event
async def helpp():
    if helpp.content == "help":
        await bot.say("How can I help you?")

@bot.command(pass_context = True)
async def googlesearch():
    await bot.say("The Google Search feature is coming soon for this bot.")

@bot.command(pass_context = True)
async def hosting():
    await bot.say("This bot is usually hosted on repl.it!")

@bot.command(pass_context = True)
async def on_message(message):
    if message.content.startswith:
       msg = await bot.say("Say hi or hey.")
       if msg.content == "hi":
           await bot.say("Hi!")
       if msg.content == "hello":
           await bot.say("Hello!")

@bot.command(pass_context = True)
async def github():
    await bot.say("Source code for this bot is availible at: https://github.com/XiNoZzR/xinbot")

@bot.command(pass_context = True)
async def join(ctx):
    chnl = ctx.message.author.voice_channel
    await bot.join_voice_channel(chnl)

@bot.command(pass_context = True)
async def leave(ctx):
    server = ctx.message.server
    voice_bot = bot.voice_client_in(server)
    await voice_channel.disconnect()

@bot.command(pass_context = True)
async def play(ctx, url):
    server = ctx.message.server
    voice_bot = bot.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()


bot.run("")
