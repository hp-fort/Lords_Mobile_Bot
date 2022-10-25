from turtle import color, title
from discord.ext import commands
from discord_slash import *
from discord_slash.utils.manage_commands import *
from discord_slash.utils.manage_components import *
import time

bot = commands.Bot(command_prefix="!",
                   description="Bot lords mobile")
slash = SlashCommand(bot, sync_commands = True)

@bot.event
async def on_ready():
    print("Lords Mobile Bot is connect in the server !")
    Dis = bot.get_guild(int(974566955132526673))
    activity = discord.Activity(type=discord.ActivityType.watching, name=f'👥 {Dis.member_count}')
    await bot.change_presence(activity=activity)


@slash.slash(name="batiment_payant", description="Permet d'obtenir des information a propos de vos batiment payant", guild_ids=[930527744306061333, 974566955132526673], options=[
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
    nb_menote_manquant=0
    nb_cristal_manquant=0
    nb_gemmes_grimoire_manquant=0
    nb_gemmes_menote_manquant=0
    nb_gemmes_cristal_manquant=0
    for i in range(26):
        if i == hall or i > hall:
            nb_grimoire_manquant+=lv[i]
            nb_gemmes_grimoire_manquant_base=nb_grimoire_manquant-grimoire
    for i in range(26):
        if i == prison or i > prison:
            nb_menote_manquant+=lv[i]
            nb_gemmes_menote_manquant_base=nb_menote_manquant-menote
    for i in range(26):
        if i == autel or i > autel:
            nb_cristal_manquant+=lv[i]
            nb_gemmes_cristal_manquant_base=nb_cristal_manquant-cristal

    while nb_gemmes_grimoire_manquant_base!=0:
        if (nb_gemmes_grimoire_manquant_base-1000)>=0:
            nb_gemmes_grimoire_manquant +=10000
            nb_gemmes_grimoire_manquant_base-=1000
        elif (nb_gemmes_grimoire_manquant_base-100)>=0:
            nb_gemmes_grimoire_manquant +=1100
            nb_gemmes_grimoire_manquant_base-=100
        elif (nb_gemmes_grimoire_manquant_base-10)>=0:
            nb_gemmes_grimoire_manquant +=120
            nb_gemmes_grimoire_manquant_base-=10
        elif (nb_gemmes_grimoire_manquant_base-1)>=0:
            nb_gemmes_grimoire_manquant +=15
            nb_gemmes_grimoire_manquant_base-=1

    while nb_gemmes_menote_manquant_base!=0:
        if (nb_gemmes_menote_manquant_base-1000)>=0:
            nb_gemmes_menote_manquant +=10000
            nb_gemmes_menote_manquant_base-=1000
        elif (nb_gemmes_menote_manquant_base-100)>=0:
            nb_gemmes_menote_manquant +=1100
            nb_gemmes_menote_manquant_base-=100
        elif (nb_gemmes_menote_manquant_base-10)>=0:
            nb_gemmes_menote_manquant +=120
            nb_gemmes_menote_manquant_base-=10
        elif (nb_gemmes_menote_manquant_base-1)>=0:
            nb_gemmes_menote_manquant +=15
            nb_gemmes_menote_manquant_base-=1

    while nb_gemmes_cristal_manquant_base!=0:
        if (nb_gemmes_cristal_manquant_base-1000)>=0:
            nb_gemmes_cristal_manquant +=10000
            nb_gemmes_cristal_manquant_base-=1000
        elif (nb_gemmes_cristal_manquant_base-100)>=0:
            nb_gemmes_cristal_manquant +=1100
            nb_gemmes_cristal_manquant_base-=100
        elif (nb_gemmes_cristal_manquant_base-10)>=0:
            nb_gemmes_cristal_manquant +=120
            nb_gemmes_cristal_manquant_base-=10
        elif (nb_gemmes_cristal_manquant_base-1)>=0:
            nb_gemmes_cristal_manquant +=15
            nb_gemmes_cristal_manquant_base-=1
    
    BotEmbed = discord.Embed(title="batiment payant", description = "", color=0x9c19fb)
    BotEmbed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    BotEmbed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1025391983503614073/1034598369491943595/unknown.png")
    BotEmbed.add_field(name="grimoire manquant", value=f"{nb_grimoire_manquant - grimoire} grimoire", inline=True)
    BotEmbed.add_field(name="menote manquante", value=f"{nb_menote_manquant - menote} menote", inline=True)
    BotEmbed.add_field(name="cristal manquant", value=f"{nb_cristal_manquant - cristal} cristal", inline=True)
    BotEmbed.add_field(name="gemmes des grimoires manquants", value=f"{nb_gemmes_grimoire_manquant} gemmes", inline=True)
    BotEmbed.add_field(name="gemmes des menotes manquantes", value=f"{nb_gemmes_menote_manquant} gemmes", inline=True)
    BotEmbed.add_field(name="gemmes des cristal manquant", value=f"{nb_gemmes_cristal_manquant} gemmes", inline=True)
    BotEmbed.add_field(name="grimoire manquant", value=f"{nb_gemmes_grimoire_manquant + nb_gemmes_cristal_manquant + nb_gemmes_menote_manquant} gemmes", inline=True)
    BotEmbed.add_field(name="grimoire manquant", value=f"{(nb_gemmes_grimoire_manquant + nb_gemmes_cristal_manquant + nb_gemmes_menote_manquant) - gemmes} gemmes", inline=True)

    message = await ctx.send(embed=BotEmbed)
    time.sleep(120)
    await message.delete()


with open("config", "r", encoding="utf-8") as f:
    bot_id = f.read()

bot.run(bot_id)