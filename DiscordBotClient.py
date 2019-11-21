import discord
import os
from discord.ext import commands

class DiscordBotClient(commands.Bot):
    
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                
                self.load_extension(f'cogs.{filename[:-3]}')
                print(f"loaded: {filename} ")


    async def on_message(self, message):
        # Check if message not from bot
        if message.author.bot == False:
            #  Actions based on plain input
            # await self.handle_middleware(message)

            await self.process_commands(message)
