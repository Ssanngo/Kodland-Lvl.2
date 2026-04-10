import discord
import random
from discord.ext import commands
from settings import settings
from tts_module import generate_tts
from bot_login import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix=settings["prefix"],
    intents=intents,
    help_command=None
)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("hi!")


@bot.command()
async def coin(ctx):
    result = random.choice(["heads", "tails"])
    await ctx.send(result)

@bot.command()
async def tts(ctx, *, text):
    await generate_tts(ctx, text)

@bot.command()
async def number(ctx):
    num = random.randint(1, 100)
    await ctx.send(num)

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def help(ctx):
    await ctx.send(
        "```"
        "Commands available:\n"
        "$hello\n"
        "$ping\n"
        "$password\n"
        "$coin\n"
        "$number"
        "```"
    )

@bot.command()
async def password(ctx):
    pass_length = 8
    await ctx.send(gen_pass(pass_length))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Unknown command.\nType $help for a list of commands.")

bot.run(settings["TOKEN"])
