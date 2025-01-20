from discord import Message
from discord.ext import commands
from logging import getLogger

class OnMessageEdit(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.logger = getLogger(__name__)

    @commands.Cog.listener()
    async def on_message_edit(self, before: Message, after: Message) -> None:
        if after.author.bot:
            return

        if before.content == after.content:
            return
        
        prefixes = await self.bot.get_prefix(after)
        
        if not any(after.content.startswith(prefix) for prefix in prefixes):
            return

        ctx = await self.bot.get_context(after)
        
        if ctx.valid:
            await self.bot.invoke(ctx)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(OnMessageEdit(bot))
    getLogger(__name__).info(f"{OnMessageEdit.__name__} successfully loaded")
