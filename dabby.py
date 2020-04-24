import discord
from discord.ext import commands
import asyncio
from time import strftime
from datetime import datetime
import time
import logging
import platform
import string
from random import randint
import random
from urllib.request import urlopen

TOKEN=os.getenv("Token")

bot=commands.Bot(command_prefix="D")

@bot.event
@commands.guild_only()
async def on_message(message):
	if(message.channel.id==697416071593984013):
		await bot.process_commands(message)
	else:
		await message.channel.send("Bot's is beta mode")
		
@bot.command()
async def ping(ctx):
	await ctx.send("Ping!")

bot.run(TOKEN)

"""
!Autorole!
@bot.event
async def on_member_join(member):
	autorole = discord.utils.get(member.server.roles,name="Fan")
	await bot.add_roles(member,autorole)"""
