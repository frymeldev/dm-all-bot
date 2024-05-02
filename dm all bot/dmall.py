import logging
import discord
from discord.ext import commands

def print_red(text):
    print("\033[91m {}\033[00m" .format(text))

intents = discord.Intents.default()
intents.members = True
intents.messages = True  

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print('Bot connecté en tant que', bot.user)

@bot.command()
async def dm_all(ctx, guild_id: int, *, message: str):
    if ctx.guild is None:          
        guild = bot.get_guild(guild_id)
        if guild is not None:
            count = 0
            for member in guild.members:
                try:
                    await member.send(f"{member.mention} {message}")  
                    count += 1
                    print(f"Message envoyé à {member.name}#{member.discriminator}")
                except:
                    print(f"Impossible d'envoyer un message à {member.name}#{member.discriminator}")

            await ctx.send(f"Nombre de membres auxquels le message a été envoyé : {count}")
        else:
            await ctx.send("ID de serveur invalide.")
    else:
        await ctx.send("Cette commande doit être exécutée en messages privés (DM).")

print_red("Créé par Frymel")

token = input("Veuillez entrer le token du bot : ")
bot.run(token)
