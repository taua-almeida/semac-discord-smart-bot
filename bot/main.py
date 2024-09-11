import discord
from discord.ext import commands
import httpx

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

HF_API_KEY = "d"
API_URL = ""
BOT_TOKEN = ""

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


async def query_hf_model(query):
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    data = {"inputs": query, "wait_for_model": True}

    async with httpx.AsyncClient() as client:
        response = await client.post(API_URL, headers=headers, json=data, timeout=60.0)
        try:
            generated_text = response.json()[0]['generated_text']
            return generated_text
        except (KeyError, IndexError):
            return "Não consegui gerar uma resposta válida."
        
@bot.command()
async def ask(ctx, *, question):
    response = await query_hf_model(question)
    await ctx.send(response)


bot.run("")
