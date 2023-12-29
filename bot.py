import discord
from discord.ext import commands

import settings

config = settings.Config().load()
intents: discord.Intents = discord.Intents(
    guilds=True,
    members=True,
    emojis=True,
    webhooks=True,
    presences=True,
    messages=True,
    reactions=True,
    message_content=True,
)


class Bot(commands.AutoShardedBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


bot = Bot(
    command_prefix=commands.when_mentioned_or("!", "! "),
    case_insensitive=True,
    intents=intents,
    status="online",
    activity=discord.Activity(
        type=1,
        name="We are awesome",
    ),
)


@bot.event
async def on_ready():
    for command_file in settings.HIDDEN_COMMANDS_DIR.glob("*.py"):
        if command_file.name != "__init__.py":
            command_name = command_file.name[:-3]
            print("loading hidden command: " + command_name)
            await bot.load_extension(f"hidden_commands.{command_name}")

    for command_file in settings.APPLICATION_COMMANDS_DIR.glob("*.py"):
        if command_file.name != "__init__.py":
            command_name = command_file.name[:-3]
            print("loading application command: " + command_name)
            await bot.load_extension(f"application_commands.{command_name}")
    print("I am working!")

bot.run(str(config.BOT_TOKEN))
