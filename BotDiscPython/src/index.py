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


bot = commands.Bot(command_prefix="q.", description="help bot")

@bot.event
async def on_ready():
    print("Ready...")
    await bot.change_presence(activity=discord.Streaming(name="twitch", url="twitchchannel")) #-> Here you add you twitch.
    
@client.event
async def on_member_join():
    member = client.get_user()
    #guild_pan = guild.Guild.get_channel(770517288965111829)
    #welcome_channel = client.get_channel(929544918534324336)
    welcome_channel = guild.Guild.get_channel(929544918534324336)
    print (welcome_channel.id)
    await welcome_channel.send(f"Welcome {member.mention} to {guild.name}, i hope you like my discord server. Thx u for enjoy :D")

#this command is used to calculate the ping, but below is a better one
@bot.command()
async def ping(ctx):
    await ctx.send("pong")

#this command i use to test, just repite words.
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

 #Search in youtube
@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({"search_query": search})
    html_content = request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall('watch\?v=(.{11})',html_content.read().decode('utf-8'))
    print(search_results)
    await ctx.send("https://www.youtube.com/watch?v=" + search_results[0])

# here be the server info    
@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Hello", timestamp=datetime.datetime.utcnow(), color=discord.Color.dark_red())
    embed.add_field(name="The server was created in", value=f"{ctx.guild.created_at}")
    embed.add_field(name="There a total of", value=f"{ctx.guild.owner}", "members")
    embed.add_field(name="", value=f"{ctx.guild.member_count}")
    embed.add_field(name="The region is", value=f"{ctx.guild.region}")
    embed.add_field(name="The ID server is", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url="http://www.malagana.net/wp-content/uploads/2015/03/internet-explorer-windows-10.png")
    await ctx.send(embed=embed)

#Here is the important of bot, this is a dictionary to help students find word and their definition. It is en development
@bot.command()
async def definicion(ctx, *, word):
#Palabras y definición
    word = word.lower()
    about = "'Acerca de...', refiere a hablar sobre algo o alguien."
    I = "'Yo', habla de ti mismo."
    yes = "'Sí', aceptación o confirmación de algo."
    arigato_gozaimasu = "'Muchas gracias', forma cortez de agradecer."


    if word == "about":
        await ctx.send(about)

    elif word == "i":
        await ctx.send(I)

    elif word == "yes":
        await ctx.send(yes)

    elif word == "arigato gozaimasu" or word == "ありがとうございます" :
        await ctx.send(arigato_gozaimasu)

    else :
        await ctx.send("The word is incorrect")

 #Replace messages 
@bot.command()
async def replace(ctx):
    message_replace = await ctx.send("Replacing...")
    time.sleep(2)
    await message_replace.edit(content="this messages was replace.")

# This command use to show the ping in ms
@bot.command()
async def pingms(ctx):
    before = time.monotonic()
    pong = "pong"
    response = await ctx.send(pong)
    pingA = (time.monotonic() -before)*1000 
    pingB = (str(pingA).split("."))[0]
    await response.edit(content=pong +" (" + pingB + "ms)")

#Repeat what you wrote, this repeat sentences
@bot.command()
async def repite(ctx, *, words):
    await ctx.send(words)

#This command does not work, i working in it
@bot.command()
async def excel(ctx, msg):
    
    msgE = msg

    def words1(msg3): 
        print (msg3 ,"sended")

    pl1 = words1(msgE)

    #excelprueba.makesheet
    await ctx.send("Ready")





bot.run(TOKEN)
