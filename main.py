import discord
import ezcord
import json

bot = ezcord.Bot(intents=discord.Intents.default(),
                 activity=discord.CustomActivity(name="💻 Template by copyandbuild/Larrox"),debug_guilds=["YOUR_GUILD_ID"])

with open('token.json', 'r') as f:
    data = json.load(f)
    TOKEN = data['TOKEN']

bot.load_cogs()
bot.run(TOKEN)
