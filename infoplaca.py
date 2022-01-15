import discord
from discord.ext import commands
import requests
import json
import time
 
 
bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help
 


@bot.command()
async def infoplaca(ctx, *, placa):
    async with ctx.typing():
        response = requests.get(f"https://api.habtium.es/v1/badges/info/{placa}")
        placa = response.json()['data']['results']['es']['name'][0]['text']
    try:

        descripcion = response.json()['data']['results']['es']['description'][0]['text']
    except KeyError:
        descripcion="No tiene descripción"
    try:

        codigo = response.json()['data']['code']
    except UnboundLocalError:
        codigo=""   
       
    embed = discord.Embed(title="", description="•Nombre🡺" + f"{placa}" + "\n\n•Descripcion🡺" + f"{descripcion}" + "\n\n•Codigo🡺" f"{codigo.upper()}")
    embed.set_thumbnail(url="https://images.habbo.com/c_images/album1584/" f"{codigo.upper()}.png")
    await ctx.send("buscando...", delete_after=0)
    time.sleep(6)
    await ctx.message.delete()

    
   
    
    await ctx.send(embed=embed)

    
    
   
    
    
 
 
 
@bot.event
async def on_ready():
    activity = discord.Game(name="info placa", type=1)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("BOT listo!")

bot.run('') #OBTEN UN TOKEN EN: https://discord.com/developers/applications    
