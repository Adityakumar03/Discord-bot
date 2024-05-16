import discord
from discord.ext import commands
from itertools import cycle
import os
import requests
import asyncio
import json

client = commands.Bot(command_prefix =".", intents = discord.Intents.all())
    
client.remove_command("help")

@client.event
async def on_ready():
    await client.tree.sync()
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type = discord.ActivityType.listening, name='Your commands'))    
    print("Success: Bot is ready")
    
    
@client.event
async def on_guild_join(guild):
    with open("cogs/jsonfiles/mutes.json", "r") as f:
        mute_role = json.load(f)
        
        mute_role[str(guild.id)] = None
        
    with open("cogs/jsonfiles/mutes.json", "w") as f:
        json.dump(mute_role, f, indent=4)
        
        
@client.event
async def on_guild_remove(guild):
    with open("cogs/jsonfiles/mutes.json", "r") as f:
        mute_role = json.load(f)
        
        mute_role[str(guild.id)] = None
        
    with open("cogs/jsonfiles/mutes.json", "w") as f:
        json.dump(mute_role, f, indent=4)
    
@client.tree.command(name="ping", description="Shows the bot's latency in ms")
async def ping(interaction: discord.Interaction):
    bot_latency = round(client.latency * 1000)
    await interaction.response.send_message(f"Pong! {bot_latency} ms")
        
async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
            
@client.event
async def on_guild_join(guild):
    with open("cogs/jsonfiles/welcome.json", "r") as f:
        data = json.load(f)
        
    data[str(guild.id)] = {}
    data[str(guild.id)]["Channel"] = None
    data[str(guild.id)]["Message"] = None
    data[str(guild.id)]["Autorole"] = None
    data[str(guild.id)]["ImageUrl"] = None
    

    with open("cogs/jsonfiles/welcome.json", "w") as f:
        json.dump(data, f, indent=4)
        
@client.event
async def on_guild_remove(guild):
    with open("cogs/jsonfiles/welcome.json", "r") as f:
        data = json.load(f)
        
    data.pop(str(guild.id))
    
    with open("cogs/jsonfiles/welcome.json", "w") as f:
        json.dump(data, f, indent=4)

            
async def main():
    async with client:
        await load()
        await client.start("MTIzOTE4NDk1MTAxOTMxMTEzNA.Gh85o9.QBbyX5vL-MtoQjZnwBYntAnsSQEfyT6pXLi5Ew")

asyncio.run(main())
