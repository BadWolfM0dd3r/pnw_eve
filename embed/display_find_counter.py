import discord
from core.wars import Wars

class DisplayFindCounter:
    def display(self, aggresor_nation, counter_array):
        aggresor_nation_link = f'https://politicsandwar.com/nation/id={aggresor_nation["nationid"]}'

        embed = discord.Embed(
            color=discord.Color.orange(),
        )

        embed.set_author(name='Counter Recommendations')

        embed.add_field(
            name='Guide',
            value='Nation Name - Nation Score - Military Score',
            inline=False
        )

        embed.add_field(
            name='Aggresor Nation',
            value=f'''
                [{aggresor_nation["name"]} ({aggresor_nation["alliance"]})]({aggresor_nation_link}) - {float(aggresor_nation["score"]):,.2f} - {float(aggresor_nation["military_score"]):,.2f}
            ''',
            inline=False
        )

        for index, counter in enumerate(counter_array):
            counter_link = f'https://politicsandwar.com/nation/id={counter["nationid"]}'

            embed.add_field(
                name=f'Recommendation #{index+1}',
                value=f'''
                    [{counter["nation"]}]({counter_link}) - {float(counter["score"]):,.2f} - {float(counter["military_score"]):,.2f}
                ''',
                inline=False
            )

        return embed
