#! /usr/bin/python3
from discord.ext import commands
import discord
from pathlib import Path
import sys
from parser import *
from pprint import pprint

def getPath():
    if '/' in __file__:
        return './' + '/'.join(__file__.split('/')[:-1]) + '/'
    return './'

def getToken(tokenPath):
    if not Path(tokenPath).is_file():
        print('\'token\' file not found.\nPlease create a file named \'token\' in which your access token is written on the first line')
        sys.exit(-1)
    with open(tokenPath, 'r') as tokenFile:
        return tokenFile.readline().strip()

path = getPath()
print('Running from ' + path)
tokenPath = path + 'token'
ACCESS_TOKEN = getToken(tokenPath)
print('Starting server')

class PCBot(discord.Client):
    memory_channel_name = 'bot-pc-memory'

    async def getCommand(self, msg):
        cmd = msg.content.lower().strip()
        if cmd.startswith('pc '):
            print('='*10)
            if client.user.id != msg.author.id:
                id_list = list(map(lambda c: c.id, filter(lambda c: c.name == self.memory_channel_name,
                                           msg.guild.channels)))
                print(id_list)
                memory_channel_id = id_list[0] if len(id_list) > 0 else None
                if memory_channel_id is None:
                    guild = msg.guild
                    await msg.channel.send('Memory not Found\nCreating new channel to store pc\'s internal memory state')
                    await msg.guild.create_text_channel(
                            name=self.memory_channel_name,
                            overwrites={
                                        guild.default_role: discord.PermissionOverwrite(read_messages=False),
                                        guild.me: discord.PermissionOverwrite(read_messages=True)
                                       },
                            reason=f'{client.user.name}\'s memory channel',
                            )
                    await msg.channel.send(f'Created text channel: #{self.memory_channel_name}')
                else:
                    async for m in msg.guild.get_channel(memory_channel_id).history(limit=100, oldest_first=True):
                        cell = m.content.lower().strip()
                        if m.id != msg.id and not cell.startswith('$') :
                            print(f'Invalid text: {cell}')
                            await m.delete()
                    memory_messages = [m.content.strip().lower() 
                                       async for m in msg.guild.get_channel(memory_channel_id).history(limit=100,
                                                                                                       oldest_first=True)
                                         if m.id != msg.id]
                    state = {k:v 
                             for m in memory_messages
                             for k,v in zip(m.split(' '), m.split(' ')[1:]) #TODO add support for groupped units and repeated symbols
                            }
            await msg.add_reaction('🔆')
            return state, cmd

    async def on_message(self, msg):
        state, cmd = await self.getCommand(msg)
        print(f'{cmd=}')
        print(f'state :')
        pprint(state)

client = PCBot()
client.run(ACCESS_TOKEN)
