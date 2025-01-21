from discord import Member
from discord.ext import commands
from logging import getLogger

class Avatar(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="avatar", aliases=["av"])
    async def avatar(self, ctx: commands.Context, user: Member = None) -> None:
        """Get the avatar of a user
        
        Usage:
        {prefix}avatar [user]"""
        user = user or ctx.author
        embed = ctx.embed(description=f"[{user.name}]({user.avatar.url})")
        embed.set_image(url=user.avatar.url)
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Avatar(bot))
    getLogger(__name__).info("Avatar successfully loaded")
