import discord
import os
from discord.ext import commands


class DiscordBotClient(commands.Bot):
    # startup_extensions = ["cogs.spongebobCommand"]

    properties = {
        'spongebob': True,
    }

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

        for filename in os.listdir('./app/cogs'):
            if filename.endswith('.py') and filename.find('__') == -1:
                self.load_extension(f'app.cogs.{filename[:-3]}')
                print(f"loaded: {filename} ")

    async def on_message(self, message):
        # Check if message not from bot
        if not message.author.bot:
            #  Actions based on plain input
            await self.handle_middleware(message)

            await self.process_commands(message)

    async def handle_middleware(self, message):
        # TODO: Dynamicly add modules here
        if self.properties['spongebob']:
            content = message.content
            anoying_message = ""
            for i in range(0, len(content)):
                if i % 2 == 0:
                    anoying_message += content[i].lower()
                else:
                    anoying_message += content[i].upper()

            await message.channel.send(anoying_message)
