import asyncio
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from googletrans import Translator
import config
import paramiko

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
    elif message.content.startswith('!stationeersrestart'):
        k = paramiko.RSAKey.from_private_key_file("/Users/whatever/Downloads/mykey.pem")
        c = paramiko.SSHClient()
        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("connecting")
        c.connect(hostname = "192.168.0.119", username = "thurdi", pkey = k)
        print("connected")
        commands = [ "/home/thurdi/stat_restart.sh"]
        for command in commands:
            print("Executing {0}".format( command ))
            stdin , stdout, stderr = c.exec_command(command)
            print(stdout.read())
            print("Errors")
            print(stderr.read())
        c.close()
        
        user = message.author.name
        response = user + " has initiated a server restart"
        await client.send_message(message.channel, response)
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