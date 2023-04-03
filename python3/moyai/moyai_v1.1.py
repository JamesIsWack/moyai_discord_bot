# moyai bot foe discord // "invented" and written by kernaltrap
import discord
import asyncio
import sys

# to add the bot, simply paste "https://discord.com/api/oauth2/authorize?client_id=844572613421301761&permissions=0&scope=bot" into web browser, and add to your discord server

# variables for bot usage
TOKEN = 'MTA5MjQ1MDg3NTMyMDA1Mzc2MA.GxE-G5.Uz-9VwaTk5QwyQppOATH01n2EK0dmVs10Jv4PY'
EMOJI = '🗿'
TEXT = 'funy sound effec'
CREATOR = 'i was created by JamesIsWack // kernaltrap'
CREATOR_link = 'https://github.com/JamesIsWack'
MENTION = 'bro i cant answer you i am literally only for sending the moyai emoji, talk to my creator instead'
SRC = "https://github.com/JamesIsWack/moyai_discord_bot"
HELP = '\n!spam // send the moyai 10 times.\n !creator // credits lol\n !commands // display this help message.\n !version // prints current Py Script version.\n !client /. prints client version.'
VER = "client is running version 1.1 of moyai, run !client to see host version." 
print(sys.version)

intents = discord.Intents().all() # probably shouldnt do this for security
client = discord.Client(application_id=844572613421301761, intents=intents) # set app_id and use intents 

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!spam'): #sends moyai emoji, and sleeps for 0.1s
         for i in range(5):
            await message.channel.send(EMOJI)
            await asyncio.sleep(0.1)
    if client.user.mentioned_in(message): # when bot is mentioned, send the MENTION data.
        await message.channel.send(MENTION)
        await asyncio.sleep(0.1)
        await message.channel.send(CREATOR_link)
        await asyncio.sleep(0.1)
    if message.content.startswith('!commands'): # help list
        for i in range(1):
            await message.channel.send(HELP)
            await asyncio.sleep(0.1)
    if message.content.startswith('!creator'): # credits.....
        for i in range(1):
            await message.channel.send(CREATOR) # sends conents of CREATOR, CREATOR_link, and sleep for some time.
            await asyncio.sleep(0.1) 
            await message.channel.send(CREATOR_link) 
            await asyncio.sleep(0.4)

@client.event
async def on_message(message):
    if message.content.startswith('!version'): # prints current bot version
        for i in range(1):
            await message.channel.send(VER)
            await asyncio.sleep(0.1)
    if message.content.startswith('!client'): # prints output of sys.version (imported from sys)
        for i in range(1):
            await message.channel.send(sys.version)
            await asyncio.sleep(0.1)

client.run(TOKEN)