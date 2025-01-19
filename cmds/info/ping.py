import discord
from discord.ext import commands
from logging import getLogger
class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.logger = getLogger(__name__)
        
    @commands.command()
    async def ping(self, ctx: commands.Context) -> None:
        """Ping the bot to check if it's alive
        
        Usage:
        {prefix}ping"""
        before = discord.utils.utcnow()
        msg = await ctx.send(f"`{round(self.bot.latency * 1000)}ms`")
        after = discord.utils.utcnow()
        
        latency = (after - before).total_seconds() * 1000
        await msg.edit(content=f"`{round(self.bot.latency * 1000)}ms` (edit: `{round(latency)}ms`)")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Ping(bot))
    getLogger(__name__).info(f"{Ping.__name__} successfully loaded")
