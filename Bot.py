import discord
import random
import time
nabercevap = ("1", "2", "3", "4", "5", "6")
kolecevap = ("1", "2","3","4","5","6", "7")
duyuru = str("YOUR ANOUNCEMENT HERE")



TOKEN = 'YOUR TOKEN HERE'
client = discord.Client()

@client.event
async def on_ready():
    print('Giriş yapıldı >> {0.user}'.format(client))



@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')



    if message.author == client.user:
        return

    if user_message.lower() == 'selam':
        await message.channel.send(f'selam {username}')
        return
    elif user_message.lower() == 'burada mısın köle' or user_message.lower() == 'burada mısın bot':
        await message.channel.send(f'Buradayım {username}')
        return
    elif user_message.lower() == 'köle':
        cevapkole= random.choice(kolecevap)
        await message.channel.send(cevapkole)
        return
    elif user_message.lower() == 'baybay' or user_message.lower() == 'hoşçakal' or user_message.lower() == 'görüşürüz':
         await message.channel.send(f'baybay {username}')
         return
    elif user_message.lower() == 'naber köle' or user_message.lower() == 'nasılsın köle':
         naber = random.choice(nabercevap)
         await message.channel.send(naber)
         return
    elif user_message.lower() == 'sa' or user_message.lower() == 'selamun aleyküm':
         await message.channel.send('as')
         return
    elif user_message.lower() == 'benim adım ne':
        await message.channel.send(f'senin takma adın {username}')
        return
    elif user_message.lower() == 'let me control':
        giris = input("Mesaj gönder: ")
        await message.channel.send(giris)
        return
    elif user_message.lower() == 'bana x de':
        await message.channel.send(f'Sana (şimdilik) ismin dışında bir isimle hitap edemem maalesef {username}')
        return
    elif user_message.lower() == 'manage functions':
        await message.channel.send(f'This command is not ready to use {username}')
        return
    elif username == "YOUR USERNAME" and user_message.lower() == "disconnect":
        await message.channel.send("Logging Out...")
        time.sleep(4.0)
        await message.channel.send("Logout Will Be Completed In 5 Minutes...")
        await client.logout()
        return
    elif username != "YOUR USERNAME" and user_message.lower() == "disconnect":
        await message.channel.send(f"You are not authorized for this transaction {username}")
        return 
    elif user_message.lower() == "!duyuru":
        await message.channel.send(duyuru)
        return

client.run(TOKEN)
