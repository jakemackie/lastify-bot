from discord.ext import commands
from logging import getLogger
from utils.prefix import set_guild_prefix, set_user_prefix

class Prefix(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.logger = getLogger(__name__)

    @commands.group(invoke_without_command=True)
    async def prefix(self, ctx: commands.Context) -> None:
        """Prefix management commands"""
        await ctx.send_help(ctx.command)

    @prefix.command(name="set")
    @commands.has_permissions(manage_guild=True)
    async def prefix_set(self, ctx: commands.Context, prefix: str) -> None:
        """Set the prefix for the current server"""
        if len(prefix) > 5:
            await ctx.send("Prefix must be 5 characters or less!")
            return
            
        await set_guild_prefix(ctx.guild.id, prefix)
        await ctx.send(f"Server prefix has been set to: `{prefix}`")

    @commands.command()
    async def selfprefix(self, ctx: commands.Context, prefix: str) -> None:
        """Set your personal prefix
        
        Usage:
        {prefix}selfprefix <prefix>"""
        if len(prefix) > 5:
            await ctx.send("Prefix must be 5 characters or less!")
            return
            
        await set_user_prefix(ctx.author.id, prefix)
        await ctx.send(f"Your personal prefix has been set to: `{prefix}`")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Prefix(bot))
    getLogger(__name__).info(f"{Prefix.__name__} successfully loaded")
