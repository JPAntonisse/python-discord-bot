import discord
from discord.ext import commands

class DiscordBotClient(commands.Bot):
    # startup_extensions = ["cogs.spongebobCommand"]

    properties = {
        'spongebob' : True,
    }

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

        # for extension in self.startup_extensions:
        #     try:
        #         self.load_extension(extension)
        #     except Exception as e:
        #         exc = '{}: {}'.format(type(e).__name__, e)
        #         print('Failed to load extension {}\n{}'.format(extension, exc))

    async def on_message(self, message):
        # Check if message not from bot
        if message.author.bot == False:
            #  Actions based on plain input
            await self.handle_middleware(message)

            await self.process_commands(message)

    async def handle_middleware(self, message):
        # TODO: Dynamicly add modules here
        if self.properties['spongebob'] == True:
            content = message.content
            anoying_message = ""
            for i in range(0, len(content)):
                if i % 2 == 0:
                    anoying_message += content[i].lower()
                else:
                    anoying_message += content[i].upper()

            await message.channel.send(anoying_message)
                
