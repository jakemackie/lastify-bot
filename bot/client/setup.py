from discord import Intents
from utils.prefix import get_prefix
from .bot import CustomBot

def create_bot(config):
    intents = Intents.all()
    
    bot = CustomBot(
        config=config,
        command_prefix=get_prefix,
        intents=intents,
        help_command=None
    )
    
    return bot