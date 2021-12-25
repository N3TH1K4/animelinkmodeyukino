import requests
#"https://source.unsplash.com/1600x900/?{keyword},{keyword}"
from telethon.sync import TelegramClient ,events,Button
api_id = 4091096
api_hash = '6bb0682b4af56456201c3b9d8b99c94a'
bot_token = '5069583926:AAFl9BFiu6ZyMOPHXxLQkWvkhjp46fPha3Y'

# We have to manually call "start" if we want an explicit bot token
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

op=[Button.url('HELLO','https://t.me/tr0j3n')]

with bot:
    @bot.on(events.NewMessage)
    async def start(event):
        if '/anime naruto' or '/anime Naruto' in event.raw_text:
            await event.reply('hi!',buttons=op)
    


bot.start()
bot.run_until_disconnected()
