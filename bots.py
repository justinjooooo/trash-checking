import discord
from discord.ext import commands
import random
import os
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'You have logged in as {bot.user}')

@bot.command("tebak")
async def tebak(ctx):
    kategori = ["organik", "anorganik"]
    jenis_sampah = random.choice(kategori)

    try:
        nama_images = random.choice(os.listdir(f'sampah/{jenis_sampah}'))
    except FileNotFoundError:
        await ctx.send("Folder gambar tidak ditemukan.")
        return
    
    with open(f'sampah/{jenis_sampah}/{nama_images}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send("Apa jenis sampah ini?", file=picture)
    
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    try:
        msg = await bot.wait_for('message', timeout=30.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send(f"Waktu habis! Jawabannya adalah: {jenis_sampah.upper()}")
        return

    if msg.content.lower() == jenis_sampah.lower():
        await ctx.send("Benar!")
    else:
        await ctx.send(f"Salah! Jawabannya adalah: {jenis_sampah.upper()}")

bot.run("MTI4ODQ4Njc5NTg4MDk1NTk1NQ.GBs0Wb.OhKMV5smzyZCoWTXjh0OAzVKpiLQr5l4uqzNlU")