import discord, random,os, requests
from discord.ext import commands
from M1L2 import sifre_uret
from love import whatsstatus

# ayrıcalıklar (intents)
intents = discord.Intents.default()
intents.message_content = True

# bot oluşturma
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} olarak giriş yaptık.")

@bot.command()
async def merhaba(ctx):
    await ctx.send("Selam!")

@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")

@bot.command(name="Sifre")
async def sifre(ctx):
    await ctx.send(sifre_uret())

@bot.command()
async def Random(ctx):
    await ctx.send(random.randint(0, 9))

@bot.command()
async def tekrar(ctx, *, metin):
    await ctx.send(metin)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command(name="love")
async def sifre(ctx):
    await ctx.send(whatsstatus())

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def mem2(ctx):
    liste = os.listdir("images")
    with open(f'images/{random.choice(liste)}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def mem(ctx):
    liste = os.listdir("images")
    with open(f'images/{random.choice(liste)}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def animal(ctx):
    animal_list = os.listdir("images/animal")
    with open(f"images/animal/{random.choice(animal_list)}", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)



bot.run("TOKEN")




