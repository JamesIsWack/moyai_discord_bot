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
help = '!spam // send the moyai 5 times.\n!creator // credits lol\n!commands // display this help message.\n!version // prints current Py Script version.\n!client // prints client version.\n!what // spam emoji one time.\n!ballsdeath // o noe deth'
ver = 'client is running version 2.0.040423 of moyai, run !client to see host version.'
deth = config["moyaiVariables"]["deth"]
balls = config["moyaiVariables"]["balls"]
error80010017 = config["moyaiVariables"]["error80010017"]
error80010007 = config["moyaiVariables"]["error80010007"]
ps2blackscreen = config["moyaiVariables"]["ps2blackscreen"]
error80029C7F = config["moyaiVariables"]["error80029C7F"]
error80010009 = 'this is related to PARAM.SFO and/or DEBUG SELF on RETAIL (DEX EBOOT on CEX). to fix, redownload the EBOOT/PARAM.SFO from here: https://archive.midnightchannel.net/SonyPS/PS3/Disc%20Repair/'
evilnat = config["moyaiVariables"]["evilnat"]
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
    if message.content.startswith('!commands errors'):
         await message.channel.send(help_err)
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
    if message.content.startswith('.err 80010017'):
        await message.channel.send(error80010017)
        await asyncio.sleep(0.1)
    if message.content.startswith('.err 80010007'):
        await message.channel.send(error80010007)
        await asyncio.sleep(0.1)
    if message.content.startswith('.err ps2blackscreen'):
        await message.channel.send(ps2blackscreen)
        await asyncio.sleep(0.1)
    if message.content.startswith('.err 80029C7F'):
        await message.channel.send(error80029C7F)
        await asyncio.sleep(0.1)
    if message.content.startswith('.err 80010009'):
        await message.channel.send(error80010009)
        await asyncio.sleep(0.1)
    if message.content.startswith('.dl evilnat'):
        await message.channel.send(evilnat)
        await asyncio.sleep(0.1)


client.run(token)