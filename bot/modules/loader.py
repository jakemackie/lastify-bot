import os
from discord.ext import commands
from utils.find_module_paths import find_module_paths
from logging import getLogger

logger = getLogger(__name__)

async def load_module(bot: commands.Bot, path: str) -> None:
    """Helper function to load a module or directory of modules as bot extensions."""
    if os.path.isdir(path):
        module_paths = await find_module_paths(path)
        for module_path in module_paths:
            try:
                await bot.load_extension(module_path)
                logger.info(f"Loaded module: {module_path}")
            except commands.ExtensionError as e:
                logger.error(f"Failed to load module {module_path}: {str(e)}")
    else:
        try:
            await bot.load_extension(path)
            logger.info(f"Loaded module: {path}")
        except commands.ExtensionError as e:
            logger.error(f"Failed to load module {path}: {str(e)}")

async def load_modules(bot, module_list):
    """Load multiple modules at once"""
    for module in module_list:
        await load_module(bot, module)
