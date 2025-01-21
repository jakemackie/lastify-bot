from discord import User, Member
from discord.ext import commands
from logging import getLogger
from datetime import datetime
from utils.resolvers import resolve_user

class UserInfo(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="userinfo", aliases=["ui"])
    async def userinfo(self, ctx: commands.Context, *, user: str = None) -> None:
        """Get information about a user
        
        Usage:
        {prefix}userinfo <user>"""
        user = await resolve_user(ctx, user)
        
        if user is None:
            embed = ctx.error_embed(description="Could not find that user.")
            await ctx.send(embed=embed)
            return
        
        footer_parts = []
        
        if isinstance(user, Member) and user.guild == ctx.guild:
            roles = ", ".join([r.mention for r in user.roles][:8])
            
            sorted_members = sorted(ctx.guild.members, key=lambda m: m.joined_at or datetime.max)
            join_position = sorted_members.index(user) + 1
            footer_parts.append(f"Join position: {join_position}")
            
            joined_info = f"\nJoined:  {user.joined_at.strftime('%m/%d/%Y, %I:%M %p')} (<t:{int(user.joined_at.timestamp())}:R>)"
            roles_field = {
                "name": "Roles",
                "value": f"{roles}{'...' if len(user.roles) > 8 else ''}",
                "inline": False
            }
        else:
            joined_info = ""
            roles_field = None

        mutual_servers = len([guild for guild in self.bot.guilds if user in guild.members])
        if mutual_servers:
            footer_parts.append(f"{mutual_servers} mutual servers")

        footer_text = " ∙ ".join(footer_parts) if footer_parts else None

        embed = ctx.embed(
        ).set_author(name=f"{user.name} ({user.id})"
        ).add_field(
            inline=False,
            name="Dates",
            value=(
                f"Created: {user.created_at.strftime('%m/%d/%Y, %I:%M %p')} (<t:{int(user.created_at.timestamp())}:R>)"
                f"{joined_info}"
            )
        )

        if roles_field:
            embed.add_field(**roles_field)

        if footer_text:
            embed.set_footer(text=footer_text)

        embed.set_thumbnail(url=user.avatar.url)

        await ctx.send(embed=embed)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(UserInfo(bot))
    getLogger(__name__).info("UserInfo successfully loaded")
