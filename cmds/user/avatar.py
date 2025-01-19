from discord import Member
from discord.ext import commands
from utils.embeds import Embeds
from logging import getLogger

class Avatar(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="avatar", aliases=["av"])
    async def avatar(self, ctx: commands.Context, user: Member = None):
        """Get the avatar of a user"""
        user = user or ctx.author
        embed = Embeds.embed(description=f"[{user.name}]({user.avatar.url})")
        embed.set_image(url=user.avatar.url)
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Avatar(bot))
    getLogger(__name__).info("Avatar successfully loaded")
