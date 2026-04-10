from gtts import gTTS
import discord
import os

async def generate_tts(ctx, text):
    filename = "tts.mp3"

    tts = gTTS(text=text, lang="es")  
    # Language Available:
    # https://gtts.readthedocs.io/en/latest/module.html#available-languages
    # Examples:
    # en - English
    # es - Spanish
    # fr - French
    # de - German
    # ja - Japanese
    # ru - Russian

    tts.save(filename)

    await ctx.send(file=discord.File(filename))

    os.remove(filename)  # elimina el archivo después
