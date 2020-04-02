import discord

class DisplayError:
    def display(self, message):
        embed = discord.Embed(
            color=discord.Color.orange()
        )

        embed.set_author(name=message)

        return embed
