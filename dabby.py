import discord
from discord.ext import commands
import asyncio
import os

bot=commands.Bot(command_prefix="D",case_insensitive=True)

#For variables
TOKEN=os.getenv("Token")

#On message
@bot.event
@commands.guild_only() #No dms
async def on_message(message):
    channel=message.channel
    if(message.author==bot.user):
        return
    elif(message.channel.id==697416071593984013):
        await bot.process_commands(message)
    elif(message.content.startswith=="D"):
        await channel.send("```Bot's in test mode right now,try again later.```")

#Latency
@bot.command()
async def ping(ctx):
	timesent=get_time
	pingtime=round(bot.latency,1)
	e=discord.Embed(color=0x55edc2)
	e.add_field(name="Latency",value=f"{pingtime}ms")
	e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
	await ctx.send(embed=e)

bot.remove_command("help")
@bot.command()
async def help(ctx):
	timesent=get_time
	e=discord.Embed(title="Help for Dabby",color=0x55edc2)
	e.add_field(name="Dbinfo",value="Shows bot info")
	e.add_field(name="Dping",value="Shows bot latency")
	e.add_field(name="Dadd {1} {2}",value="Adds 2 numbers")
	e.add_field(name="Dsub {1} {2}",value="Subtracts 2 numbers")
	e.add_field(name="Dmultiply {1} {2}",value="Multiplies 2 numbers")
	e.add_field(name="Ddivide {1} {2}",value="Divides 2 numbers")
	e.add_field(name="Dinfo {user}",value="Shows info about a user")
	e.add_field(name="Dinvite",value="Gives the link to invite this bot")
	e.add_field(name="Dpick {min} {max}",value="Picks a random number between min,max")
	e.add_field(name="Dgen {length}",value="Generates a string in the desired length")
	e.add_field(name="Dsource",value="Shows bot source code link")
	#e.add_field(name="Dreact {emoji}",value="Waits for your reaction with an emoji")
	e.add_field(name="Drepeat {times=<5} {text=<30}",value="Repeats a message with a desired text")
	e.add_field(name="Dversion",value="Shows current and online version")
	e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
	await ctx.send(embed=e)

bot.run(TOKEN)
