# moyai bot foe discord // "invented" and written by kernaltrap
import discord
import asyncio
import sys

# to add the bot, simply paste "https://discord.com/api/oauth2/authorize?client_id=844572613421301761&permissions=0&scope=bot" into web browser, and add to your discord server

# variables for bot usage
tokenBytes = 'MTA5MjQ1MDg3NTMyMDA1Mzc2MA.GK2Aeo.HCoMSkj2ka8H-oWiCzArICe19qR7Iighrtzqv8'
emoji = '🗿'
text = 'funy sound effec'
creator = 'i was created by JamesIsWack // kernaltrap'
creatorLink = 'https://github.com/JamesIsWack'
mention = 'bro i cant answer you i am literally only for sending the moyai emoji, talk to my creator instead'
src = "https://github.com/JamesIsWack/moyai_discord_bot"
help = '\n!spam // send the moyai 5 times.\n !creator // credits lol\n !commands // display this help message.\n !version // prints current Py Script version.\n !client // prints client version.\n !what // spam emoji one time.\n !ballsdeath // o noe deth\n !balls // the boogie'
ver = "client is running version 1.2a of moyai, run !client to see host version." 
deth = 'https://tenor.com/view/persona-persona5-morgana-catfish-mona-gif-22879397'
balls = 'https://tenor.com/view/morgana-persona5-p5-persona-dance-gif-24135947'

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

    
client.run(tokenBytes)