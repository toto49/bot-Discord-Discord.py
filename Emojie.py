@bot.command()
#Définir si c'est une commande, un event ou autre chose
async def github(ctx):
# définir le nom de la commande eet des requêtes ()
    message =await ctx.send("bonjour")
    # definir le bonjour pour ajouter une reaction
    await message.add_reaction("<a:valid:794520750802731020>")
    # envoie une reaction en dessous du message
    
