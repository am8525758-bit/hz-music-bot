import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

# 1. Web server-er code (24/7 active rakhar jonno)
app = Flask('')

@app.route('/')
def home():
    return "Bot is running 24/7!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# 2. Discord Bot Setup
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} online hoye geche!")

# Apnar onnanno music ba bot-er command ba code ekhane thakbe

# 3. Bot Run korar age keep_alive() call kora
keep_alive()

# 4. Ekhane apnar bot token-ti boshan (ba render er environment variable use korte paren)
bot.run("APNAR_BOT_TOKEN_EKHANE_DIN")
