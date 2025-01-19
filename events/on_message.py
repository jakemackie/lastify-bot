import discord
from discord.ext import commands
from logging import getLogger
from utils.prefix import get_guild_prefix, get_user_prefix

class OnMessage(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.logger = getLogger(__name__)

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        if message.author.bot:
            return

        if self.bot.user.mentioned_in(message) and len(message.content.split()) == 1:            
            response_parts = []
            
            server_prefix = await get_guild_prefix(message.guild.id)
            response_parts.append(f"(server) `{server_prefix}`")

            user_prefix = await get_user_prefix(message.author.id)
            if user_prefix:
                response_parts.append(f"(you) `{user_prefix}`")
            
            await message.reply("\n".join(response_parts), mention_author=False)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(OnMessage(bot))
    getLogger(__name__).info(f"{OnMessage.__name__} successfully loaded")

