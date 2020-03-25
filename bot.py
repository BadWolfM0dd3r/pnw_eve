import discord
import os
import asyncio
import time
from discord.ext import commands
from settings import DISCORD_TOKEN
from core.nations import Nations

class Bot(commands.Bot):
    def __init__(self, **options):
        super().__init__(command_prefix='=')
        super().remove_command('help')

        super().add_command(self.ping)
        super().add_command(self.display_nation)

    @classmethod
    def start_bot(bot, token=None):
        """Actual method to start the bot
        
        Args:
            bot ([type]): [description]
            token ([type], optional): [description]. Defaults to None.
        """
        bot = bot()
        token = token or DISCORD_TOKEN

        try:
            bot.run(token, reconnect=True)
        except Exception as e:
            print(e)

    async def on_connect(self):
        print('bot.py connected!')

    async def on_ready(self):
        print(f'Hi, {self.user} is online!')

    async def on_message(self, message):
        # respond to others only
        if message.author.id == self.user.id:
            return

        await self.process_commands(message)

    @commands.command()
    async def ping(self):
        await self.send('Pong!')

    @commands.command()
    async def find(self, nation_id):
        await self.send(f'The nation id youre looking for is: {nation_id}. {round(self.latency*1000)}ms')

    @commands.command(aliases=['nation'])
    async def display_nation(self, nation_id):
        """Display a nation's info
        
        Args:
            nation_id (int): Unique ID of nation get info
        """
        nation_info = Nations().find_nation(nation_id)

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
            url=f'https://politicsandwar.com/nation/id={nation_id}',
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

        embed.set_footer(text=f'Latency: WIPms') # self.latency doesn't work, need to find an alternative

        return await self.send(embed=embed)

    @commands.command()
    async def raid(self, nation_id, alliance_id=0):
        await self.send(f'Raid target is: {nation_id}, member of {alliance_id}. {round(self.latency*1000)}ms')

    @commands.command(pass_context=True)
    async def help(self):
        author = self.message.author

        embed = discord.Embed(
            colour=discord.Colour.blue()
        )

        embed.add_field(name='Help', value='Test', inline=False)

        await self.send(embed=embed)

if __name__ == '__main__':
    Bot.start_bot()
