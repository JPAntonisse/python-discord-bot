from app.DiscordBotClient import DiscordBotClient
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("TOKEN")

client = DiscordBotClient(command_prefix = "$")

client.run(token)

