import os

import discord
from discord.ext import commands
from utils.Token import token
from routes.paldeck import paldeck
from routes.elements import elements
from routes.drops import drops
from routes.partnerSkill import partner_skill
from routes.workSuitability import work_suitability
from routes.skills import skills
from routes.info import info

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    synced = await bot.tree.sync()


@bot.tree.command(name='paldeck', description="Returns basic info about pals! OwO")
async def root(ctx: discord.Interaction, palname: str):
    return await paldeck(ctx, palname)


@bot.tree.command(name='elements', description="Returns info about pals elements! UwU")
async def root(ctx: discord.Interaction, palname: str):
    return await elements(ctx, palname)


@bot.tree.command(name='drops', description="Returns info about pals drops! TwT")
async def root(ctx: discord.Interaction, palname: str):
    return await drops(ctx, palname)


@bot.tree.command(name='partner_skill', description="Returns info about pals Partner Skill! QwQ")
async def root(ctx: discord.Interaction, palname: str):
    return await partner_skill(ctx, palname)


@bot.tree.command(name='work_suitability', description="Returns info about pals Work Suitability! PwP")
async def root(ctx: discord.Interaction, palname: str):
    return await work_suitability(ctx, palname)


@bot.tree.command(name='skills', description="Returns info about pals skills! JwJ")
async def root(ctx: discord.Interaction, palname: str):
    return await skills(ctx, palname)


@bot.tree.command(name='help', description='Returns info about bot! MwM')
async def root(ctx: discord.Interaction):
    return await info(ctx)


bot.run(token)
