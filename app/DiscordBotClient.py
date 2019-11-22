import discord
import os
from discord.ext import commands


class DiscordBotClient(commands.Bot):
    channel_name_to_channel_dict = {}

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        self.init()
        await self.send_welcome_message()

    async def on_message(self, message):
        if not message.author.bot:
            await self.process_commands(message)

    def init(self):
        self.map_channels_to_dict()
        self.import_extensions()
        
    def map_channels_to_dict(self):
        channels = self.get_all_channels()
        for channel in channels:
            self.channel_name_to_channel_dict[channel.name] = channel

    def import_extensions(self):
        for filename in os.listdir('./app/cogs'):
            if filename.endswith('.py') and filename.find('__') == -1:
                self.load_extension(f'app.cogs.{filename[:-3]}')
                print(f"loaded: {filename} ")

    async def send_welcome_message(self):
            owner = os.getenv('OWNER')
            version = os.getenv('VERSION')
            channel = self.channel_name_to_channel_dict['bot-requests']
            
            await channel.send(f"HALLO DAAR BEN IK WEER! (Instance owner: {owner}, version: {version})")
            