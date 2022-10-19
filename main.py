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
    Dis = bot.get_guild(int(930527744306061333))
    activity = discord.Activity(type=discord.ActivityType.watching, name=f'👥 {Dis.member_count}')
    await bot.change_presence(activity=activity)

@slash.slash(name = "batiment_payant", description = "Permet d'obtenir des information a propos de vos batiment payant", guild_ids=[930527744306061333, 974566955132526673], options=[
    create_option(
        name = "nombre de gemmes",
        description = "combien de gemmes avez vous ?",
        option_type = 4, 
        required = True),
    create_option(
        name = "niveau du hall",
        description = "quel est le niveau de votre hall ?",
        option_type = 4, 
        required = True,
        choices=[
            create_choice(
                name="0",
                value=0
            ),
            create_choice(
                name="1",
                value=1
            ),
            create_choice(
                name="2",
                value=2
            ),
            create_choice(
                name="3",
                value=3
            ),
            create_choice(
                name="4",
                value=4
            ),
            create_choice(
                name="5",
                value=5
            ),
            create_choice(
                name="6",
                value=6
            ),
            create_choice(
                name="7",
                value=7
            ),
            create_choice(
                name="8",
                value=8
            ),
            create_choice(
                name="9",
                value=9
            ),
            create_choice(
                name="10",
                value=10
            ),
            create_choice(
                name="11",
                value=11
            ),
            create_choice(
                name="12",
                value=12
            ),
            create_choice(
                name="13",
                value=13
            ),
            create_choice(
                name="14",
                value=14
            ),
            create_choice(
                name="15",
                value=15
            ),
            create_choice(
                name="16",
                value=16
            ),
            create_choice(
                name="17",
                value=17
            ),
            create_choice(
                name="18",
                value=18
            ),
            create_choice(
                name="19",
                value=19
            ),
            create_choice(
                name="20",
                value=20
            ),
            create_choice(
                name="21",
                value=21
            ),
            create_choice(
                name="22",
                value=22
            ),
            create_choice(
                name="23",
                value=23
            ),
            create_choice(
                name="24",
                value=24
            ),
            create_choice(
                name="25",
                value=25
            )]),
    create_option(
        name = "niveau de la prison",
        description = "quel est le niveau de votre prison ?",
        option_type = 4, 
        required = True,
        choices=[
            create_choice(
                name="0",
                value=0
            ),
            create_choice(
                name="1",
                value=1
            ),
            create_choice(
                name="2",
                value=2
            ),
            create_choice(
                name="3",
                value=3
            ),
            create_choice(
                name="4",
                value=4
            ),
            create_choice(
                name="5",
                value=5
            ),
            create_choice(
                name="6",
                value=6
            ),
            create_choice(
                name="7",
                value=7
            ),
            create_choice(
                name="8",
                value=8
            ),
            create_choice(
                name="9",
                value=9
            ),
            create_choice(
                name="10",
                value=10
            ),
            create_choice(
                name="11",
                value=11
            ),
            create_choice(
                name="12",
                value=12
            ),
            create_choice(
                name="13",
                value=13
            ),
            create_choice(
                name="14",
                value=14
            ),
            create_choice(
                name="15",
                value=15
            ),
            create_choice(
                name="16",
                value=16
            ),
            create_choice(
                name="17",
                value=17
            ),
            create_choice(
                name="18",
                value=18
            ),
            create_choice(
                name="19",
                value=19
            ),
            create_choice(
                name="20",
                value=20
            ),
            create_choice(
                name="21",
                value=21
            ),
            create_choice(
                name="22",
                value=22
            ),
            create_choice(
                name="23",
                value=23
            ),
            create_choice(
                name="24",
                value=24
            ),
            create_choice(
                name="25",
                value=25
            )]),
    create_option(
        name = "niveau de l'autel",
        description = "quel est le niveau de votre autel ?",
        option_type = 4, 
        required = True,
        choices=[
            create_choice(
                name="0",
                value=0
            ),
            create_choice(
                name="1",
                value=1
            ),
            create_choice(
                name="2",
                value=2
            ),
            create_choice(
                name="3",
                value=3
            ),
            create_choice(
                name="4",
                value=4
            ),
            create_choice(
                name="5",
                value=5
            ),
            create_choice(
                name="6",
                value=6
            ),
            create_choice(
                name="7",
                value=7
            ),
            create_choice(
                name="8",
                value=8
            ),
            create_choice(
                name="9",
                value=9
            ),
            create_choice(
                name="10",
                value=10
            ),
            create_choice(
                name="11",
                value=11
            ),
            create_choice(
                name="12",
                value=12
            ),
            create_choice(
                name="13",
                value=13
            ),
            create_choice(
                name="14",
                value=14
            ),
            create_choice(
                name="15",
                value=15
            ),
            create_choice(
                name="16",
                value=16
            ),
            create_choice(
                name="17",
                value=17
            ),
            create_choice(
                name="18",
                value=18
            ),
            create_choice(
                name="19",
                value=19
            ),
            create_choice(
                name="20",
                value=20
            ),
            create_choice(
                name="21",
                value=21
            ),
            create_choice(
                name="22",
                value=22
            ),
            create_choice(
                name="23",
                value=23
            ),
            create_choice(
                name="24",
                value=24
            ),
            create_choice(
                name="25",
                value=25
            )]),
    create_option(
        name = "nombre de grimoire de guerre",
        description = "combien de grimoire de guerre avez vous ?",
        option_type = 4, 
        required = True),
    create_option(
        name = "nombre de Menotes en acier",
        description = "combien de Menotes en acier avez vous ?",
        option_type = 4, 
        required = True),
    create_option(
        name = "nombre de Cristal d'ame",
        description = "combien de Cristal d'ame avez vous ?",
        option_type = 4, 
        required = True),
    create_option(
        name = "nombre de Pioche",
        description = "combien de Pioche pour la salle au tresor avez vous ?",
        option_type = 4, 
        required = True),
    create_option(
        name = "Depot max",
        description = "combien de gemmes pouvez vous mettre d'un seul coup a la salle au tresor ?",
        option_type = 4, 
        required = True),
    create_option(
        name = "Rendement max (en %)",
        description = "quel est le pourcentage de rendement ?",
        option_type = 4, 
        required = True)
    ])

async def mp(ctx, membre: discord.Member, message):
        await membre.send(message)



bot.run("OTMyNTcyODE3MzkwNzE0OTIx.Gtz0Gn.NYT_g1Miy5xyTMKnR2cUghEIVp0m4OvVlPHKl0")