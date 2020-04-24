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

#Definitions
def get_time():
    return strftime("&d/%m/%Y %H:%M:%S")

def format(text):
    return text.get_time

"""def get_prefix(bot,message):
    with open("prefixes.json","r") as f:
        prefixes=json.load(f)
        prefix=prefixes[str(message.guild.id)]
        return prefix"""

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

bot=commands.Bot(command_prefix="D",case_insensitive=True)

#For variables
TOKEN=os.getenv("Token")
online_v="https://raw.githubusercontent.com/DabsYt/Dabby/master/version"
bot_v="0.1.1"
#TOKEN=os.getenv("Token")
pyv=platform.python_version()
osc=platform.system()
v=discord.__version__
start=time.time()
sourcelink="https://github.com/DabsYt/Dabby"
invitelink="https://discordapp.com/api/oauth2/authorize?client_id=701374856247246888&permissions=8&scope=bot"
versionlink="https://github.com/DabsYt/Dabby/blob/master/version"

#For logging(disabled since 10 runs>=8mb)
"""logger=logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler=logging.FileHandler(filename="dabby-log.txt",encoding="utf-8",mode="a")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s"))
logger.addHandler(handler)"""

#On ready
@bot.event
async def on_ready():
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

#On message
@bot.event
@commands.guild_only() #No dms
async def on_message(message):
    channel=message.channel
    if(message.author==bot.user):
        return
    elif(message.channel.id==697416071593984013):
        await bot.process_commands(message)
    else:
        await channel.send("```Bot's in test mode right now,try again later.```")

#Bot info
@bot.command()
async def binfo(ctx):
	timesent=get_time
	e=discord.Embed(title="Bot Info",color=0x55edc2)
	e.add_field(name="Servers",value=len(list(bot.guilds)))
	e.add_field(name="Members",value=str(len(set(bot.get_all_members()))))
	e.add_field(name="Discord version",value=v)
	e.add_field(name="OS",value=osc)
	e.add_field(name="Python version",value=pyv)
	e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
	await ctx.send(embed=e)

#Latency
@bot.command()
async def ping(ctx):
	timesent=get_time
	pingtime=round(bot.latency,1)
	e=discord.Embed(color=0x55edc2)
	e.add_field(name="Latency",value=f"{pingtime}ms")
	e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
	await ctx.send(embed=e)

#Add
@bot.command()
async def add(ctx,a:int,b:int):
	if(a):
		if(b):
			timesent=get_time
			e=discord.Embed(color=0x55edc2)
			e.add_field(name="Result",value=a+b)
			e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
			await ctx.send(embed=e)
		else:
			await ctx.send("```Dadd {a} **{b}**```")
	else:
		await ctx.send("```Dadd **{a}** {b}```")

#Subtract
@bot.command()
async def sub(ctx,a:int,b:int):
	if(a):
		if(b):
			timesent=get_time
			e=discord.Embed(color=0x55edc2)
			e.add_field(name="Result",value=a-b)
			e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
			await ctx.send(embed=e)
		else:
			await ctx.send("```Dsub {a} **{b}**```")
	else:
		await ctx.send("```Dsub **{a}** {b}```")

#Multiply
@bot.command()
async def multiply(ctx,a:int,b:int):
	if(a):
		if(b):
			timesent=get_time
			e=discord.Embed(color=0x55edc2)
			e.add_field(name="Result",value=a*b)
			e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
			await ctx.send(embed=e)
		else:
			await ctx.send("```Dmultiply {a} **{b}**```")
	else:
		await ctx.send("```Dmultiply **{a}** {b}```")

#Divide
@bot.command()
async def divide(ctx,a:int,b:int):
	if(a):
		if(b):
			timesent=get_time
			e=discord.Embed(color=0x55edc2)
			e.add_field(name="Result",value=a/b)
			e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
			await ctx.send(embed=e)
		else:
			await ctx.send("```Ddivide {a} **{b}**```")
	else:
		await ctx.send("```Ddivide **{a}** {b}```")

#User info
@bot.command()
async def info(ctx,user:discord.Member=None):
    if(user):
        name=user.name
        id=user.id
        joined=format(user.joined_at)
        created=format(user.created_at)
        e=discord.Embed(title=f"Info for {name}",color=0x55edc2)
        e.add_field(name="Name",value=name)
        e.add_field(name="Id",value=id)
        e.add_field(name="Joined at",value=joined)
        e.add_field(name="Created at",value=created)
        e.set_footer(text="Sent at {timesent} for {ctx.author.name}")
    else:
        await ctx.send("```Dinfo **{user}**```")

#Invite link
@bot.command()
async def invite(ctx):
	timesent=get_time
	e=discord.Embed(color=0x55edc2)
	e.add_field(name="Invite the beta version using this link",value=invitelink)
	e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
	await ctx.send(embed=e)

#Pick number
@bot.command()
async def pick(ctx,min:int=None,max:int=None):
	if(min):
		if(max):
			pickres=randint(min,max)
			timesent=get_time
			e=discord.Embed(color=0x55edc2)
			e.add_field(name="Picked",value=pickres)
			e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
			await ctx.send(embed=e)
		else:
			await ctx.send("```Dpick {min} **{max}**```")
	else:
		await ctx.send("```Dpick **{min}** {max}```")

#Generate string
@bot.command()
async def gen(ctx,n:int=None):
  if(n and n>0 and n<=100):
    sel=string.ascii_letters+string.digits
    gent= ''.join(random.choice(sel)for i in range(n))
    timesent=get_time
    e=discord.Embed(title=gent,color=0x55edc2)
    e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
    await ctx.send(embed=e)
  else:
  	await ctx.send("```Dgen **{length<=100}**```")

#Source code link
@bot.command()
async def source(ctx):
	timesent=get_time
	e=discord.Embed(color=0x55edc2)
	e.add_field(name="Get the bot's code here",value=sourcelink)
	e.set_footer(text=f"Sent at {timesent} for {ctx.author.name}")
	await ctx.send(embed=e)

#Get reaction
"""@bot.command()
async def react(ctx):
	msg=await ctx.send("React with: 👍")
	def check(reaction,user):
		return user==ctx.author and str(reaction.emoji)=="👍"
	try:
		reaction,user=await bot.wait_for("reaction_add",timeout=10.0,check=check)
	except asyncio.TimeoutError:
		await ctx.send("Didnt react :(")
	else:
		await ctx.send("Reacted :) good boi")"""

#Repeat
@bot.command()
@commands.is_owner()
async def repeat(ctx,t:int=None,*,txt:str=None):
	if(t and t>0 and t<=5):
		if(txt and len(txt)<=30):
			for i in range(t):
				await ctx.send(txt)
		else:
			await ctx.send("```Drepeat {times=<5} **{text=<30}**```")
	else:
		await ctx.send("```Drepeat **{times=<5}** {text=<30}```")

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

bot.run(TOKEN,reconnect=True)

"""
!Autorole!
@bot.event
async def on_member_join(member):
	autorole = discord.utils.get(member.server.roles,name="Fan")
	await bot.add_roles(member,autorole)"""
