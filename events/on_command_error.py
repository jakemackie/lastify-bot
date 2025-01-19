import discord
from discord.ext import commands
from logging import getLogger
from utils.embeds import Embeds

class CommandErrorHandler(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.logger = getLogger(__name__)

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: Exception):
        if isinstance(error, commands.CommandNotFound):
            return
            
        if isinstance(error, commands.MissingPermissions):
            embed = Embeds.error_embed(description="You don't have permission to use this command.")
            await ctx.send(embed=embed)
            return

        self.logger.error(f"Error in {ctx.command}: {str(error)}", exc_info=error)
        embed = Embeds.error_embed(description=f"An error occurred: {str(error)}")
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(CommandErrorHandler(bot))
    getLogger(__name__).info("CommandErrorHandler successfully loaded")
