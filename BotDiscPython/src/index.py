import os
from discord import embeds
from dotenv import load_dotenv
import datetime
import time

import discord
from discord.ext import commands

from urllib import parse, request
import re



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="q.", description="Bot de ayuda")

@bot.event
async def on_ready():
    print("Listo...")
    await bot.change_presence(activity=discord.Streaming(name="SamFiore", url="http://twitch.tv/bartofiore1"))
    

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({"search_query": search})
    html_content = request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall('watch\?v=(.{11})',html_content.read().decode('utf-8'))
    print(search_results)
    await ctx.send("https://www.youtube.com/watch?v=" + search_results[0])

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Hola", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_red())
    embed.add_field(name="El server fue creado en", value=f"{ctx.guild.created_at}")
    embed.add_field(name="El dueño es", value=f"{ctx.guild.owner}")
    embed.add_field(name="Hay un total de", value=f"{ctx.guild.member_count}")
    embed.add_field(name="La región es", value=f"{ctx.guild.region}")
    embed.add_field(name="La ID del server es", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url="http://www.malagana.net/wp-content/uploads/2015/03/internet-explorer-windows-10.png")
    await ctx.send(embed=embed)

@bot.command()
async def definicion(ctx, palabra):
#Palabras y definición
    about = "'Acerca de...', refiere a hablar sobre algo o alguien."
    I = "'Yo', habla de ti mismo"

    if palabra == "about" or palabra == "About":
        await ctx.send(about)

    elif palabra == "I" or palabra == "i":
        await ctx.send(I)

    else :
        await ctx.send("La palabra es incorrecta o no existe")

@bot.command()
async def replace(ctx):
    mensaje_remplazado = await ctx.send("Remplazando este mensaje...")
    time.sleep(2)
    await mensaje_remplazado.edit(content="El mensaje ha sido remplazado.")

@bot.command()
async def pingms(ctx):
    before = time.monotonic()
    pong = "pong"
    response = await ctx.send(pong)
    pingA = (time.monotonic() -before)*1000 
    pingB = (str(pingA).split("."))[0]
    await response.edit(content=pong +" (" + pingB + "ms)")

@bot.command()
async def repite(ctx, *, palabras):
    await ctx.send(palabras)

bot.run(TOKEN)