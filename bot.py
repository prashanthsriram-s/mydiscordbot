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
        '''When the bot establishes connection and becomes online'''
        guild = client.guilds[0]
        print(f'{client.user} is now connected and running!')
        print(f'I have connected to {guild.name}!')
        

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return # To prevent bot replying to itself
        

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said {user_message} in guild {channel}')
        if user_message[0] == '!':
            await send_message(message=message, user_message=user_message[1:])

        
    
    client.run(TOKEN)

    



