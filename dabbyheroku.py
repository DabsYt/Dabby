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

bot=commands.Bot(command_prefix="D")
invitelink="https://discordapp.com/api/oauth2/authorize?client_id=694812810068361246&permissions=8&scope=bot"
TOKEN=os.getenv("Token")
start=time.time()
v=discord.__version__
#vi=discord.version_info same as v
pyv=platform.python_version()
osc=platform.system()
#Log everything
logger=logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler=logging.FileHandler(filename="dabby-log.txt",encoding="utf-8",mode="a")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s"))
logger.addHandler(handler)

#Dont use global bot specific classes here cuz it isnt ready yet(use only for locally available vars like 'pyv'')
#TOKEN=os.getenv("Token")

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
	
@bot.event
async def on_ready():
	timeup=strftime("%d/%m/%Y %H:%M:%S")
	print("|---------------|")
	print(f"|Discord version:{v}|")
	print("|Bot is running!|")
	print(f"|Bot name: {bot.user}|")
	print(f"|Guilds:{len(list(bot.guilds))}|")
	for guild in bot.guilds:
		print(f"|Guild:{guild.name}|Members:{guild.member_count}|")
	print(f"|Users:{str(len(set(bot.get_all_members())))}|")
	bot.loop.create_task(status())

@bot.command()
async def binfo(ctx):
	timesent=strftime("%d/%m/%Y %H:%M:%S")
	e=discord.Embed(title="Bot Info",color=0x55edc2)
	e.add_field(name="Discord version",value=v)
	e.add_field(name="OS",value=osc)
	e.add_field(name="Python version",value=pyv)
	e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
	await ctx.send(embed=e)
	
@bot.command()
async def ping(ctx):
	timesent=strftime("%d/%m/%Y %H:%M:%S")
	pingtime=bot.latency
	e=discord.Embed(color=0x55edc2)
	e.add_field(name="Latency",value=pingtime)
	e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
	await ctx.send(embed=e)

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

@bot.command()
async def invite(ctx):
	timesent=strftime("%d/%m/%Y %H:%M:%S")
	e=discord.Embed(color=0x55edc2)
	e.add_field(name="Invite me using this link",value=invitelink)
	e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
	await ctx.send(embed=e)

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

@bot.command()
async def gen(ctx,n:int=None):
  if(n):
    sel=string.ascii_letters+string.digits
    gent= ''.join(random.choice(sel)for i in range(n))
    timesent=strftime("%d/%m/%Y %H:%M:%S")
    e=discord.Embed(title=gent,color=0x55edc2)
    e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
    await ctx.send(embed=e)
  else:
  	await ctx.send("Dgen **{length}**")

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
	e.add_field(name="Dgen {length}",value="Generates a string in the desired length")
	e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
	await ctx.send(embed=e)

bot.run(TOKEN)

"""
!Autorole!
@bot.event
async def on_member_join(member):
	autorole = discord.utils.get(member.server.roles,name="Fan")
	await bot.add_roles(member,autorole)"""