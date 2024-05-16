import discord
from discord import app_commands
from discord.ext import commands

class AppCommands(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.tree.sync()
        print(f"{__name__} loaded successfully!")
        
    @app_commands.command(name="avatar", description="Sends user's avatar in a embed (sends own avatar if user is left none)")
    async def avatar(self, interaction: discord.Interaction, member: discord.Member=None):
        if member is None:
            member = interaction.user
        elif member is not None:
            member = member
            
        avatar_embed = discord.Embed(title=f"{member.name}'s Avatar", color=discord.Color.random())
        avatar_embed.set_image(url=member.avatar)
        avatar_embed.set_footer(text=f"Requested by {interaction.user.name}", icon_url=interaction.user.avatar)

        await interaction.response.send_message(embed=avatar_embed)
                
async def setup(client):
    await client.add_cog(AppCommands(client))