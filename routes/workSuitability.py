import discord
from discord import Color
import requests
from utils.API import apiBaseUrl


async def work_suitability(ctx: discord.Interaction, palname: str):
    endpoint_url = f'{apiBaseUrl}/Pal={palname}'
    response = requests.get(endpoint_url)
    try:
        json_data = response.json()
        paldeck = json_data.get('Paldeck')
        palNumber = paldeck.get('PaldeckNumber')
        workSuitability = json_data.get('WorkSuitability')
        kindling = workSuitability.get('Kindling')
        planting = workSuitability.get('Planting')
        handiwork = workSuitability.get('Handiwork')
        lumbering = workSuitability.get('Lumbering')
        medicineProduction = workSuitability.get('MedicineProduction')
        transporting = workSuitability.get('Transporting')
        watering = workSuitability.get('Watering')
        generatingElectricity = workSuitability.get('GeneratingElectricity')
        gathering = workSuitability.get('Gathering')
        mining = workSuitability.get('Mining')
        cooling = workSuitability.get('Cooling')
        farming = workSuitability.get('Farming')

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

        embed = discord.Embed(title="Work Suitability", color=color)
        embed.set_author(name=f"{palname.capitalize()} {palNumber}")
        embed.add_field(name="Kindling :fire:",value=f'{kindling}')
        embed.add_field(name='Planting :seedling:',value=f'{planting} ')
        embed.add_field(name='Handiwork :raised_hand:',value=f'{handiwork}')
        embed.add_field(name='Lumbering :axe:',value=f'{lumbering}')
        embed.add_field(name='Medicine Production :microscope:',value=f'{medicineProduction}')
        embed.add_field(name='Transporting :package:',value=f'{transporting}')
        embed.add_field(name='Watering :sweat_drops:',value=f'{watering}')
        embed.add_field(name='Generating Electricity :bulb:',value=f'{generatingElectricity}')
        embed.add_field(name='Gathering :palm_down_hand:',value=f'{gathering}')
        embed.add_field(name='Mining :pick:',value=f'{mining}')
        embed.add_field(name='Cooling :snowflake:',value=f'{cooling}')
        embed.add_field(name='Farming :herb:',value=f'{farming}')
        await ctx.response.send_message(embed=embed)
    except AttributeError:
        embed = discord.Embed(title="ERROR", description="Wrong pal name given", color=Color.red())
        await ctx.response.send_message(embed=embed)