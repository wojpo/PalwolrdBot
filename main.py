import discord
from discord.ext import commands
import requests
from utils.Token import token
from utils.API import apiBaseUrl
from paldeckEntry import paldeckEntry

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    synced = await bot.tree.sync()


@bot.tree.command(name='paldeck-entry')
async def root(ctx: discord.Interaction, palname: str):
    return await paldeckEntry(ctx,palname)


bot.run(f'{token}')
