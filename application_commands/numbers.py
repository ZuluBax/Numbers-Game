from discord import app_commands, Interaction


class Numbers(app_commands.Group):
    pass

numbers=Numbers(description="Numbers Game")

@numbers.command()
async def play(interaction: Interaction):
    await interaction.response.send_message("Numbers game coming soon")

async def setup(bot):
    bot.tree.add_command(numbers)
