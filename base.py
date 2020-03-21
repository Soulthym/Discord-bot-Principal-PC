#! /usr/bin/python3
import discord
from pathlib import Path
import sys
from collections import deque

def getPath():
    if '/' in __file__:
        return './' + '/'.join(__file__.split('/')[:-1]) + '/'
    return './'

def getToken(tokenPath):
    if not Path(tokenPath).is_file():
        print("'token' file not found.\nPlease create a file named 'token' in which your access token is written on the first line")
        sys.exit(-1)
    with open(tokenPath, "r") as tokenFile:
        return tokenFile.readline().strip()

def splitargs(args=[]):
    assert "__getitem__" in dir(args), "args should be a list (or implement the __getitem__ method)"
    if len(args) == 0:
        return None,[]
    return args[0], args[1:]

def parse(args, path):
    arg, args = splitargs(args)
    if arg == None:
        return "Found '"+str(path)+"' path"
    path = path/arg
    if path.exists():
        return parse(args, path)
    else:
        pass
        return "ERROR: Path '"+str(path)+"' does not exist"

path = getPath()
print('Running from ' + path)
tokenPath = path + 'token'
ACCESS_TOKEN = getToken(tokenPath)
print("Starting server")

client = discord.Client()

@client.event
async def on_message(message):
    msg = message.content.lower().strip()
    if msg.startswith("pc"):
        msg = [arg.strip()
               for arg in filter(None, msg.split(" "))]
        output = parse(msg, Path(path))
        await message.channel.send(output)

client.run(ACCESS_TOKEN)
