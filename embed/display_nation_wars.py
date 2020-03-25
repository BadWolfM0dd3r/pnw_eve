import discord
from core.wars import Wars

class DisplayNationWars:
    def display(self, nation_info):
        offensive_wars = Wars().show_offensive_wars(nation_info['offensivewar_ids'])
        defensive_wars = Wars().show_defensive_wars(nation_info['defensivewar_ids'])

        if len(offensive_wars) > 0:
            offensive_value = '\n'.join([war for war in offensive_wars])
        else:
            offensive_value = 'None'

        if len(defensive_wars) > 0:
            defensive_value = '\n'.join([war for war in defensive_wars])
        else:
            defensive_value = 'None'

        embed = discord.Embed(
            color=discord.Color.orange(),
        )

        embed.set_author(
            name=f'{nation_info["name"]} ({nation_info["alliance"]})',
            url=f'https://politicsandwar.com/nation/id={nation_info["nationid"]}',
            icon_url=nation_info['flagurl']
        )

        embed.add_field(
            name=f'Offensive Wars ({nation_info["offensivewars"]}/5)',
            value=offensive_value,
            inline=False
        )

        embed.add_field(
            name=f'Defensive Wars ({nation_info["defensivewars"]}/3)',
            value=defensive_value,
            inline=False
        )

        return embed
