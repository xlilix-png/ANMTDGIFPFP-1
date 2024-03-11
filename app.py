import discord
import asyncio
import replicate

intents = discord.Intents.all()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

    try:
        with open('avatar.gif', 'rb') as avatar:
            await client.user.edit(avatar=avatar.read())
        print('Animated avatar uploaded successfully!')
    except Exception as e:
        print('Failed to upload animated avatar:', e)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('&hey'):
        await message.channel.send('Hey, the  code is working fine')

DISCORD_BOT_TOKEN = 'TOKEN'

client.run(DISCORD_BOT_TOKEN)
