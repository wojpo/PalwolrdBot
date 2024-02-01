import discord
from discord import Color


async def info(ctx: discord.Interaction):
    embed = discord.Embed(title='HELP', color=Color.green(), description='Bot made by ``wojpo`` which returns data '
                                                                         'about pals'
                                                                         'from '
                                                                         '`https://palworld.fandom.com/wiki'
                                                                         '/Palworld_Wiki`'
                          )
    embed.add_field(name="Commands", value='`paldeck`, `elements`, `drops`, `work_suitability`, `partner_skill`, '
                                           '`skills`')
    embed.set_footer(text='https://discord.gg/wQaF6Peazu')
    await ctx.response.send_message(embed=embed)
