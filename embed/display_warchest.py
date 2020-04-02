import discord
from core.warchest import WarChest

class DisplayWarChest:
    def display(self, city_count, city_warchest):
        embed = discord.Embed(
            color=discord.Color.orange(),
        )

        embed.set_author(
            name=f'City {city_count} War Chest requirements'
        )

        embed.add_field(
            name='Gas',
            value=f'{city_warchest["Gas"]:,}',
            inline=True
        )

        embed.add_field(
            name='Munitions',
            value=f'{city_warchest["Munitions"]:,}',
            inline=True
        )

        embed.add_field(
            name='Food',
            value=f'{city_warchest["Food"]:,}',
            inline=True
        )

        embed.add_field(
            name='Steel',
            value=f'{city_warchest["Steel"]:,}',
            inline=True
        )

        embed.add_field(
            name='Aluminum',
            value=f'{city_warchest["Aluminum"]:,}',
            inline=True
        )

        embed.add_field(
            name='Power Plant Fuel',
            value=f'{city_warchest["Fuel"]:,}',
            inline=True
        )

        embed.add_field(
            name='Cash on hand',
            value=f'{city_warchest["Cash"]:,}',
            inline=False
        )

        return embed
