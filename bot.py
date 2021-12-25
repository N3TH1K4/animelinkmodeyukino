import requests
#"https://source.unsplash.com/1600x900/?{keyword},{keyword}"
from telethon.sync import TelegramClient ,events,Button
api_id = 4091096
api_hash = '6bb0682b4af56456201c3b9d8b99c94a'
bot_token = '5069583926:AAFl9BFiu6ZyMOPHXxLQkWvkhjp46fPha3Y'

# We have to manually call "start" if we want an explicit bot token
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

op=[Button.url('Naruto','https://t.me/Naruto_and_NarutoShippuden')]

with bot:
    @bot.on(events.NewMessage(pattern="^/anime (.*)"))
    async def start(event):
        if 'naruto' or 'Naruto' or 'NARUTO' in event.pattern_match.group(1):
            await event.reply('Link For Naruto And Naruto Shippuden 👇',buttons=op)
    


bot.start()
bot.run_until_disconnected()
