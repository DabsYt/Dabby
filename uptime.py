import discord
from discord.ext import commands
import asyncio
import os

async def keepalive(user,message):
 while True:
  for i in range(9999999):
    await message.channel.send(user.mention)
    await asyncio.sleep(5)

bot=commands.Bot(command_prefix="D")

@bot.event
async def on_ready():
  print("Up")

@bot.command()
async def keep(ctx,user:discord.Member):
  bot.loop.create_task(user,ctx.message)
  await ctx.send("Done!")

bot.run(os.getenv("Ttoken"))
