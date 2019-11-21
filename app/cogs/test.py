import discord
from discord.ext import commands

class Test(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')


# Called to setup the extension
def setup(client):
    client.add_cog(Test(client))