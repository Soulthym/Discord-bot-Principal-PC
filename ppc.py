#! /usr/bin/python3
import discord
from pathlib import Path
import sys
from collections import deque

path = './'
if "/" in __file__:
    path = path + '/'.join(__file__.split('/')[:-1]) + '/'
print("Running from " + path)
tokenPath = path+'token'

if not Path(tokenPath).is_file():
    print("'token' file not found.\nPlease create a file named 'token' in which your access token is written on the first line")
    sys.exit(-1)
with open(tokenPath, "r") as tokenFile:
    ACCESS_TOKEN = tokenFile.readline().strip()
    print("Starting server")

client = discord.Client()

@client.event
async def on_message(message):
    msg = deque([arg.strip() for arg in filter(None, message.content.lower().strip().split(" "))])
    if len(msg) == 0:
        return
    print(msg)
    arg = msg.popleft()
    if arg in ["pc",
               "<@!690624786333958185>",
               "<@!690624786333958185>,"]:
        if len(msg) == 0:
            return
        arg = msg.popleft()
        if arg in ["ping"]:
            await message.channel.send("Pong!")
        elif arg in ["stop",
                     "exit",
                     "restart",
                     "ta gueule putain",
                     "reboot"]:
            await message.channel.send("Restarting")
            print("Restarting")
            sys.exit(0)
        elif arg == "help":
            embed = discord.Embed(title="PC Help", description="Help for the Principal-PC Bot")
            embed.add_field(name="ping", value='Replies "Pong!"')
            embed.add_field(name="restart|reboot|stop|exit", value="Restarts Principal-PC Bot")
            await message.channel.send(content=None, embed=embed)
        else:
            print("PC command found: "+ " ".join([arg]+list(msg)))

client.run(ACCESS_TOKEN)
