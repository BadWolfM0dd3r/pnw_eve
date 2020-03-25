import discord
from core.nations import Nations

class DisplayNation:
    def display(self, nation_info):
        if nation_info['vmode'] != '0':
            vacation_mode = f'🏖 Out of Vacation mode in {nation_info["vmode"]} turns'
        else:
            vacation_mode = ''

        embed = discord.Embed(
            description=vacation_mode,
            color=discord.Color.orange(),
        )

        embed.set_author(
            name=f'{nation_info["name"]} ({nation_info["alliance"]}) - Active {nation_info["minutessinceactive"]//60}hrs ago',
            url=f'https://politicsandwar.com/nation/id={nation_info["nationid"]}',
            icon_url=nation_info['flagurl']
        )

        embed.add_field(
            name='Stats',
            value=f'''
                {nation_info["cities"]} cities
                {nation_info["totalinfrastructure"]} infra
                {nation_info["landarea"]} land
                {nation_info["score"]} nation score
                {nation_info["offensivewars"]} off wars
                {nation_info["defensivewars"]} def wars
            ''',
            inline=True
        )

        embed.add_field(
            name='Military',
            value=f'''
                🛡 {nation_info["soldiers"]}
                🚍 {nation_info["tanks"]}
                🛩 {nation_info["aircraft"]}
                🚢 {nation_info["ships"]}
            ''',
            inline=True
        )
        
        embed.add_field(
            name='Policies',
            value=f'''
                {nation_info["domestic_policy"]}
                {nation_info["war_policy"]}
            ''',
            inline=True
        )

        return embed