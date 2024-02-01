import discord
from discord import Color


async def info(ctx: discord.Interaction):
    embed = discord.Embed(title='INFO',color = Color.green(), description="")
