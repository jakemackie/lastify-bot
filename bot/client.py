import discord
from discord.ext import commands
from utils.prefix import get_prefix

def create_bot(config):
    intents = discord.Intents.default()
    intents.message_content = True
    
    bot = commands.Bot(
        command_prefix=get_prefix,
        intents=intents,
        help_command=None
    )
    
    bot.owner_id = config["bot"]["owner_id"]
    return bot 