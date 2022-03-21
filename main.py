# bot.py
import os

import discord
from dotenv import load_dotenv
from bot import jv_bot

load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']
GUILD = os.environ['SERVER_NAME']

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #print(message)
    try:
      if message.content:
          await jv_bot.process_text_message(message,client)
      elif message.content == 'raise-exception':
          raise discord.DiscordException
    except Exception as e:
      jv_bot.process_exception(client.user, message.author, message.content, e)

client.run(TOKEN)
