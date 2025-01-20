from discord import __version__
from discord.ext import commands
from logging import getLogger

class OnReady(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.logger = getLogger(__name__)

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        self.logger.info(f"{self.bot.user.name} @{__version__}")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(OnReady(bot))
    getLogger(__name__).info(f"{OnReady.__name__} successfully loaded")
