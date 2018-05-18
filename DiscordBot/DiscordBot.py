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
#J33P's stationeers controls
    elif message.content.startswith('!stationeersrestart'):
        k = paramiko.RSAKey.from_private_key_file("/usr/src/app/private.pem")
        c = paramiko.SSHClient()
        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("connecting")
        c.connect(hostname = config.docker_ip, username = config.docker_username, pkey = k)
        print("connected")
        commands = [ "sudo /home/thurdi/stat_control_jeep.sh -o restart" ]
        for command in commands:
            print("Executing {0}".format( command ))
            stdin , stdout, stderr = c.exec_command(command)
            print(stdout.read())
        c.close()
        user = message.author.name
        response = user + " has initiated a server restart"
        await client.send_message(message.channel, response)
    elif message.content.startswith('!stationeersstart'):
        k = paramiko.RSAKey.from_private_key_file("/usr/src/app/private.pem")
        c = paramiko.SSHClient()
        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("connecting")
        c.connect(hostname = config.docker_ip, username = config.docker_username, pkey = k)
        print("connected")
        commands = [ "sudo /home/thurdi/stat_control_jeep.sh -o start" ]
        for command in commands:
            print("Executing {0}".format( command ))
            stdin , stdout, stderr = c.exec_command(command)
            print(stdout.read())
        c.close()
        user = message.author.name
        response = user + " has started the server."
        await client.send_message(message.channel, response)
    elif message.content.startswith('!stationeersstop'):
        k = paramiko.RSAKey.from_private_key_file("/usr/src/app/private.pem")
        c = paramiko.SSHClient()
        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("connecting")
        c.connect(hostname = config.docker_ip, username = config.docker_username, pkey = k)
        print("connected")
        commands = [ "sudo /home/thurdi/stat_control_jeep.sh -o stop" ]
        for command in commands:
            print("Executing {0}".format( command ))
            stdin , stdout, stderr = c.exec_command(command)
            print(stdout.read())
        c.close()
        user = message.author.name
        response = user + " has stopped the server."
        await client.send_message(message.channel, response)
#BeardSyndicate's eco controls
    elif message.content.startswith('!ecorestart'):
        k = paramiko.RSAKey.from_private_key_file("/usr/src/app/private.pem")
        c = paramiko.SSHClient()
        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("connecting")
        c.connect(hostname = config.eco_ip, username = config.eco_username, pkey = k)
        print("connected")
        commands = [ "sudo /home/eco/eco_control.sh -o restart" ]
        for command in commands:
            print("Executing {0}".format( command ))
            stdin , stdout, stderr = c.exec_command(command)
            print(stdout.read())
        c.close()
        user = message.author.name
        response = user + " has initiated a server restart"
        await client.send_message(message.channel, response)
    elif message.content.startswith('!ecostart'):
        k = paramiko.RSAKey.from_private_key_file("/usr/src/app/private.pem")
        c = paramiko.SSHClient()
        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("connecting")
        c.connect(hostname = config.eco_ip, username = config.eco_username, pkey = k)
        print("connected")
        commands = [ "sudo /home/eco/eco_control.sh -o start" ]
        for command in commands:
            print("Executing {0}".format( command ))
            stdin , stdout, stderr = c.exec_command(command)
            print(stdout.read())
        c.close()
        user = message.author.name
        response = user + " has started the server."
        await client.send_message(message.channel, response)
    elif message.content.startswith('!ecostop'):
        k = paramiko.RSAKey.from_private_key_file("/usr/src/app/private.pem")
        c = paramiko.SSHClient()
        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("connecting")
        c.connect(hostname = config.eco_ip, username = config.eco_username, pkey = k)
        print("connected")
        commands = [ "sudo /home/eco/eco_control.sh -o stop" ]
        for command in commands:
            print("Executing {0}".format( command ))
            stdin , stdout, stderr = c.exec_command(command)
            print(stdout.read())
        c.close()
        user = message.author.name
        response = user + " has stopped the server."
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