#! /bin/python3
import discord
from pathlib import Path
import sys

path = './'
if "/" in __file__:
    path = path + '/'.join(__file__.split('/')[:-1]) + '/'
print("Running from " + path)

if not Path(path+"token").is_file():
    print("'token' file not found.\nPlease create a file named 'token' in which your access token is written on the first line")
    sys.exit(-1)
with open("./token", "r") as tokenFile:
    ACCESS_TOKEN = tokenFile.readline().strip()
    print("Starting server")

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.find("Pong") != -1:
        await message.channel.send("ping")
    if message.content == "PC exit" :
        await message.channel.send("Exiting")

client.run(ACCESS_TOKEN)
