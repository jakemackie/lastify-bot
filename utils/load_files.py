import os
from discord.ext import commands

async def load_files(bot: commands.Bot, dir_path: str) -> None:
    """Helper function to load extensions from a directory."""
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isfile(item_path) and item.endswith(".py"):
            module_path = item_path[:-3].replace(os.path.sep, ".")
            await bot.load_extension(module_path)
            print(f"Loaded {module_path}")
        elif os.path.isdir(item_path):
            await load_files(bot, item_path)
