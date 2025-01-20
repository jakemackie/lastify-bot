from discord import User
from discord.ext import commands
from bot.core.config import Config

class CustomBot(commands.Bot):
    def __init__(self, config: Config, **kwargs):
        super().__init__(**kwargs)
        self.config = config

    async def is_owner(self, user: User):
        if await super().is_owner(user):
            return True
            
        return user.id in self.config.bot.owner_ids
