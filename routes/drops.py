import discord
from discord import Color
import requests
from utils.API import apiBaseUrl
from utils.elemDict import elemDict


async def drops(ctx: discord.Interaction, palname: str):
    endpoint_url = f'{apiBaseUrl}/Pal={palname}'
    response = requests.get(endpoint_url)
    try:
        json_data = response.json()
        paldeck = json_data.get('Paldeck')
        palNumber = paldeck.get('PaldeckNumber')
        paldrops = json_data.get('Drops')
        drop1 = paldrops.get('Drop1')
        drop2 = paldrops.get('Drop2')
        drop3 = paldrops.get('Drop3')
        drop4 = paldrops.get('Drop4')
        palelements = json_data.get('Elements')
        element1 = palelements.get('Element1')

        color = elemDict[element1]
        embed = discord.Embed(title="Drops", color=color)
        embed.set_author(name=f"{palname.capitalize()} {palNumber}")
        embed.add_field(name="Drop 1", value=f"{drop1}", inline=False)
        if drop2 != "None":
            embed.add_field(name="Drop 2", value=f"{drop2}", inline=False)
        if drop3 != "None":
            embed.add_field(name="Drop 3", value=f"{drop3}", inline=False)
        if drop4 != "None":
            embed.add_field(name="Drop 4", value=f"{drop4}", inline=False)
        await ctx.response.send_message(embed=embed)
    except AttributeError:
        embed = discord.Embed(title="ERROR", description="Wrong pal name given", color=Color.red())
        await ctx.response.send_message(embed=embed)
