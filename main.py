import asyncio as ay
import discord
from discord.ext import commands
from discord.app_commands import Choice
from database_handler import DatabaseHandler


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents().all())

    async def setup_hook(self):
            await Bot.tree.sync()

    async def on_ready(self):
        print("Lords Mobile Bot is connect in the server !")
        Dis = Bot.get_guild(int(974566955132526673))
        activity = discord.Activity(type=discord.ActivityType.watching, name=f'👥 {(Dis.member_count)-9}')
        await Bot.change_presence(activity=activity)
database_handler = DatabaseHandler("Lords_Mobile_Bot.db")

    
Bot = MyBot()

@Bot.tree.command(name="batiment_payant", description="Permet d'obtenir des information a propos de vos batiments payants")
async def self(interaction: discord.Interaction, gemmes:int, hall:int, prison:int, autel:int, grimoire:int, menotes:int, cristal:int):
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
            nb_gemmes_menote_manquant_base=nb_menote_manquant-menotes
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
    print(interaction)
    BotEmbed = discord.Embed(title="batiment payant", description = "", color=0x9c19fb)
    BotEmbed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar.url)
    BotEmbed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1025391983503614073/1034598369491943595/unknown.png")
    BotEmbed.add_field(name="grimoire manquant", value=f"{nb_grimoire_manquant - grimoire} grimoire", inline=True)
    BotEmbed.add_field(name="menote manquante", value=f"{nb_menote_manquant - menotes} menote", inline=True)
    BotEmbed.add_field(name="cristal manquant", value=f"{nb_cristal_manquant - cristal} cristal", inline=True)
    BotEmbed.add_field(name="gemmes des grimoires manquants", value=f"{nb_gemmes_grimoire_manquant} gemmes", inline=True)
    BotEmbed.add_field(name="gemmes des menotes manquantes", value=f"{nb_gemmes_menote_manquant} gemmes", inline=True)
    BotEmbed.add_field(name="gemmes des cristal manquant", value=f"{nb_gemmes_cristal_manquant} gemmes", inline=True)
    BotEmbed.add_field(name="total", value=f"{nb_gemmes_grimoire_manquant + nb_gemmes_cristal_manquant + nb_gemmes_menote_manquant} gemmes", inline=True)
    BotEmbed.add_field(name="total - vos gemmes", value=f"{(nb_gemmes_grimoire_manquant + nb_gemmes_cristal_manquant + nb_gemmes_menote_manquant) - gemmes} gemmes", inline=True)

    await interaction.response.send_message(embed=BotEmbed)
    await ay.sleep(120)
    await interaction.delete_original_response()


@Bot.tree.command(name="speed_up", description="Calcule vos accelerations")
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(".")
    await interaction.delete_original_response()
    def check(message):
        return message.author == interaction.user and interaction.channel == message.channel
    nb_min = [1, 3, 5, 10, 15, 30, 60, 180, 480, 900, 1440, 4320, 10080, 43200]
    min = 0
    for i in nb_min:
        if i == 1:
            temps = "1 minute"
        elif i == 3:
            temps = "3 minutes"
        elif i == 5:
            temps = "5 minutes"
        elif i == 10:
            temps = "10 minutes"
        elif i == 15:
            temps = "15 minutes"
        elif i == 30:
            temps = "30 minutes"
        elif i == 60:
            temps = "1 heure"
        elif i == 180:
            temps = "3 heures"
        elif i == 480:
            temps = "8 heures"
        elif i == 900:
            temps = "15 heures"
        elif i == 1440:
            temps = "1 jour"
        elif i == 4320:
            temps = "3 jours"
        elif i == 10080:
            temps = "7 jours"
        elif i == 43200:
            temps = "30 jours"

        embed = discord.Embed(title="Speed up", description=f"Combien d'acceleration de {temps} as tu ?")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/938452030442323968/1035271662737821737/unknown.png")
        embed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar.url)
        await interaction.channel.send(embed=embed)
        min_waited = await Bot.wait_for("message", timeout=60, check=check)
        await interaction.channel.purge(limit=2)
        min_waited = int(min_waited.content)
        min_waited *= int(i)
        min += min_waited

    def truncate_day(day, n):
        integer_day = int(day * (10**n))/(10**n)
        return int(integer_day)

    day = truncate_day(min/1440, 0)

    def truncate_hour(day, n):
        integer_hour = int(day * (10**n))/(10**n)
        return int(integer_hour)

    min = min - day*1440

    hour = truncate_hour(min/60, 0)

    min = min - hour*60
    if day > 1: days = "s"
    else: days = ""
    if min > 1: mins = "s"
    else: mins = ""
    if hour > 1: hours = "s"
    else: hours = ""
    embed_result = discord.Embed(title="**__Speed Up__**", description=f"Vous pouvez accelerer pendant {day} jour{days}, {hour} heure{hours} et {min} minute{mins}.")
    embed_result.set_thumbnail(url="https://cdn.discordapp.com/attachments/938452030442323968/1035271662737821737/unknown.png")
    embed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar.url)
    message = await interaction.channel.send(embed=embed_result)
    await ay.sleep(120)
    await interaction.channel.purge(limit=1)


@Bot.tree.command(name="shield_spam")
async def self(interaction: discord.Interaction, membre:discord.Member):
    channel = Bot.get_channel(977911012739153990)
    if interaction.channel != channel:
        await interaction.response.send_message("you are in the bad channel")
    else:
        for i in range(10):
            if i == 0:
                await interaction.response.send_message(f"<@{membre.id}> put your shield")
            else:
                
                await channel.send(f"<@{membre.id}> put your shield")
            
            await ay.sleep(2)



# Admin


@Bot.tree.command(name="guild_fest")
@discord.app_commands.checks.has_role(976818687455674381)
@discord.app_commands.choices(success=[
    Choice(name="yes", value=1), 
    Choice(name="no", value=0),
    ])

async def self(interaction: discord.Interaction, membre:discord.Member, success:int):
    player_find = False
    id_member = membre.id
    rep = database_handler.search_member()
    message = "erreur dans le code"
    for id in rep:
        if id["member_id"] == id_member:
            old_gf = database_handler.take_old_result(id_member)
            for list in old_gf:
                last_gf = list["guild_fest_success"]
                database_handler.update_new_gf(id_member, success)
                if last_gf == 0 and success == 0:
                    message = "The member already exists, during the last gf, he failed to finish his points. He didn't make it either."
                elif last_gf == 0 and success == 1:
                    message = "The member already exists, during the last gf, he failed to finish his points. He succeeded this time."
                elif last_gf == 1 and success == 0:
                    message = "The member already exists, during the last gf, he managed to finish his points. He didn't make it this time."
                elif last_gf == 1 and success == 1:
                    message = "The member already exists, during the last gf, he managed to finish his points. He succeeded this time. He's a good player."
                player_find = True

    if player_find == False:
        database_handler.add_member(id_member, success)
        if success == 0:
            message = "The member has been added to the list, he did not pass his guild fest"
        else:
            message = "The member has been added to the list, he has successfully completed his guild fest"
    
    
    await interaction.response.send_message(message, ephemeral=True)


with open("config", "r", encoding="utf-8") as f:
    bot_id = f.read()

Bot.run(bot_id)