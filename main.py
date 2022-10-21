from discord.ext import commands, tasks
from discord_slash import *
from discord_slash.utils.manage_commands import *
from discord_slash.utils.manage_components import *

bot = commands.Bot(command_prefix="!",
                   description="Bot lords mobile")
slash = SlashCommand(bot, sync_commands = True)

@bot.event
async def on_ready():
    print("Lords Mobile Bot is connect in the server !")
    # Dis = bot.get_guild(int(930527744306061333))
    # activity = discord.Activity(type=discord.ActivityType.watching, name=f'👥 {Dis.member_count}')
    # await bot.change_presence(activity=activity)

@slash.slash(name = "batiment_payant", description = "Permet d'obtenir des information a propos de vos batiment payant", guild_ids=[930527744306061333], options=[
# 974566955132526673 -> id FA serv
    create_option(
        name = "gemmes",
        description = "combien de gemmes avez vous ?",
        option_type = 4, 
        required = True),
    create_option(
        name = "hall",
        description = "quel est le niveau de votre hall ?",
        option_type = 4, 
        required = True),
    create_option(
        name = "prison",
        description = "quel est le niveau de votre prison ?",
        option_type = 4, 
        required = True),
    create_option(
        name = "autel",
        description = "quel est le niveau de votre autel ?",
        option_type = 4, 
        required = True),
    create_option(
        name = "grimoire",
        description = "combien de grimoire de guerre avez vous ?",
        option_type = 4, 
        required = True),
    create_option(
        name = "menote",
        description = "combien de Menotes en acier avez vous ?",
        option_type = 4, 
        required = True),
    create_option(
        name = "cristal",
        description = "combien de Cristal d'ame avez vous ?",
        option_type = 4, 
        required = True),
    create_option(
        name = "pioche",
        description = "combien de Pioche pour la salle au tresor avez vous ?",
        option_type = 4, 
        required = True),
    create_option(
        name = "depot",
        description = "combien de gemmes pouvez vous mettre d'un seul coup a la salle au tresor ?",
        option_type = 4, 
        required = True),
    create_option(
        name = "rendement",
        description = "quel est le pourcentage de rendement ?",
        option_type = 4, 
        required = True)
    ])

async def bat_payant(ctx, gemmes, hall, prison, autel, grimoire, menote, cristal, pioche, depot, rendement):
    lv = [1, 2, 5, 12, 20, 30, 45, 60, 85, 100, 120, 150, 180, 250, 340, 500, 700, 900, 1200, 1500, 1800, 2100, 2400, 3000, 4500, 0]
    nb_grimoire_manquant=0
    nb_prison_manquant=0
    nb_autel_manquant=0
    for i in range(26):
        if i == hall or i > hall:
            nb_grimoire_manquant+=lv[i]
    for i in range(26):
        if i == prison or i > prison:
            nb_prison_manquant+=lv[i]
    for i in range(26):
        if i == autel or i > autel:
            nb_autel_manquant+=lv[i]

















    await ctx.send(nb_grimoire_manquant)
    await ctx.send(nb_prison_manquant)
    await ctx.send(nb_autel_manquant)
    




bot.run("OTMyNTcyODE3MzkwNzE0OTIx.Gtz0Gn.NYT_g1Miy5xyTMKnR2cUghEIVp0m4OvVlPHKl0")