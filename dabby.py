import discord
from discord.ext import commands
import platform
import os

bot=commands.Bot(command_prefix="D")
invitelink="https://discordapp.com/api/oauth2/authorize?client_id=694812810068361246&permissions=8&scope=bot"
welcomechannel=694120800063717436
leavechannel=694128777365553232

async def owner(ctx):
	return ctx.author.id==694104161997815880
	
@bot.event
async def on_ready():
	print("Bot is running!")
	game=discord.Game("with bots.")
	await bot.change_presence(status=discord.Status.online,activity=game)
	
@bot.event
async def on_message(message):
	await bot.process_commands(message)
	if(message.author==bot.user):
		return
	elif(bot.user.mentioned_in(message)):
		await message.channel.send("Prefix is D")

@bot.event
async def on_member_join(member):
	channel=discord.utils.get(member.guild.text_channels,id=welcomechannel)
	server=member.guild
	await channel.send(f"{member.name} just joined {server.name}")
	
@bot.event
async def on_member_remove(member):
	channel=discord.utils.get(member.guild.text_channels,id=leavechannel)
	server=member.guild
	await channel.send(f"{member.name} just left {server.name}")
	
@bot.command()
async def ping(ctx):
	pingtime=bot.latency
	await ctx.send(f"Ping is {pingtime}")

@bot.command()
async def add(ctx,a:int,b:int):
	await ctx.send(a+b)
	
@bot.command()
async def sub(ctx,a:int,b:int):
	await ctx.send(a-b)
	
@bot.command()
async def multiply(ctx,a:int,b:int):
	await ctx.send(a*b)
	
@bot.command()
async def divide(ctx,a:int,b:int):
	await ctx.send(a/b)
		
@bot.command()
async def info(ctx,user:discord.User=None):
	if(user):
		name=f"{user.name}"
		id=f"{user.id}"
		e=discord.Embed(color=0x000000)
		e.add_field(name="Name",value=name)
		e.add_field(name="Id",value=id)
		e.set_footer(text="Made by Dabs Yt#6208")
		await ctx.send(embed=e)
	
@bot.command()
async def binfo(ctx):
	pyv=platform.python_version()
	botos=platform.system()
	discordv=discord.__version__
	e=discord.Embed(color=0x000000)
	e.add_field(name="Python version",value=pyv)
	e.add_field(name="OS",value=botos)
	e.add_field(name="Discord version",value=discordv)
	e.set_footer(text="Made by Dabs Yt#6208")
	await ctx.send(embed=e)
	
@bot.command()
async def invite(ctx):
	await ctx.send(invitelink)

@bot.command()
@commands.check(owner)
async def kick(ctx,user:discord.Member=None):
	if(user):
		await ctx.send(f"{user.name} was kicked!")
		await user.kick()
		
@bot.command()
@commands.check(owner)
async def ban(ctx,user:discord.Member=None):
	if(user):
		await ctx.send(f"{user.name} was banned!")
		await user.ban()

@bot.command()
@commands.check(owner)
async def nick(ctx,member:discord.Member,*,name):
	await member.edit(nick=name)
	await ctx.send(f"Renamed {member} to {name}")
	
@bot.command()
async def avatar(ctx,member:discord.Member):
	await ctx.send(member.avatar_url)
	
bot.remove_command("help")
@bot.command()
async def help(ctx):
	e=discord.Embed(color=0x000000)
	e.add_field(name="Dping",value="Shows bot latency")
	e.add_field(name="Dadd {1} {2}",value="Adds 2 numbers")
	e.add_field(name="Dsub {1} {2}",value="Subtracts 2 numbers")
	e.add_field(name="Dmultiply {1} {2}",value="Multiplies 2 numbers")
	e.add_field(name="Ddivide {1} {2}",value="Divides 2 numbers")
	e.add_field(name="Dinfo {user}",value="Shows info about a user")
	e.add_field(name="Dinvite",value="Gives the link to invite this bot")
	e.add_field(name="Dkick {user}",value="Kicks a user")
	e.add_field(name="Dban {user}",value="Bans a user")
	e.add_field(name="Dbinfo",value="Shows bot info")
	e.add_field(name="Dnick {user}",value="Changes the nickname of a user")
	e.add_field(name="Davatar {user}",value="Shows the avatar of a user")
	e.set_footer(text="Made by Dabs Yt#6208")
	await ctx.send(embed=e)

bot.run(os.getenv("Token"))
