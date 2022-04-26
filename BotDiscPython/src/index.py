from dis import disco
from multiprocessing.sharedctypes import Value
import os
from turtle import color, title
from unicodedata import name
from discord import channel, client, embeds, guild, member, message
from discord.flags import Intents
from discord.utils import get
from dotenv import load_dotenv
import datetime
import time
import excelprueba as excelprueba


import discord
from discord.ext import commands

from urllib import parse, request
import re

import asyncio



load_dotenv()
intents = discord.Intents(messages=True , guilds=True)
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents(members = True)
client = discord.Client(intents = intents)


bot = commands.Bot(command_prefix="q.", description="Bot de ayuda")

@bot.event
async def on_ready():
    print("Listo...")
    await bot.change_presence(activity=discord.Streaming(name="SamFiore", url="http://twitch.tv/bartofiore1"))
    
@client.event
async def on_member_join():
    member = client.get_user()
    #guild_pan = guild.Guild.get_channel(770517288965111829)
    #welcome_channel = client.get_channel(929544918534324336)
    welcome_channel = guild.Guild.get_channel(929544918534324336)
    print (welcome_channel.id)
    await welcome_channel.send(f"Bienvenido {member.mention} a {guild.name}, espero que disfrutes tu estancia aquí. :D")

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
async def febrero(ctx):
    embed = discord.Embed(title="Nota de amor...")
    embed.add_field(name="14 de febrero. Recuerdo en mi alma que siempre fue un día que estuve solo, pero ahora tengo a la llama que prender mi amor.", value="-------")
    embed.add_field(name="Sabes, eres como la luna, pero en el sentido de que me iluminas por las noches más oscuras.", value="---------")
    embed.add_field(name="Eres la persona que aprecio como una obra de arte, no paro de contemplarte.", value="----------")
    embed.add_field(name="Los recuerdos y los momentos, son mi tesoro, pero sobre todo vos sos mi oro.",value="-----------")
    embed.add_field(name="Eres mi día favorito de la semana, o sea, eres el día que siempre espero con ansías.",value="------------")
    embed.add_field(name="La mecanica que me arregla cada día y pone en marcha el motor de mi corazón.", value="-------------")
    embed.set_image(url="https://i.ibb.co/YX5HrCY/Collage-Mamor.jpg")
    embed.add_field(name="""
    ♥♥♥♥♥♥♥
    https://youtu.be/vZqzy9JSB4E
    ♥♥♥♥♥♥♥

    """, value="<3")
    await ctx.send(embed=embed)

@bot.command()
async def definicion(ctx, *, palabra):
#Palabras y definición
    palabra = palabra.lower()
    about = "'Acerca de...', refiere a hablar sobre algo o alguien."
    I = "'Yo', habla de ti mismo."
    yes = "'Sí', aceptación o confirmación de algo."
    arigato_gozaimasu = "'Muchas gracias', forma cortez de agradecer."


    if palabra == "about":
        await ctx.send(about)

    elif palabra == "i":
        await ctx.send(I)

    elif palabra == "yes":
        await ctx.send(yes)

    elif palabra == "arigato gozaimasu" or palabra == "ありがとうございます" :
        await ctx.send(arigato_gozaimasu)

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
    await ctx.send(words)


@bot.command()
async def excel(ctx, msg):
    
    msgE = msg

    def words1(msg3): 
        print (msg3 ,"sended")

    pl1 = words1(msgE)

    #excelprueba.makesheet
    await ctx.send("Ready")





bot.run(TOKEN)
