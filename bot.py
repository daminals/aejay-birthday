# bot.py
import os


import discord, random, asyncio
from dotenv import load_dotenv
from discord import Member


load_dotenv()
from discord.ext import commands

bot = commands.Bot(command_prefix='!', description='owo i sure do L-O-V-E programming')
TOKEN = os.environ.get('TOKEN', 3)

@bot.event
async def on_ready():
    bot_channel = bot.get_channel(689168363083268249)
    party = bot.get_emoji(698725283649290310)
    user = bot.get_user(340996105460514816)
    #340996105460514816 - Aejay
    #577668867380477962 - me
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Aejay... Constantly", emoji=party))
    await bot_channel.send('Happy Birthday! 🥳🎉')
    print('bot.py is active')
    while True:
        await bot_channel.send(f'Happy Birthday {user.mention}! 🥳🎉')
        await asyncio.sleep(60*60)



@bot.event
async def on_message(message):
    if message.channel == bot.get_channel(689168363083268249):
        emoji = '🥳'
        emoji2 = '🎉'
        await message.add_reaction(emoji)
        await message.add_reaction(emoji2)
    else:
        if random.randint(0,100)>99:
            emoji = '🥳'
            emoji2 = '🎉'
            await message.add_reaction(emoji)
            await message.add_reaction(emoji2)




@bot.command(hidden=True)
async def load(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')


@bot.command(hidden=True)
async def unload(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.unload_extension(f'cogs.{filename[:-3]}')


@bot.command(hidden=True)
async def reload(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.unload_extension(f'cogs.{filename[:-3]}')
            bot.load_extension(f'cogs.{filename[:-3]}')


bot.run(TOKEN)
