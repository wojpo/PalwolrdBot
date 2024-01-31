import discord
from discord import Color
import requests
from utils.API import apiBaseUrl


async def paldeck(ctx: discord.Interaction, palname: str):
    endpoint_url = f'{apiBaseUrl}/Pal={palname}'
    response = requests.get(endpoint_url)
    try:
        json_data = response.json()
        paldeck = json_data.get('Paldeck')
        palNumber = paldeck.get('PaldeckNumber')
        paldeckEntry = paldeck.get('PaldeckEntry')
        palAppearance = paldeck.get('PalAppearance')
        palIcon = json_data.get('paliconurl')

        # EMBED COLOR DEPEND ON PAL ELEMENT
        palelements = json_data.get('Elements')
        element1 = palelements.get('Element1')
        if element1 == 'Dark':
            color = Color.dark_gray()
        if element1 == 'Dragon':
            color = Color.purple()
        if element1 == 'Electricity':
            color = Color.yellow()
        if element1 == 'Fire':
            color = Color.red()
        if element1 == 'Grass':
            color = Color.green()
        if element1 == 'Ground':
            color = 0x964b00
        if element1 == 'Ice':
            color = Color.blue()
        if element1 == 'Neutral':
            color = 0xffe5b4
        if element1 == 'Water':
            color = Color.teal()

        embed = discord.Embed(title="Paldeck", color=color)
        embed.set_author(name=f"{palname.capitalize()} {palNumber}")
        embed.add_field(name="Paldeck Entry", value=f"{paldeckEntry}", inline=False)
        embed.add_field(name="Pal Appearance", value=f"{palAppearance}", inline=False)
        await ctx.response.send_message(embed=embed)
    except AttributeError:
        embed = discord.Embed(title="ERROR", description="Wrong pal name given", color=Color.red())
        await ctx.response.send_message(embed=embed)
