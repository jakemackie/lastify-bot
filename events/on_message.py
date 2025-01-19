import discord
from discord.ext import commands
from logging import getLogger

class OnMessage(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.logger = getLogger(__name__)

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        if message.author.bot:
            return
        
        # ...

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(OnMessage(bot))
    getLogger(__name__).info(f"{OnMessage.__name__} successfully loaded")

