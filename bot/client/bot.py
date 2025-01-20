import discord
from discord.ext import commands

class CustomBot(commands.Bot):
    def __init__(self, config, **kwargs):
        super().__init__(**kwargs)
        self.config = config

    async def is_owner(self, user: discord.User):
        if await super().is_owner(user):
            return True
            
        owner_ids = self.config["bot"]["owner_ids"]
        return user.id in owner_ids
