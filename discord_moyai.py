# moyai bot foe discord // "invented" and written by kernaltrap
import discord
import asyncio

# to add the bot, simply paste "https://discord.com/api/oauth2/authorize?client_id=844572613421301761&permissions=0&scope=bot" into web browser, and add to your discord server

# variables for bot usage
TOKEN = 'ODQ0NTcyNjEzNDIxMzAxNzYx.GyxMMx.-7LBagkFq96-FYrLgdMSWNMjaFH3IsatonEs-s'
EMOJI = '🗿'
TEXT = 'funy sound effec'
CREATOR = 'i was created by JamesIsWack // kernaltrap'
CREATOR_link = 'https://github.com/JamesIsWack'
HELP = '!spam // send the moyai 10 times.\n !creator // credits lol\n !commands // display this help message.'

intents = discord.Intents().all() # probably shouldnt do this for security
client = discord.Client(application_id=844572613421301761, intents=intents) # set app_id and use intents 

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!spam'):
        for i in range(10):
            await message.channel.send(EMOJI) # sends the moyai emoji
            await asyncio.sleep(0.1) # sleep for 0.1s until sending next message
            await message.channel.send(TEXT) # sends contents of TEXT
            await asyncio.sleep(0.3) # sleep for 0.3s until sending next message

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!creator'):
        for i in range(1):
            await message.channel.send(CREATOR) # sends conents of CREATOR
            await asyncio.sleep(0.1) # sleep for 1s until next message
            await message.channel.send(CREATOR_link) # send contents of CREATOR_link
            await asyncio.sleep(0.4) # sleep for 0.4s until next message

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!commands'):
        for i in range(1):
            await message.channel.send(HELP) # display help message
            await asyncio.sleep(0.2) # sleep for 0.2s

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        await message.channel.send('bro i cant answer you i am literally only for sending the moyai emoji, talk to my creator instead') # print this message
        await asyncio.sleep(0.8) # sleep 8th of a second
        await message.channel.send(CREATOR_link) # send creator link
        await asyncio.sleep(0.1) # sleep half a second

client.run(TOKEN)

