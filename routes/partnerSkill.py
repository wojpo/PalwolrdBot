import discord
from discord import Color
import requests
from utils.API import apiBaseUrl
from utils.elemDict import elemDict

async def partner_skill(ctx: discord.Interaction, palname: str):
    endpoint_url = f'{apiBaseUrl}/Pal={palname}'
    response = requests.get(endpoint_url)
    try:
        json_data = response.json()
        paldeck = json_data.get('Paldeck')
        palNumber = paldeck.get('PaldeckNumber')
        palPartnerSkill = json_data.get('PartnerSkill')
        partnerSkillName = palPartnerSkill.get('PartnerSkillName')
        partnerSkillDescription = palPartnerSkill.get('PartnerSkillDescription')

        palelements = json_data.get('Elements')
        element1 = palelements.get('Element1')
        color = elemDict[element1]
        embed = discord.Embed(title="Partner Skill", color=color)
        embed.set_author(name=f"{palname.capitalize()} {palNumber}")
        embed.add_field(name=f"{partnerSkillName}", value=f"{partnerSkillDescription}",inline=False)
        await ctx.response.send_message(embed=embed)
    except AttributeError:
        embed = discord.Embed(title="ERROR", description="Wrong pal name given", color=Color.red())
        await ctx.response.send_message(embed=embed)