import discord
from discord.ext import commands
from main import __version__

class OnReady(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user.name} v{__version__} @{discord.__version__}')


async def setup(bot: commands.Bot):
    await bot.add_cog(OnReady(bot)) 