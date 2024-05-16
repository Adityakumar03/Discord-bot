import discord
from discord.ext import commands
import json

class Mute(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print("Mute.py is online")
        
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def setmuterole(self, ctx, role: discord.Role):
        with open("cogs/jsonfiles/mutes.json", "r") as f:
            mute_role = json.load(f)
        
            mute_role[str(ctx.guild.id)] = role.name
        
        with open("cogs/jsonfiles/mutes.json", "w") as f:
            json.dump(mute_role, f, indent=4)
            
        conf_embed = discord.Embed(title="Success!", color=discord.Color.green())
        conf_embed.add_field(name="Mute role has been set!", value=f"The mute role has been changed to '{role.mention}' for this guild. All members who are muted will be equipped with this role")
        
        await ctx.send(embed=conf_embed)
        
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def setmuterole(self, ctx, role: discord.Role):
        with open("cogs/jsonfiles/mutes.json", "r") as f:
            mute_role = json.load(f)
        
            mute_role[str(ctx.guild.id)] = role.name
        
        with open("cogs/jsonfiles/mutes.json", "w") as f:
            json.dump(mute_role, f, indent=4)
            
        conf_embed = discord.Embed(title="Success!", color=discord.Color.green())
        conf_embed.add_field(name="Unmute role has been set!", value=f"The unmute role has been changed to '{role.mention}' for this guild. All members who are muted will be equipped with this role")
        
        await ctx.send(embed=conf_embed)
        
        
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member):
        with open("cogs/jsonfiles/mutes.json", "r") as f:
            role = json.load(f)
            
            mute_role = discord.utils.get(ctx.guild.roles, name=role[str(ctx.guild.id)])
        
        await member.add_roles(mute_role)
        
        conf_embed = discord.Embed(title="Success!", color=discord.Color.green())
        conf_embed.add_field(name="Muted", value=f"{member.mention} has been muted by {ctx.author.mention}", inline=False)
        await ctx.send(embed=conf_embed)
        
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unmute(self, ctx, member: discord.Member):
        with open("cogs/jsonfiles/mutes.json", "r") as f:
            role = json.load(f)
            
            mute_role = discord.utils.get(ctx.guild.roles, name=role[str(ctx.guild.id)])
        
        await member.remove_roles(mute_role)
        
        conf_embed = discord.Embed(title="Success!", color=discord.Color.green())
        conf_embed.add_field(name="Unmuted", value=f"{member.mention} has been unmuted by {ctx.author.mention}", inline=False)
        await ctx.send(embed=conf_embed)
        
    
        
async def setup(client):
    await client.add_cog(Mute(client))