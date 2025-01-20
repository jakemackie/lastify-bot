import asyncio
from logging import getLogger
from bot.client.setup import create_bot
from bot.core.config import load_config
from bot.core.logging import logging_init
from bot.modules.loader import load_modules

logger = getLogger(__name__)

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
