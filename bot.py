import discord
import os
from dotenv import load_dotenv
from responses import generate_response

async def send_message(message, user_message):
    try:
        response = generate_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now connected and running!')

    client.run(TOKEN)
    

