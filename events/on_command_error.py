from secrets import token_hex
from discord.ext import commands
from logging import getLogger
import discord

class CommandErrorHandler(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.logger = getLogger(__name__)

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: Exception):
        if isinstance(error, commands.CommandNotFound):
            return
            
        if isinstance(error, commands.MissingPermissions):
            embed = ctx.error_embed(description="You don't have permission to use this command.")
            await ctx.send(embed=embed)
            return
        
        err_code = token_hex(4)
        self.logger.error(f"({err_code}) Error in {ctx.command}: {str(error)}", exc_info=error)
        embed = ctx.error_embed(description=f"An error occurred, please report this error code to the developer(s): `{err_code}`")
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(CommandErrorHandler(bot))
    getLogger(__name__).info("CommandErrorHandler successfully loaded")
