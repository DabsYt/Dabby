import discord
import asyncio
from discord.ext import commands
from time import strftime,localtime
from datetime import datetime
import time
import logging
import platform
import string
from random import randint
import os
import random
from urllib.request import urlopen

bot=commands.Bot(command_prefix="D",case_insensitive=True)

#For global variables
TOKEN=os.getenv("Token")
online_v="https://raw.githubusercontent.com/DabsYt/Dabby/master/version"
bot_v="0.1.0"
#TOKEN=os.getenv("Token")

#For definitions
async def status():
	while True:
		for x in range(9999999):
			await bot.change_presence(status=discord.Status.online,activity=discord.Game("Made by Dabs Yt#6208"))
			await asyncio.sleep(15)
			await bot.change_presence(status=discord.Status.online,activity=discord.Game(f"Serving {len(list(bot.guilds))} servers!"))
			await asyncio.sleep(15)
			await bot.change_presence(status=discord.Status.online,activity=discord.Game(f"Serving {str(len(set(bot.get_all_members())))} users!"))
			now=time.time()
			secs=int(now-start)
			mins=int(secs//60)
			await bot.change_presence(status=discord.Status.online,activity=discord.Game(f"Uptime is {mins} minutes!"))
			await asyncio.sleep(15)
	
#For misc
pyv=platform.python_version()
osc=platform.system()
v=discord.__version__

#For logging in file
logger=logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler=logging.FileHandler(filename="dabby-log.txt",encoding="utf-8",mode="a")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s"))
logger.addHandler(handler)

#For getting start of uptime
start=time.time()
	
#For source code on github
sourcelink="https://github.com/DabsYt/Dabby/blob/master/dabby.py"
sourcebetalink="https://github.com/DabsYt/Dabby/blob/master/dabby-beta.py"

#For invite
invitelink="https://discordapp.com/api/oauth2/authorize?client_id=694812810068361246&permissions=8&scope=bot"

#For version
versionlink="https://github.com/DabsYt/Dabby/blob/master/version"

#For creating remote embed
"""def c_embed(titlet:str=None,fields:int=None):
	if(titlet):
		if(fields):
			timesent=strftime("%d/%m/%Y %H:%M:%S")
		  e=discord.Embed(title=titlet,color=0x55edc2)
		  for i in range()
		  e.add_field(name=,value=a*b)
		  e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
		  await ctx.send(embed=e)"""
	
#On ready
@bot.event
async def on_ready():
	timeup=strftime("%d/%m/%Y %H:%M:%S")
	print("|---------------|")
	print("|Bot is running!|")
	print(f"|Discord version: {v}|")
	print(f"|Bot name: {bot.user}|")
	print(f"|Guilds: {len(list(bot.guilds))}|")
	for guild in bot.guilds:
		print(f"|Guild: {guild.name}|Members: {guild.member_count}|")
	print(f"|Users: {str(len(set(bot.get_all_members())))}|")
	#Create presence loop
	bot.loop.create_task(status())
 
#Bot info
@bot.command()
async def binfo(ctx):
	timesent=strftime("%d/%m/%Y %H:%M:%S")
	e=discord.Embed(title="Bot Info",color=0x55edc2)
	e.add_field(name="Discord version",value=v)
	e.add_field(name="OS",value=osc)
	e.add_field(name="Python version",value=pyv)
	e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
	await ctx.send(embed=e)
	
#Latency
@bot.command()
async def ping(ctx):
	timesent=strftime("%d/%m/%Y %H:%M:%S")
	pingtime=bot.latency
	e=discord.Embed(color=0x55edc2)
	e.add_field(name="Latency",value=pingtime)
	e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
	await ctx.send(embed=e)
 
#Add
@bot.command()
async def add(ctx,a:int,b:int):
	if(a):
		if(b):
			timesent=strftime("%d/%m/%Y %H:%M:%S")
			e=discord.Embed(color=0x55edc2)
			e.add_field(name="Result",value=a+b)
			e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
			await ctx.send(embed=e)
		else:
			await ctx.send("Dadd {a} **{b}**")
	else:
		await ctx.send("Dadd **{a}** {b}")
	
#Subtract
@bot.command()
async def sub(ctx,a:int,b:int):
	if(a):
		if(b):
			timesent=strftime("%d/%m/%Y %H:%M:%S")
			e=discord.Embed(color=0x55edc2)
			e.add_field(name="Result",value=a-b)
			e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
			await ctx.send(embed=e)
		else:
			await ctx.send("Dsub {a} **{b}**")
	else:
		await ctx.send("Dsub **{a}** {b}")
	
#Multiply
@bot.command()
async def multiply(ctx,a:int,b:int):
	if(a):
		if(b):
			timesent=strftime("%d/%m/%Y %H:%M:%S")
			e=discord.Embed(color=0x55edc2)
			e.add_field(name="Result",value=a*b)
			e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
			await ctx.send(embed=e)
		else:
			await ctx.send("Dmultiply {a} **{b}**")
	else:
		await ctx.send("Dmultiply **{a}** {b}")
	
#Divide
@bot.command()
async def divide(ctx,a:int,b:int):
	if(a):
		if(b):
			timesent=strftime("%d/%m/%Y %H:%M:%S")
			e=discord.Embed(color=0x55edc2)
			e.add_field(name="Result",value=a/b)
			e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
			await ctx.send(embed=e)
		else:
			await ctx.send("Ddivide {a} **{b}**")
	else:
		await ctx.send("Ddivide **{a}** {b}")
		
#User info
@bot.command()
async def info(ctx,user:discord.User=None):
	if(user):
		timesent=strftime("%d/%m/%Y %H:%M:%S")
		name=f"{user.name}"
		id=f"{user.id}"
		e=discord.Embed(title=f"Info for {user.name}",color=0x55edc2)
		e.add_field(name="Name",value=name)
		e.add_field(name="Id",value=id)
		e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
		await ctx.send(embed=e)
	else:
		await ctx.send("Dinfo **{user}**")
 
#Invite link
@bot.command()
async def invite(ctx):
	timesent=strftime("%d/%m/%Y %H:%M:%S")
	e=discord.Embed(color=0x55edc2)
	e.add_field(name="Invite the basic version using this link",value=invitelink)
	e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
	await ctx.send(embed=e)
 
#Pick number
@bot.command()
async def pick(ctx,min:int=None,max:int=None):
	if(min):
		if(max):
			pickres=randint(min,max)
			timesent=strftime("%d/%m/%Y %H:%M:%S")
			e=discord.Embed(color=0x55edc2)
			e.add_field(name="Picked",value=pickres)
			e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
			await ctx.send(embed=e)
		else:
			await ctx.send("Dpick {min} **{max}**")
	else:
		await ctx.send("Dpick **{min}** {max}")
 
#Generate string
@bot.command()
async def gen(ctx,n:int=None):
  if(n and n<=100):
    sel=string.ascii_letters+string.digits
    gent= ''.join(random.choice(sel)for i in range(n))
    timesent=strftime("%d/%m/%Y %H:%M:%S")
    e=discord.Embed(title=gent,color=0x55edc2)
    e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
    await ctx.send(embed=e)
  else:
  	await ctx.send("Dgen **{length<=100}**")
 
#Source code link
@bot.command()
async def source(ctx):
	timesent=strftime("%d/%m/%Y %H:%M:%S")
	e=discord.Embed(color=0x55edc2)
	e.add_field(name="Get the bot's code here",value=sourcelink)
	e.add_field(name="Get the bot's beta code here",value=sourcebetalink)
	e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
	await ctx.send(embed=e)
 
#Get version
@bot.command()
async def version(ctx):
	async def get_v():
		online_v=urlopen("https://raw.githubusercontent.com/DabsYt/Dabby/master/version")
		latest=str(online_v.read()).replace("b","").replace("'","")
		timesent=strftime("%d/%m/%Y %H:%M:%S")
		if(int(latest.replace(".",""))>int(bot_v.replace(".",""))):
			titlet="Update is available online"
		else:
			titlet="Bot is up to date"
		e=discord.Embed(title=titlet,color=0x55edc2)
		e.add_field(name="Online version",value=latest)
		e.add_field(name="Bot version",value=bot_v)
		e.add_field(name="Version got from here",value=versionlink)
		e.add_field(name="You can use early versions here by downloading the beta version",value="https://github.com/DabsYt/Dabby/blob/master/dabby-beta.py")
		e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
		await ctx.send(embed=e)
	await get_v()

bot.remove_command("help")
@bot.command()
async def help(ctx):
	timesent=strftime("%d/%m/%Y %H:%M:%S")
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
	e.add_field(name="Dgen {length<=100}",value="Generates a string in the desired length")
	e.add_field(name="Dsource",value="Shows bot source code link")
	e.add_field(name="Dversion",value="Shows current and online version")
	e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
	await ctx.send(embed=e)
 
bot.run(TOKEN)
 
"""
!Autorole!
@bot.event
async def on_member_join(member):
	autorole = discord.utils.get(member.server.roles,name="Fan")
	await bot.add_roles(member,autorole)"""
