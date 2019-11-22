import discord
from discord.ext import commands
import os

class Test(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def info(self, ctx):
        owner = os.getenv("OWNER") 
        version = os.getenv("VERSION") 
        await ctx.send(f"info --> owner: {owner} ; version: {version}")

# Called to setup the extension
def setup(client):
    client.add_cog(Test(client))