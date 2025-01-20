import discord
from discord.ext import commands
import aiosqlite

async def get_prefix(bot: commands.Bot, message: discord.Message) -> list[str]:
    """Get the appropriate prefix for a message context"""
    default_prefix = ","
    prefixes = set()

    if not message.guild:
        return [default_prefix]

    async with aiosqlite.connect('database.db') as db:
        await db.execute('''CREATE TABLE IF NOT EXISTS guild_prefixes (guild_id INTEGER PRIMARY KEY, prefix TEXT)''')
        await db.execute('''CREATE TABLE IF NOT EXISTS user_prefixes (user_id INTEGER PRIMARY KEY, prefix TEXT)''')
        await db.commit()

        cursor = await db.execute('SELECT prefix FROM user_prefixes WHERE user_id = ?', (message.author.id,))
        user_prefix = await cursor.fetchone()
        if user_prefix:
            prefixes.add(user_prefix[0])

        cursor = await db.execute('SELECT prefix FROM guild_prefixes WHERE guild_id = ?', (message.guild.id,))
        guild_prefix = await cursor.fetchone()
        if guild_prefix:
            prefixes.add(guild_prefix[0])

        # Only add default prefix if no custom prefixes are set
        if not prefixes:
            prefixes.add(default_prefix)

        return list(prefixes)

async def set_guild_prefix(guild_id: int, prefix: str) -> None:
    """Set a custom prefix for a guild"""
    async with aiosqlite.connect('database.db') as db:
        await db.execute('''INSERT OR REPLACE INTO guild_prefixes (guild_id, prefix) VALUES (?, ?)''', (guild_id, prefix))
        await db.commit()

async def set_user_prefix(user_id: int, prefix: str) -> None:
    """Set a custom prefix for a user"""
    async with aiosqlite.connect('database.db') as db:
        await db.execute('''INSERT OR REPLACE INTO user_prefixes (user_id, prefix) VALUES (?, ?)''', (user_id, prefix))
        await db.commit()

async def get_guild_prefix(guild_id: int | None) -> str:
    """Get the guild's prefix or default if none is set"""
    if guild_id is None:
        return ","
        
    async with aiosqlite.connect('database.db') as db:
        cursor = await db.execute('SELECT prefix FROM guild_prefixes WHERE guild_id = ?', (guild_id,))
        guild_prefix = await cursor.fetchone()
        return guild_prefix[0] if guild_prefix else ","

async def get_user_prefix(user_id: int) -> str | None:
    """Get the user's prefix if set"""
    async with aiosqlite.connect('database.db') as db:
        cursor = await db.execute('SELECT prefix FROM user_prefixes WHERE user_id = ?', (user_id,))
        user_prefix = await cursor.fetchone()
        return user_prefix[0] if user_prefix else None
