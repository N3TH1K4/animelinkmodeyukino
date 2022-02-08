import asyncio
from telethon.tl import functions, types
from telethon.sync import TelegramClient ,events 
from telethon.sessions import StringSession
api_id = 4091096
api_hash = '6bb0682b4af56456201c3b9d8b99c94a'
bot_token = '2025919134:AAEtaYWwSrYcIQsK7-1zn5aA581bb0hDJNc'
STRING_SESSION = "1BVtsOK0BuyOrsOmanqjqtRki98zGYMZtJE0CoaDRuBmlbw-bGzviSFhA3KhgMnKtUxyr9EDwgswl2ddFqptdD0NbBKRLCspOw9sJFtaIpj6A1XpCcC4d1cgddpROD4zXO2oYUwycDU2qvmyeyetRMwfo6J7-mCji1x66qQX_FWKQ5gkKv1ZY7W0XIf-0jpvJU60e2pGA_pY398QKmGdyK_soCsLVbclgs7QgJPw67-T4ManKid3qGCNUw3BHM8elvebCEBlHdt7IuJy2UmQx2hjStKZpuD0bAarI28yDCV6R1z33VTbJFmVTf-rSG5Ct33uNkva7SDyXnkQo3zcnagdjeWlu30A="
# We have to manually call "start" if we want an explicit bot token
tbot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
ubot = TelegramClient(StringSession(STRING_SESSION), api_id, api_hash)


@tbot.on(events.NewMessage(pattern="^/dmanga (.*)"))
async def alive(event):
    m = await event.reply("Getting The Manga")
    ok = event.pattern_match.group(1)
    async with ubot.conversation("@SagiriiRoBot") as bot_conv:
        await bot_conv.send_message("/manga " +ok)
        mang = await bot_conv.get_response()
        mangaa= mang.text
        await m.edit(mangaa)
        await m.edit("Now Copy The Manga ID and Send It As /rmanga <manga_id> <chapter_number>")
@tbot.on(events.NewMessage(pattern="^/rmanga (.*)"))
async def alisve(event):
    sender = await event.get_sender()
    m = await event.reply("Searching For The Chap")
    ok = event.pattern_match.group(1)
    async with ubot.conversation("@SagiriiRoBot") as bot_conv:
        await bot_conv.send_message("/read " +ok)
        await asyncio.sleep(5)
        response = await bot_conv.get_response()
        await asyncio.sleep(2)
        await ubot.forward_to(sender,response)
        


ubot.start()
tbot.run_until_disconnected()
ubot.run_until_disconnected()







