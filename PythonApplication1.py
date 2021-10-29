import discord
import random
import re
import os

bot = discord.Client()
regex = r'( ?({t}) )|(^({t})$)|( ({t}) ?)'.format(t='zxc|dota|дота|доту|ZXC|1000\-7|сф|сфе|душа|души')

array = ['I come for souls.', 'It\'s now or Nevermore.', 'Never say Nevermore…', 'I sense the proximity of souls…',
         ' I\'ll take that soul if you\'re not using it.']
array2 = ['https://tenor.com/view/dota-hero-shadow-fiend-freedom-gif-22676123',
          'https://tenor.com/view/sf-dance-sf-shadow-fiend-shadow-fiend-dance-sf-fiendish-swag-gif-22410105',
          'https://tenor.com/view/sf-shadowfiend-dota-dota2-ghoul-gif-22773706',
          'https://tenor.com/view/%D0%BF%D1%83%D0%B4%D0%B6-gif-23376057',
          'https://tenor.com/view/shadow-fiend-shadowraze-zxc-dota-gif-21768064',
          'https://tenor.com/view/let-me-die-zxc-shadow-fiend-dota-zxcursed-gif-21363324']


@bot.event
async def on_ready(event):
    print('сф вышел в мид)')


@bot.event
async def on_message(message):
    if not message.author.bot:
        print(f'{message.author}: {message.content}')
        if re.search(regex, message.content):
            await message.channel.send(random.choice(array))
            await message.channel.send(random.choice(array2))


bot.run(os.getenv('DISCORDTOKEN'))
