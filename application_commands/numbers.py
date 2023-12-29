from discord import app_commands, Interaction
import random

class Numbers(app_commands.Group):
    pass


numbers = Numbers(description="Numbers Game")


@numbers.command()
async def play(interaction: Interaction):

    digit1 = str(random.randint(0, 9))
    digit2 = str(random.randint(0, 9))
    while digit2 == digit1:
        digit2 = str(random.randint(0, 9))
    digit3 = str(random.randint(0, 9))
    while digit3 == digit2 or digit3 == digit1:
        digit3 = str(random.randint(0, 9))
    digit4 = str(random.randint(0, 9))
    while digit4 == digit3 or digit4 == digit2 or digit4 == digit1:
        digit4 = str(random.randint(0, 9))
    stored_number = digit1+digit2+digit3+digit4
    print(stored_number)

    # create a variable to store the correct number. DONE
    # correct number is a random set of 4-digit integers. DONE
    # cannot have 2 of the same digit in the number (1234 = valid, 2123 = invalid). DONE
    # validation to ensure only numbers are entered
    # must be whole numbers (integers) decimals are not allowed
    # negative numbers are not allowed
    # send a message with the generated number in Discord

    await interaction.response.send_message(stored_number)


async def setup(bot):
    bot.tree.add_command(numbers)
