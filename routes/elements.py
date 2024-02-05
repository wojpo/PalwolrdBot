import discord
from discord import Color
import requests
from utils.API import apiBaseUrl
from utils.elemDict import elemDict


async def elements(ctx: discord.Interaction, palname: str):
    endpoint_url = f'{apiBaseUrl}/Pal={palname}'
    response = requests.get(endpoint_url)
    try:
        json_data = response.json()
        paldeck = json_data.get('Paldeck')
        palNumber = paldeck.get('PaldeckNumber')
        palelements = json_data.get('Elements')
        element1 = palelements.get('Element1')
        element2 = palelements.get('Element2')

        color = elemDict[element1]
        embed = discord.Embed(title="Elements", color=color)
        embed.set_author(name=f"{palname.capitalize()} {palNumber}")
        embed.add_field(name="Element 1", value=f"{element1}", inline=False)
        if element2 != "None":
            embed.add_field(name="Element 2", value=f"{element2}", inline=False)
        await ctx.response.send_message(embed=embed)
    except AttributeError:
        embed = discord.Embed(title="ERROR", description="Wrong pal name given", color=Color.red())
        await ctx.response.send_message(embed=embed)
