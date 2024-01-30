import os
import discord
from discord import app_commands
from discord.ext import commands
import requests
from Token import token

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    synced = await bot.tree.sync()


@bot.tree.command(name='paldeck-entry')
async def paldeckinfo(ctx: discord.Interaction, palname: str):
    endpoint_url = f'http://127.0.0.1:8000/Pal={palname}'
    response = requests.get(endpoint_url)
    if response.status_code == 200:
        json_data = response.json()
        paldeck = json_data.get('Paldeck')
        paldeckEntry = paldeck.get('PaldeckEntry')
        print(f"Parameter Value: {paldeckEntry}")
        embed = discord.Embed(title=f"{palname}", description=f"{paldeckEntry}")
        await ctx.response.send_message(embed=embed)
    else:
        embed = discord.Embed(title="ERROR", description="Wrong pal name given")
        await ctx.response.send_message(embed=embed)


bot.run(f'{token}')
