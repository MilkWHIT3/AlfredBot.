import discord
from discord.ext import commands
import datetime

from urllib import parse, request
import re

bot = commands.Bot(command_prefix='>', description="This is a helper bot")

@bot.command()
async def Hola_Alfred(ctx):
    await ctx.send('¿Cómo se siente hoy, señor Wayne?')
    await ctx.send('¿En qué le puedo servir?')

@bot.command()
async def sum(ctx, NumberOne: int, NumberTwo:int):
    await ctx.send(NumberOne + NumberTwo)

@bot.command()
async def sub(ctx, NumberOne: int, NumberTwo:int):
    await ctx.send(NumberOne - NumberTwo)

@bot.command()
async def multi(ctx, NumberOne: int, NumberTwo:int):
    await ctx.send(NumberOne * NumberTwo)

@bot.command()
async def divi(ctx, NumberOne: int, NumberTwo:int):
    await ctx.send(NumberOne / NumberTwo)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Acerca de mí, señor", timestamp=datetime.datetime.utcnow(), color = discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url="https://i.pinimg.com/originals/05/7a/3f/057a3f6beecb60f6b1f4dc77e2afb617.jpg")
    await ctx.send(embed = embed)

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query':search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    #print(search_results)
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

#Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Tutorials", url="http://www.twitch.tv/milk_whit3"))
    print('My AlfredBot is ready')

bot.run('NzEzNTcwOTgzNzc2MzU0MzU1.XsiDLw.OeCEcL38WJQafCzbtBr2YzfXmpM')
