import discord
from discord.ext import commands

class OnMessageEdit(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        if after.author.bot:
            return

        if before.content == after.content:
            return

        if not after.content.startswith(self.bot.command_prefix):
            return

        ctx = await self.bot.get_context(after)
        
        if ctx.valid:
            await self.bot.invoke(ctx)

async def setup(bot: commands.Bot):
    await bot.add_cog(OnMessageEdit(bot)) 