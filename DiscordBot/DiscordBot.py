import asyncio
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from googletrans import Translator
import config

client = discord.Client()
user = discord.User()

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
@client.event
async def on_member_update(before, after):
    print("member update")
    print(after.display_name)
@client.event
async def on_message(message):
    print(message.content)
    if message.content.startswith('!exit'):
        await client.close()
    else:
        translator = Translator()
        tmp = translator.translate(message.content)
        if tmp.src != "en":
            user = message.author.name
            response = user + " (translation):\n " + tmp.text
            await client.send_message(message.channel, response)
        else:
            pass


client.run(config.access_token)