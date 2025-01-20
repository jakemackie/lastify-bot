import discord
from discord.ext import commands
from utils.prefix import get_prefix
from .bot import CustomBot

def create_bot(config):
    intents = discord.Intents.all()
    
    bot = CustomBot(
        config=config,
        command_prefix=get_prefix,
        intents=intents,
        help_command=None
    )
    
    return bot