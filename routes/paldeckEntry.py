import discord
from discord.ext import commands
import requests
from utils.API import apiBaseUrl

async def paldeckEntry(ctx: discord.Interaction, palname: str):
    endpoint_url = f'{apiBaseUrl}/Pal={palname}'
    response = requests.get(endpoint_url)
    if response.status_code == 200:
        json_data = response.json()
        paldeck = json_data.get('Paldeck')
        palNumber = paldeck.get('PaldeckNumber')
        paldeckEntry = paldeck.get('PaldeckEntry')
        embed = discord.Embed(title="Pal Entry", description=f"{paldeckEntry}")
        embed.set_author(name=f"{palname.capitalize()} {palNumber}")
        await ctx.response.send_message(embed=embed)
    else:
        embed = discord.Embed(title="ERROR", description="Wrong pal name given")
        await ctx.response.send_message(embed=embed)