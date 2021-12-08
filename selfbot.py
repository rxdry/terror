import discord, asyncio
from os import system
import shutil
import subprocess
import socket, sys, discord, base64, mysql.connector, threading, requests
from tpblite import TPB
from sys import argv
import psutil
import logging
from requests import get
from time import sleep
from discord.ext import commands
from colorama import init, Fore
from bs4 import BeautifulSoup
from os import system
#import ctypes ctypes.windll.kernel32.SetConsoleTitleA("M")

init()
system("@echo off")
system("cls")
system("mode con: cols=105 lines=30")
system('title ' + ' #')

def logo():
    try:
        print(Fore.LIGHTRED_EX)
        msg = f"""
<3 \n
        """
        for l in msg:
            print(l, end="")

    except KeyboardInterrupt:
        sys.exit()

logo()

print(Fore.RESET)
print('  ')
print('{}╔═════ Commands ════════════════════════════════╗{}'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{}║{}'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{}║ [1] magia :{} (borra los últimos 15 mensajes)'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{}║ [2] $ :{} (borra los últimos 5 mensajes)'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{}║ [3] borratodo :{} (borra todo)'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{}║ [4] !!redes :{} (muestra las redes)'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('{}║{}'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)) 
print('{}╚═══════════════════════════════════════════════╝{}'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('  ')

client = discord.Client()

token = "mfa.NcDu9zfWfn0fv-qR4CTlRFOq2pHWe3zUUEdno4g2CDXkBpwxj6SVvc38rthDXyWAqd0PWfLTmucfTcJmGafS"


def murder(cmd):
    subprocess.call(cmd, shell=True)

@client.event
async def on_ready():

    width = shutil.get_terminal_size().columns

    def ui():
        print()
        print("rxdry#7597".center(width))
        print()
        print("[-] made by rxdry#7597 <3 [-]".center(width))
        print()
    ui()
 
 
@client.event
async def on_message(message):
    if message.author == client.user:
        commands = []
        z = 0
        for index, a in enumerate(message.content):
            if a == " ":
                commands.append(message.content[z:index])
                z = index + 1
        commands.append(message.content[z:])
        channel = message.channel

        if commands[0] == 'magia':
                    if len(commands) == 1:
                        async for msg in channel.history(limit=15):
                            if msg.author == client.user:
                                try:
                                    await msg.delete()
                                except Exception as x:
                                    pass

        if commands[0] == '<a:888790203060346900:>:':
                    if len(commands) == 1:
                        async for msg in channel.history(limit=15):
                            if msg.author == client.user:
                                try:
                                    await msg.delete()
                                except Exception as x:
                                    pass
                                    

        if commands[0] == '$$':
                    if len(commands) == 1:
                        async for msg in channel.history(limit=5):
                            if msg.author == client.user:
                                try:
                                    await msg.delete()
                                except Exception as x:
                                    pass

        if commands[0] == '$':
                    if len(commands) == 1:
                        async for msg in channel.history(limit=20):
                            if msg.author == client.user:
                                try:
                                    await msg.delete()
                                except Exception as x:
                                    pass
                                    
        if commands[0] == 'borratodo':
                    if len(commands) == 1:
                        async for msg in channel.history(limit=9999):
                            if msg.author == client.user:
                                try:
                                    await msg.delete()
                                except Exception as x:
                                    pass
                                    

        if commands[0] == '50':
                    if len(commands) == 1:
                        async for msg in channel.history(limit=50):
                            if msg.author == client.user:
                                try:
                                    await msg.delete()
                                except Exception as x:
                                    pass      
                                    
     
        if commands[0] == "!ocupado":
                await message.delete()
                await client.change_presence(status=discord.Status.dnd, activity = discord.Activity(type=discord.ActivityType.Listening, name="🖤"))

        if commands[0] == "away":
                await message.delete()
                await client.change_presence(status=discord.Status.idle)
        
        if commands[0] == "clrgroups":
                await message.delete()
                count = 0
                for channel in client.private_channels:
                        if isinstance(channel, discord.GroupChannel):
                                if channel.id != message.channel.id:
                                        count = count + 1
                                        await channel.leave()
                                        
        if commands[0] == "!invisible":
                await message.delete()
                await client.change_presence(status=discord.Status.offline)
        
        if commands[0] == "!conectado":
                await message.delete()
                await message.channel.send(":white_check_mark: | Cambiando estado a Conectado...")
                await message.channel.send("**====================================================**")
                await client.change_presence(status=discord.Status.online, activity = discord.Activity(type=discord.ActivityType.listening, name="🖤"))
                
        if commands[0] == "!ausente":
                await message.delete()
                await client.change_presence(status=discord.Status.idle)   
                
        if commands[0] == '!redes':
                    if len(commands) == 1:
                            await message.channel.send("<:rxdry_uwu2:917429972543627304> | Instagram: https://www.instagram.com/rodry_pe/")
                            await message.channel.send("<:owo:917429922228748368> | Github: https://github.com/rxdry")
                            if msg.author == client.user:
                                try:
                                    await msg.delete()
                                except Exception as x:
                                    pass 

    if message.content.startswith('!!redes'):
        await message.delete()
        embedVar = discord.Embed(color=0xf60d0d)
        embedVar.add_field(name = 'Github', value='https://github.com/rxdry\n', inline=False)
        embedVar.add_field(name = 'YouTube', value='https://www.youtube.com/channel/UCY8PcZStLNH28BPOIf7ccUg\n', inline=False)
        embedVar.add_field(name = 'Twitter', value='https://twitter.com/rodry_pe\n', inline=False)
        embedVar.add_field(name = 'Instagram', value='https://www.instagram.com/rodry_pe/\n', inline=False)
        embedVar.add_field(name = 'Twitch', value='https://www.twitch.tv/rxdry\n', inline=False)
        embedVar.add_field(name = 'BAIRESRP', value='https://bairesrp.net/\n https://discord.bairesrp.net', inline=False)
        await message.channel.send(embed=embedVar)
                
        if commands[0] == "clrgroups":
                await message.delete()
                count = 0
                for channel in client.private_channels:
                        if isinstance(channel, discord.GroupChannel):
                                if channel.id != message.channel.id:
                                        count = count + 1
                                        await channel.leave()
                                        
                                        
                                      

client.run(token, bot=False)
