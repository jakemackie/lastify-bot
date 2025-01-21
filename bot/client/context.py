from discord.ext import commands
import discord

class CustomContext(commands.Context):
    """Extended context with additional utility methods"""
    
    @property
    def _primary_color(self) -> discord.Color:
        return discord.Color.from_rgb(114, 169, 164)
        
    @property
    def _error_color(self) -> discord.Color:
        return discord.Color.red()
        
    @property
    def _success_color(self) -> discord.Color:
        return discord.Color.green()
    
    def embed(self, **kwargs) -> discord.Embed:
        """Create a themed embed with default color"""
        return discord.Embed(color=self._primary_color, **kwargs)
        
    def error_embed(self, description: str = None, **kwargs) -> discord.Embed:
        """Create an error-themed embed with author mention"""
        if description:
            description = f"{self.author.mention}: {description}"
        return discord.Embed(color=self._error_color, description=description, **kwargs)
        
    def success_embed(self, **kwargs) -> discord.Embed:
        """Create a success-themed embed"""
        return discord.Embed(color=self._success_color, **kwargs) 