import discord
from discord import Color
import requests
from utils.API import apiBaseUrl
from utils.elemDict import elemDict

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

        palelements = json_data.get('Elements')
        element1 = palelements.get('Element1')

        color = elemDict[element1]
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
