import discord
from bot_logic import gen_pass
from bot_logic import flip_coin
from bot_logic import gen_emodji
from bot_logic import add

# la variabile indents contiene i permessi al bot
intents = discord.Intents.default()
# abilita il permesso a leggere i contenuti dei messaggi
intents.message_content = True
# crea un bot e passa gli indents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$ciao'):
        await message.channel.send("Ciao!")
    elif message.content.startswith('$arrivederci'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$smile'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$password'):
        await message.channel.send("La tua password " + gen_pass(30))
    elif message.content.startswith('$add'):
        try:
            _, left, right = message.content.split()
            left = int(left)
            right = int(right)
            result = left + right
            await message.channel.send(f"Il risultato di {left} + {right} è: {result}")
        except ValueError:
            await message.channel.send("Per favore, inserisci due numeri interi dopo il comando $add.")
    elif message.content.startswith('$comandi'):
        await message.channel.send("""**I comandi disponibili sono:**
                - Lancio moneta: `$coin`
                - Genera password: `$password`
                - Emoji casuale: `$smile`
                - Benvenuto: `$ciao`
                - Arrivederci: `$arrivederci`""")
    else:
        await message.channel.send("""**Comando non riconosciuto. I comandi disponibili sono:**
                - Lancio moneta: `$coin`
                - Genera password: `$password`
                - Emoji casuale: `$smile`
                - Benvenuto: `$ciao`
                - Arrivederci: `$arrivederci`""")

client.run("MTU1OTI1NzUyNTAwODcyODEwNA.GC0Adb.GjAtHcWwdn9yv6FFwPVRCknIgb_fLB6R804BvU")