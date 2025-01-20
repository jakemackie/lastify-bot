import asyncio
import logging
from bot.client import create_bot
from bot.config import load_config
from utils.load_module import load_modules
from config.logging import logging_init

logger = logging.getLogger(__name__)

async def main():
    logging_init()

    config = load_config()
    
    bot = create_bot(config)
    
    await load_modules(bot, [
        "jishaku", 
        "cmds", 
        "events"
    ])
    
    logger.info("Starting bot...")
    await bot.start(config["bot"]["token"])

if __name__ == "__main__":
    asyncio.run(main())
