@bot.command()
#Définir si c'est une commande, un event ou autre chose
async def github(ctx):
# définir le nom de la commande eet des requêtes ()
    await ctx.send("bonjour")
    #envoie bonjour
    embed = discord.Embed(title = " github ", description = " je m appelle github et je suis un site internet ")
    # genere un embed avec un titre et une description
    embed.add_field(name = "github", value = "au revoir")
    # ajoute un sous titre et une description
    await ctx.send(embed = embed)
    # envoie l'embed
