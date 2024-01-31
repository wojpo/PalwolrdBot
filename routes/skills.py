import discord
from discord import Color
import requests
from utils.API import apiBaseUrl


async def skills(ctx: discord.Interaction, palname: str):
    endpoint_url = f'{apiBaseUrl}/Pal={palname}'
    response = requests.get(endpoint_url)
    try:
        json_data = response.json()
        paldeck = json_data.get('Paldeck')
        palNumber = paldeck.get('PaldeckNumber')
        palSkills = json_data.get('Skills')
        lvl1 = palSkills.get('lvl1')
        lvl7 = palSkills.get('lvl7')
        lvl15 = palSkills.get('lvl15')
        lvl22 = palSkills.get('lvl22')
        lvl30 = palSkills.get('lvl30')
        lvl40 = palSkills.get('lvl40')
        lvl50 = palSkills.get('lvl50')

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
        embed = discord.Embed(title="Skills", color=color)
        embed.set_author(name=f"{palname.capitalize()} {palNumber}")
        embed.add_field(name="lvl 1", value=f"{lvl1}", inline=False)
        embed.add_field(name="lvl 7", value=f"{lvl7}", inline=False)
        embed.add_field(name="lvl 15", value=f"{lvl15}", inline=False)
        embed.add_field(name="lvl 22", value=f"{lvl22}", inline=False)
        embed.add_field(name="lvl 30", value=f"{lvl30}", inline=False)
        embed.add_field(name="lvl 40", value=f"{lvl40}", inline=False)
        embed.add_field(name="lvl 50", value=f"{lvl50}", inline=False)
        await ctx.response.send_message(embed=embed)

    except AttributeError:
        embed = discord.Embed(title="ERROR", description="Wrong pal name given", color=Color.red())
        await ctx.response.send_message(embed=embed)
