from discord import app_commands, Interaction


class Numbers(app_commands.Group):
    pass


numbers = Numbers(description="Numbers Game")


@numbers.command()
async def play(interaction: Interaction):
    # create a variable to store the correct number
    # correct number is a random set of 4-digit integers
    # cannot have 2 of the same digit in the number (1234 = valid, 2123 = invalid)
    # validation to ensure only numbers are entered
    # must be whole numbers (integers) decimals are not allowed
    # negative numbers are not allowed

    # send a message with the generated number in Discord

    await interaction.response.send_message("Numbers game coming soon")


async def setup(bot):
    bot.tree.add_command(numbers)
