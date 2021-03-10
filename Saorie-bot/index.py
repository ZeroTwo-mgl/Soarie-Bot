import discord, json, pyfiglet
from colorsys import * 
from discord.ext import commands
from colorama import Back, Fore, Style, deinit, init
from termcolor import colored
import random
import pyautogui
import sys
import time
import win32api, win32com







# AFFICHAGE DU DESSUS


bot = commands.Bot(description="Selbot by LeDeuxièmeZeroTwo#2916", command_prefix="$", self_bot=True)
bot.remove_command('help')
init(convert=True)
print(Fore.RED + Style.NORMAL + """

                       ___           ___           ___           ___                       ___              
                      /  /\         /  /\         /  /\         /  /\        ___          /  /\             
                     /  /:/_       /  /::\       /  /::\       /  /::\      /  /\        /  /:/_            
                    /  /:/ /\     /  /:/\:\     /  /:/\:\     /  /:/\:\    /  /:/       /  /:/ /\           
                   /  /:/ /::\   /  /:/~/::\   /  /:/  \:\   /  /:/~/:/   /__/::\      /  /:/ /:/_          
                  /__/:/ /:/\:\ /__/:/ /:/\:\ /__/:/ \__\:\ /__/:/ /:/___ \__\/\:\__  /__/:/ /:/ /\         
                  \  \:\/:/~/:/ \  \:\/:/__\/ \  \:\ /  /:/ \  \:\/:::::/    \  \:\/\ \  \:\/:/ /:/         
                   \  \::/ /:/   \  \::/       \  \:\  /:/   \  \::/~~~~      \__\::/  \  \::/ /:/          
                    \__\/ /:/     \  \:\        \  \:\/:/     \  \:\          /__/:/    \  \:\/:/           
                      /__/:/       \  \:\        \  \::/       \  \:\         \__\/      \  \::/            
                      \__\/         \__\/         \__\/         \__\/                     \__\/             


""")



print(Fore.YELLOW +  '════════════════════════════════════════════════════CONSOLE═══════════════════════════════════════════════════════════')
deinit()
init(convert=True)

    
# commande ascii

deinit()
init(convert=True)

@bot.command()
async def ascii(ctx, *, args):
    await ctx.message.delete()
    text = pyfiglet.figlet_format(args)
    await ctx.send(f'```{text}```')
    print('Vous avez fais la commande $ascii')


    

# AFFICHAGE  DU DESSOUS


affichage = """
╔═════════╗
| Help ?  |
╚═════════╝
╔══════════════════════════════════╗
|ce bot est en développement !     |
╚══════════════════════════════════╝
╔══════════════════════════════════╗╔════════════════════════════════════════════════════════════════════════════════════╗
| le prefix est "$"                ||Si le $spam +msg + number continue après le nombre donner veuillez fermer cete page |
╚══════════════════════════════════╝╚════════════════════════════════════════════════════════════════════════════════════╝
"""
print(affichage)
deinit()
print('════════════════════════════════════════════AFFICHAGE DES COMMANDES═════════════════════════════════════════════════════')


spam_txt = False







# COMMANDE BOTE 

spam_txt = False

@bot.command()
async def spam(ctx, msg): # exemple : $spam coucou
    print("Vous avez fais la commande $spam")
    spam_txt = True
    if spam_txt == True:
        while True:
            await ctx.channel.send(msg)


@bot.command()
async def stop(ctx):
    spam_txt = False
    await ctx.channel.send("[!] - Spam stoppé !")
    print("Vous avez fais la commande $stop")











            
            


with open('./config.json') as f:
    config = json.load(f)
    
token = config.get('token')
bot.run(token, bot=False)
