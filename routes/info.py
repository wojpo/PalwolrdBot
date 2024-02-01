import discord
from discord import Color


async def info(ctx: discord.Interaction):
    embed = discord.Embed(title='HELP', color=Color.green(), description='Bot made by ``wojpo`` which returns info like '
                                                                         '`paldeck`, '
                                                                         '`elements`, `drops`, `work_suitability`, '
                                                                         '`partner_skill`, `skills` about pals')
    embed.set_footer(text='https://discord.gg/wQaF6Peazu')
    await ctx.response.send_message(embed=embed)
    
