# Based on example https://discordpy.readthedocs.io/en/stable/quickstart.html
import os

import discord
import random
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    technoblade_quotes = [
        'Dude, these orphans are getting destroyed!',
        'This is the second-worst thing to happen to these orphans.',
        'Look, I am an atheist, but when God sends me to Hell I want him to hesitate.',
        'Now, I know what you are gonna say: Technoblade, you monster! You really killed millions of your own kind just to make a sword?',
        'Most opportunities are created by luck. It takes skill to grasp those opportunities and turn it into success.',
    ]
    if message.content == 'technoblade!':
    #if message.content.startswith('$technoblade')
        response = random.choice(technoblade_quotes)
        await message.channel.send(response)
        
    elif message.content == 'pig!':
    #if message.content.startswith('pig'):
        await message.channel.send(file=discord.File(random.choice(('pig1.jpg', 'pig2.jpg', 'pig3.jpg', 'pig4.jpg', 'pig5.jpg'))))

client.run(TOKEN)
