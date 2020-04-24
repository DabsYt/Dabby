import discord
from discord.ext import commands
import asyncio
import os

bot=commands.Bot(command_prefix="D")

@bot.event
async def on_ready():
  print("Up")

@bot.command()
async def keep(ctx,user:discord.Member):
  for i in range(9999999):
    await ctx.send(user.mention)
    await asyncio.sleep(5)

bot.run(os.getenv("Ttoken"))
