from random import *
import discord
import image
import os

image_types = ["png", "jpeg", "jpg"]

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

def delmem(msg):
    msg = msg.replace('!meme', '')
    msg = msg.replace(' ', '', 1)
    if(msg == ''):
        msg = 'Feur'
    return msg

def meme(msg):
    msg = delmem(msg)
    meme = image.Meme(msg, 'nomeme.jpg')
    draw = meme.draw()
    if draw.mode in ("RGBA", "P"):
        draw = draw.convert("RGB")
    draw.save('meme.jpg', optimize=True, quality=80)  

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if(end(message.content.lower())):
        await message.reply('Feur')
    
    if(baka(message.content)):
        await message.reply(file=discord.File('BAKA.mp4'))

    if(dbl(client.user.id, message.content)):
        await message.reply("?")

    if (message.content.startswith("!meme")):
        if(message.attachments):
            for attachment in message.attachments:
                if any(attachment.filename.lower().endswith(image) for image in image_types):
                    await attachment.save('nomeme.jpg')
            meme(message.content)
            await message.reply("**ATTENTION** le générateur de meme est encore en beta, des bugs ou des changements peuvent encore intervenir (faut voir huhu pour savoir ou sa en est)" ,file=discord.File('meme.jpg'))
        else:
            await message.reply('ta oublier de mettre une image')

client.run(os.environ['TOKEN'])