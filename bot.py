# fichier de principal du bot 

# importer vos extension, librairie
import discord
from discord.ext import commands, tasks

#determiner le préfixe du bot
bot = commands.Bot(command_prefix = "!", description = "Bot de toto49")

@bot.event
async def on_ready():
  print("le bot est en ligne")














bot.run("votre token")
