import asyncio
import logging
from bot.client import create_bot
from bot.config import load_config
from utils.load_module import load_modules

logger = logging.getLogger(__name__)

async def main():
    config = load_config()
    
    bot = create_bot(config)
    
    # Load all modules
    await load_modules(bot, ["jishaku", "cmds", "events"])
    
    logger.info("Starting bot...")
    await bot.start(config["bot"]["token"])

if __name__ == "__main__":
    asyncio.run(main())
