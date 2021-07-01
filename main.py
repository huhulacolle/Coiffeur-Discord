from random import *
import discord
import os

Feur = ['Feur', 'Feur ^^', 'Feur :relaxed:', 'Feur :hot_face:']

def end(msg):
    if(msg.endswith('quoi') or msg.endswith('quoi ?') or msg.endswith('quoi !') or msg.endswith('quoi?')):
        return True
    return False

def baka(msg):
    if ('baka' in msg.lower()):
        return True
    return False

def dbl(id, msg):
    if(str(id) in msg):
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

    if(dbl(client.user.id, message.content)):
        await message.reply("Ptdr mais tu est débile je suis un bot je ne suis pas une vraie personne ça ne sert à rien de me parler mais vraiment ptdr tu est vraiment con")

client.run(os.environ['TOKEN'])