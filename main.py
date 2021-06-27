from random import *
import discord
import os

Feur = ['Feur', 'Feur ^^', 'Feur :relaxed:', 'Feur :hot_face:']

def end(msg):
    if(msg.endswith('quoi') or msg.endswith('quoi ?') or msg.endswith('quoi !') or msg.endswith('quoi?')):
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
        i = randint(0,3)
        await message.reply(Feur[i])

client.run(os.environ['TOKEN'])