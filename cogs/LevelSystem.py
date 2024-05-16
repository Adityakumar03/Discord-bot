import discord
from discord.ext import commands
import json
import asyncio
import math
import random

class LevelSystem(commands.Cog):
    def __init__(self, client):
        self.client = client
        
        self.client.loop.create_task(self.save())
        
        with open("cogs/jsonfiles/users.json", "r") as f:
            self.users = json.load(f)
            
    def level_up(self, author_id):
        current_experience = self.users[author_id]["Experience"]
        current_level = self.users[author_id]["Level"]
        
        if current_experience >= math.ceil((6 * (current_level ** 4)) /2.5):
            self.users[author_id]["Level"] += 1
            return True
        else:
            return False
          
    async def save(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            with open("cogs/jsonfiles/users.json", "w") as f:
                json.dump(self.users, f, indent=4)
                
            await asyncio.sleep(5)
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("LevelSystem.py is ready")
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.client.user.id:
            return
        
        author_id = str(message.author.id)
        
        if not author_id in self.users:
            self.users[author_id] = {}
            self.users[author_id]["Level"] = 1
            self.users[author_id]["Experience"] = 0
            
        random_exp = random.randint(5,15)
        self.users[author_id]["Experience"] += random_exp
        
        if self.level_up(author_id):
            
            level_up_embed = discord.Embed(title="Woohoo - Level up!", color=discord.Color.green())
            level_up_embed.add_field(name="Congratulations", value=f"{message.author.mention} has just leveled up to level {self.users[author_id]['Level']}!")
            
            await message.channel.send(embed= level_up_embed)
            
    @commands.command()
    async def level(self, ctx, user: discord.User=None):
        if user is None:
            user = ctx.author
        elif user is not None:
            user = user
            
        level_card = discord.Embed(title=f"{user.name}'s Level & Experience", color=discord.Color.random())
        level_card.add_field(name="Level:", value=self.users[str(user.id)]["Level"])
        level_card.add_field(name="Experience:", value=self.users[str(user.id)]["Experience"])
        level_card.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
        
        await ctx.send(embed=level_card)
                
async def setup(client):
    await client.add_cog(LevelSystem(client))