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
    msg = deque(filter(None, message.content.lower().strip().split(" ")))
    arg = msg.popleft()
    if arg in ["pc",
               "@Principal PC",
               "@Principal PC,",
              ]:
        arg = msg.popleft()
        if arg in ["ping"]:
            await message.channel.send("Pong!")
        if arg in ["restart",
                   "reboot",
                  ]:
            await message.channel.send("Restarting")
            print("Restarting")
            sys.exit(0)
        else:
            print("PC command found: "+ " ".join([arg]+list(msg)))

client.run(ACCESS_TOKEN)
