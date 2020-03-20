#! /bin/python3
import discord
from pathlib import Path
import sys

if not Path("./token").is_file():
    print("'token' file not found.\nPlease create a file named 'token' in which your access token is written on the first line")
    sys.exit(-1)
with open("./token", "r") as tokenFile:
    ACCESS_TOKEN = tokenFile.readline().strip()
    print("Starting server")

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.find("Pong") != -1:
        await message.channel.send("ping") # If the user says !hello we will send 

client.run(TOKEN)
