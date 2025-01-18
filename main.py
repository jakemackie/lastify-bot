import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from importlib.metadata import version
from utils.load_files import load_files

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=",", intents=intents, help_command=None)
bot.owner_id = 1098234073698275378

async def main():
    try:
        await bot.load_extension("jishaku")
    except ModuleNotFoundError:
        print("Error: jishaku is not installed. Please install it with: pip install -U jishaku")
    except commands.ExtensionError as e:
        print(f"Failed to load jishaku extension: {e}")
    except Exception as e:
        print(f"Unexpected error loading jishaku: {type(e).__name__}: {e}")
        
    await load_files(bot, "cmds")
    await load_files(bot, "events")
    await bot.start(os.getenv("TOKEN"))

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
