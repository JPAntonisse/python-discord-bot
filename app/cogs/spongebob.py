import discord
from discord.ext import commands

class Spongebob(commands.Cog):
    active = False
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot == False:
            if self.active == True:
                content = message.content
                anoying_message = ""
                for i in range(0, len(content)):
                    if i % 2 == 0:
                        anoying_message += content[i].lower()
                    else:
                        anoying_message += content[i].upper()

                await message.channel.send(anoying_message)

    @commands.command()
    async def spongebob(self, ctx):
        new_state = not self.active
        self.active = new_state
        
        await ctx.send(f'Spongebob echo talk active: {self.active}')

# Called to setup the extension
def setup(client):
    client.add_cog(Spongebob(client))