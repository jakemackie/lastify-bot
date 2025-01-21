from typing import Union, Optional
from discord import User, Member, utils
from discord.ext import commands

async def resolve_user(ctx: commands.Context, user_input: Union[User, Member, int, str, None]) -> Optional[Union[Member, User]]:
    """Convert various input types to Member or User object
    
    Args:
        ctx: The command context
        user_input: Can be User/Member object, ID (int/str), username, or None
        
    Returns:
        Member object if user is in guild, User object if not, None if not found
    """
    if user_input is None:
        return ctx.author
        
    if isinstance(user_input, (User, Member)):
        user_id = user_input.id
    elif isinstance(user_input, int):
        user_id = user_input
    elif isinstance(user_input, str):
        member = utils.find(
            lambda m: m.name.lower() == user_input.lower(), 
            ctx.guild.members
        )
        if member:
            return member
        try:
            user_id = int(user_input)
        except ValueError:
            return None
    else:
        return None

    return ctx.guild.get_member(user_id) or await ctx.bot.fetch_user(user_id) 
