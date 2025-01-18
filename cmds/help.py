import discord
from discord.ext import commands
import os
from utils.embeds import Embeds

class Help(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    def get_commands_by_category(self) -> dict:
        categories = {}
        
        for root, _, files in os.walk("cmds"):
            if not any(f.endswith('.py') for f in files):
                continue
                
            if root == "cmds":
                category = "General"
            else:
                category = os.path.basename(root).title()
            
            commands_list = []
            for cog in self.bot.cogs.values():
                for cmd in cog.get_commands():
                    module_path = cmd.module.replace("cmds.", "")
                    expected_path = root.replace("cmds" + os.path.sep, "").replace(os.path.sep, ".")
                    
                    if (root == "cmds" and "." not in module_path) or \
                        (root != "cmds" and module_path.startswith(expected_path)):
                        commands_list.append(cmd)
            
            if commands_list:
                categories[category] = commands_list

        return categories

    @commands.command(aliases=["commands", "h"])
    async def help(self, ctx: commands.Context, command: str = None) -> None:      
        """View extended help for commands"""
  
        if command is None:
            await self.show_all_commands(ctx)
        else:
            await self.show_command_help(ctx, command)

    async def show_all_commands(self, ctx: commands.Context) -> None:
        embed = Embeds.embed(title="Bot Commands")

        for category, commands_list in self.get_commands_by_category().items():
            command_text = "\n".join(
                f"`{cmd.name}` - {cmd.help.split('\n')[0] if cmd.help else 'No description available'}"
                for cmd in commands_list
            )
            embed.add_field(
                name=category,
                value=command_text or "No commands available",
                inline=False
            )

        await ctx.send(embed=embed)

    async def show_command_help(self, ctx: commands.Context, command: str) -> None:
        command = self.bot.get_command(command)
        
        if command is None:
            error_embed = Embeds.error_embed(description=f"Command `{command}` not found.")
            await ctx.send(embed=error_embed)
            return

        embed = Embeds.embed(title=f"Command: {command.name}")
        embed.set_author(
            name=ctx.author.display_name,
            icon_url=ctx.author.display_avatar.url
        )

        help_text = command.help or "No description available"
        help_text = help_text.replace("{prefix}", ctx.prefix)
        
        description = help_text
        usage = None
        
        if "Usage:" in help_text:
            description, usage = help_text.split("Usage:", 1)
        
        embed.description = description.strip()

        embed.add_field(
            name="Aliases",
            value=", ".join(command.aliases) if command.aliases else "n/a",
            inline=True
        )
        
        embed.add_field(
            name="Parameters",
            value=", ".join(command.clean_params.keys()) if command.clean_params else "n/a",
            inline=True
        )
        
        embed.add_field(
            name="Information",
            value="n/a",
            inline=True
        )

        if usage:
            embed.add_field(name="Usage", value=f"```{usage.strip()}```", inline=False)
        else:
            embed.add_field(name="Usage", value="```No usage has been set for this command```", inline=False)

        for category, commands in self.get_commands_by_category().items():
            if command in commands:
                embed.set_footer(text=f"Module: {category}")
                break

        await ctx.send(embed=embed)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Help(bot))
