import discord
import random
import string
import asyncio
import datetime
import requests
import os
import json
import pyfiglet
from random import randrange
from termcolor import colored
from colorama import Fore

from discord.ext import (
    commands,
    tasks
)

client = discord.Client()
client = commands.Bot(
    command_prefix="!",
    self_bot=True
)
client.remove_command('help')

with open('config.json') as f:
    config = json.load(f)
    
token = config.get("token")

def scale(time):
    defined = 60
    for unit in ["m", "h"]:
        if time < defined:
            return f"{time:.2f}{unit}"
        time /= defined

def Init():
    if config.get('token') == "token-here":
        os.system('cls')
        print(f"\n\n{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}You didnt put your token in the config.json file\n\n"+Fore.RESET)
        exit()
    else:
        token = config.get('token')
        try:
            client.run(token, reconnect=True)
            os.system(f'Discord LevelUpBot')
        except discord.errors.LoginFailure:
        
            print(f"\n\n{Fore.WHITE}[ {Fore.RED}Erorr {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Token is invalid\n\n " +Fore.RESET)
            exit()

def rnd1(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))
def rnd2(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

os.system('cls')
result = pyfiglet.figlet_format("""Discord Tools""", font = "graceful"  )
print (colored(result, 'blue'))
ip = requests.get('https://api.ipify.org').text
x = datetime.datetime.now()
print (colored('''Created by: YSA DEV - YSA DEV - YSA DEV - YSA DEV - YSA DEV''', 'cyan', attrs=['bold'])) 
print (colored('•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••', 'green', attrs=['bold']))
print (colored(f"Ξ Follow myGithub : https://github.com/yudhasaputra \nΞ START           : {x} \nΞ Your IP         : {ip} ", 'green', attrs=['bold']))
print (colored('••••••••••••••••••••••••••••••••••••••••••••••••••••••••••• \n', 'green', attrs=['bold']))
print (colored('+===================== BOT START! ========================+', 'red', attrs=['bold']))
print (colored('Write ON DISCORD: \n!levelup <number of messages> to Start Level UP', 'cyan', attrs=['bold']))


@client.command()
async def levelup(ctx, amount: int, delay: int):
    await ctx.message.delete()
    msgsend = amount
    setdelay = delay
    
    print(f"\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Sending {Fore.WHITE}{msgsend} {Fore.LIGHTBLACK_EX}messages\n{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Estimated Time: {Fore.WHITE}{scale(msgsend)}\n")
    await asyncio.sleep(setdelay)
    while msgsend > 0:
        try:
            msgsend -= 1
            print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Terkirim! | Messages left to send: {Fore.WHITE}{msgsend} {Fore.LIGHTBLACK_EX}|Estimated Time: {Fore.WHITE}{scale(msgsend)}")
            if msgsend == 0:
                print(f"\n{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}All messages was sent ")
            output = rnd1(5) + " " + rnd2(5) + "-" + rnd2(5) + " " + rnd2(5) + "-" + rnd2(5) + " " + rnd1(5)
            message = config.get("pesan")
            acak = randrange(len(message))
            kirim = message[acak]
            await ctx.send(kirim)
            print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Terkirim! | Messages : {Fore.WHITE}{kirim} {Fore.LIGHTBLACK_EX}|Estimated Time: {Fore.WHITE}{scale(msgsend)}")
        except:
            print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Gagal Mengirim Pesan {Fore.WHITE}#{msgsend}")
            pass
            await ctx.message.delete()
            await asyncio.sleep(1)
       
        async for message in ctx.message.channel.history(limit=1):
            try:
                await message.delete()
                print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Berhasil Di Hapus {Fore.WHITE}#{msgsend}")
            except:
                
                print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Pesan Gagal Di Hapus {Fore.WHITE}#{msgsend}")
              # await message.delete()
                pass

        await asyncio.sleep(setdelay) #setdelayhere(s)
    return


@client.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Discord error: {error}"+Fore.RESET)    
    else:
        print(f"{Fore.WHITE}[ {Fore.RED}Error 2 {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Discord error: {error_str} "+Fore.RESET)
        print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
pass
#os.system('kill 1')

Init()