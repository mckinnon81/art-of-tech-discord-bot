import discord
import os
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if (message.content.startswith('$hello')):
        await message.channel.send('Hello!')

@client.event
async def on_member_join(member):
        default_role = discord.utils.get(member.guild.roles, id=907235072682389554)
        message.user.send('Welcome!')
        await member.add_roles(default_role)


client.run(os.getenv('TOKEN'))
