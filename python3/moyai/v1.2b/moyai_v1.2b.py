# moyai bot foe discord // "invented" and written by kernaltrap
import discord
import asyncio
import sys
import os
from configparser import ConfigParser

# to add the bot, simply paste "https://discord.com/api/oauth2/authorize?client_id=844572613421301761&permissions=0&scope=bot" into web browser, and add to your discord server

# config parser code, you must have the config.ini locally for it to load variables.
config = ConfigParser()
file = 'config.ini'
config.read(file)
config.sections()
# this will parse config and assign the data to that varible 
token = config["moyaiVariables"]["token"]
#emoji = config["moyaiVariables"]["emoji"] // this has been removed as it causes the moyai to not be typed correctly.
emoji = '🗿'
text = config["moyaiVariables"]["text"]
creator = config["moyaiVariables"]["creator"]
creatorLink = config["moyaiVariables"]["creatorLink"]
mention = config["moyaiVariables"]["mention"]
src = config["moyaiVariables"]["src"]
help = config["moyaiVariables"]["help"]
ver = 'client is running version 1.2b of moyai, run !client to see host version.'
deth = config["moyaiVariables"]["deth"]
balls = config["moyaiVariables"]["balls"]
intents = discord.Intents().all() # probably shouldnt do this for security
client = discord.Client(application_id=844572613421301761, intents=intents) # set app_id and use intents 
activity_string = 'spamming on {} servers'.format(len(client.guilds))

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('spamming moyais like a champ'))
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!spam'): #sends moyai emoji, and sleeps for 0.1s
         for i in range(5):
            await message.channel.send(emoji)
            await asyncio.sleep(0.1)
    if message.content.startswith('!what'): # send moyai only once.
            await message.channel.send(emoji)
            await asyncio.sleep(0.1)
    if client.user.mentioned_in(message): # when bot is mentioned, send the MENTION data.
        await message.channel.send(mention)
        await asyncio.sleep(0.1)
        await message.channel.send(creatorLink)
        await asyncio.sleep(0.1)
    if message.content.startswith('!commands'): # help list
            await message.channel.send(help)
            await asyncio.sleep(0.1)
    if message.content.startswith('!creator'): # credits.....
            await message.channel.send(creator) # sends conents of CREATOR, CREATOR_link, and sleep for some time.
            await asyncio.sleep(0.1) 
            await message.channel.send(creatorLink) 
            await asyncio.sleep(0.4)
    if message.content.startswith('!version'): # prints current bot version
            await message.channel.send(ver)
            await asyncio.sleep(0.1)
    if message.content.startswith('!client'): # prints output of sys.version (imported from sys)
            await message.channel.send(sys.version)
            await asyncio.sleep(0.1)
    if message.content.startswith('!ballsdeath'):
            await message.channel.send(deth)
            await asyncio.sleep(0.1)
    #if message.content.startswith('!balls'): // unused, doesnt work correctly. sorry kaizer
         # await message.channel.send(balls)
          #await asyncio.sleep(0.1)

    
client.run(token)
