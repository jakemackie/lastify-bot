import discord

class Embeds:
    PRIMARY_COLOR = discord.Color.from_rgb(114, 169, 164)
    ERROR_COLOR = discord.Color.red()
    SUCCESS_COLOR = discord.Color.green()

    @classmethod
    def embed(cls, **kwargs) -> discord.Embed:
        """Create a themed embed with default color"""
        return discord.Embed(color=cls.PRIMARY_COLOR, **kwargs)

    @classmethod
    def error_embed(cls, **kwargs) -> discord.Embed:
        """Create an error-themed embed"""
        return discord.Embed(color=cls.ERROR_COLOR, **kwargs)

    @classmethod
    def success_embed(cls, **kwargs) -> discord.Embed:
        """Create a success-themed embed"""
        return discord.Embed(color=cls.SUCCESS_COLOR, **kwargs) 
