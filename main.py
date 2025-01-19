import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
from utils.load_module import load_module
import logging
from utils.prefix import get_prefix

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=get_prefix, intents=intents, help_command=None)
bot.owner_id = 1098234073698275378

async def main():
    await load_module(bot, "jishaku")
    await load_module(bot, "cmds")
    await load_module(bot, "events")
    
    logger.info("Starting bot...")
    await bot.start(getenv("TOKEN"))

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
