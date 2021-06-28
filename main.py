from random import *
import discord
import os

Feur = ['Feur', 'Feur ^^', 'Feur :relaxed:', 'Feur :hot_face:']

def end(msg):
    if(msg.endswith('quoi') or msg.endswith('quoi ?') or msg.endswith('quoi !') or msg.endswith('quoi?')):
        return True
    return False

def baka(msg):
    if 'baka' in msg.lower():
        return True
    return False

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if(end(message.content)):
        await message.reply(choice(Feur))
    
    if(baka(message.content)):
        await message.reply(file=discord.File('BAKA.mp4'))

client.run(os.environ['TOKEN'])