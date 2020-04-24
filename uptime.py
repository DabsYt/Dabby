import discord
from discord.ext import commands
import asyncio
import os

async def keepalive(message):
  for i in range(9999999):
    await message.channel.send("@Dabby[Beta]#3410")
    await asyncio.sleep(5)

bot=commands.Bot(command_prefix="D")

@bot.event
async def on_ready():
  print("Up")

@bot.event
async def on_message(message):
  if(message.content=="botkeepalive"):
      bot.loop.create_task(keepalive(message))
      await message.channel.send("Done!")
      
bot.run(os.getenv("Ttoken"))
