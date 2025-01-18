import discord
from discord.ext import commands
from main import __version__

class Version(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command()
    async def version(self, ctx: commands.Context) -> None:
        """Display the current bot version"""
        await ctx.send(f"Bot version: v{__version__}")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Version(bot)) 