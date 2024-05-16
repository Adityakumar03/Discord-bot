import discord
from discord.ext import  commands

class Conditionals(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Conditionals.py is online")
        
    @commands.command()
    async def hello(self, ctx):
        commands_channel = discord.utils.get(ctx.guild.channels, name="testing-1")
        
        if ctx.channel.id == commands_channel.id:
            await ctx.send("Command ran successfully!")
            
    @commands.command()
    async def dev(self, ctx):
        
        if ctx.author.id == 875700541760606208:
            await ctx.send("Command ran succesfully")
        else:
            await ctx.send("Cannot run because you do not have permission")
        
        
async def setup(client):
    await client.add_cog(Conditionals(client))