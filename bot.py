import requests
import link as link
#"https://source.unsplash.com/1600x900/?{keyword},{keyword}"
from telethon.sync import TelegramClient ,events,Button
api_id = 4091096
api_hash = '6bb0682b4af56456201c3b9d8b99c94a'
bot_token = '5069583926:AAFl9BFiu6ZyMOPHXxLQkWvkhjp46fPha3Y'

# We have to manually call "start" if we want an explicit bot token
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


with bot:
    @bot.on(events.NewMessage(pattern="^/anime (.*)"))
    async def start(event):
 
        if 'naruto shippuden' in event.pattern_match.group(1):
            await event.reply('Download Link For Naruto And Naruto Shippuden 🤍👇🏻',buttons=link.naruto)
        elif 'Naruto' in event.pattern_match.group(1):
            await event.reply('Download Link For Naruto And Naruto Shippuden 🤍👇🏻',buttons=link.naruto)
        elif 'NARUTO' in event.pattern_match.group(1):
            await event.reply('Download Link For Naruto And Naruto Shippuden 🤍👇🏻',buttons=link.naruto)
            
            
            
        elif 'a place further than the universe' in event.pattern_match.group(1):
            await event.reply('Download Link For a place further than the universe 🤍👇🏻',buttons=link.placefur)
        elif 'place further' in event.pattern_match.group(1):
            await event.reply('Download Link For a place further than the universe 🤍👇🏻',buttons=link.placefur) 
            
            
        elif 'slient voice' in event.pattern_match.group(1):
            await event.reply('Download Link For A Silent Voice 🤍👇🏻',buttons=link.silentv)
        elif 'a silent voice' in event.pattern_match.group(1):
            await event.reply('Download Link For A Silent Voice 🤍👇🏻',buttons=link.silentv)
            
            
        elif 'whisker away' in event.pattern_match.group(1):
            await event.reply('Download Link For A Wshisker Away 🤍👇🏻',buttons=link.whiskera)
        elif 'whisker' in event.pattern_match.group(1):
            await event.reply('Download Link For A Wshisker Away 🤍👇🏻',buttons=link.whiskera)
            
            
        elif 'after the rain' in event.pattern_match.group(1):
            await event.reply('Download Link For After The Rain 🤍👇🏻',buttons=link.afterrain)
        elif 'rain' in event.pattern_match.group(1):
            await event.reply('Download Link For After The Rain 🤍👇🏻',buttons=link.afterrain)
            
            
        elif 'ahiru no' in event.pattern_match.group(1):
            await event.reply('Download Link For Ahiru Non Sora 🤍👇🏻',buttons=link.ahiruno)
        elif 'ahiru no sora' in event.pattern_match.group(1):
            await event.reply('Download Link For Ahiru Non Sora 🤍👇🏻',buttons=link.ahiruno)
            
            
        elif 'ajin' in event.pattern_match.group(1):
            await event.reply(' Download Link For Ajin 🤍👇🏻',buttons=link.ajin)
        elif 'Ajin' in event.pattern_match.group(1):
            await event.reply('Download Link For Ajin 🤍👇🏻',buttons=link.ajin)
            
            
        elif 'akame' in event.pattern_match.group(1):
            await event.reply('Download Link For Akame Ga Kill 🤍👇🏻',buttons=link.akame)
        elif 'akame ga kill' in event.pattern_match.group(1):
            await event.reply('Download Link For Akame Ga Kill 🤍👇🏻',buttons=link.akame)

            
        elif 'akira' in event.pattern_match.group(1):
            await event.reply('Download Link For Akira 🤍👇🏻',buttons=link.akira)
        elif 'Akria' in event.pattern_match.group(1):
            await event.reply('Download Link For Akira 🤍👇🏻',buttons=link.akira)       

            
        elif 'akudama' in event.pattern_match.group(1):
            await event.reply('Download Link For Akudama Drive 🤍👇🏻',buttons=link.akudama)
        elif 'akudama drive' in event.pattern_match.group(1):
            await event.reply('Download Link For Akudama Drive 🤍👇🏻',buttons=link.akudama)      
            
 
            
        elif 'angel' in event.pattern_match.group(1):
            await event.reply('Download Link For Angel Beats 🤍👇🏻',buttons=link.angel)
        elif 'angel beats' in event.pattern_match.group(1):
            await event.reply('Download Link For Angel Beats 🤍👇🏻',buttons=link.angel)   
            
            
        elif 'anohana' in event.pattern_match.group(1):
            await event.reply('Download Link For Anohana 🤍👇🏻',buttons=link.anohana)
        elif 'Anohana' in event.pattern_match.group(1):
            await event.reply('Download Link For Anohana 🤍👇🏻',buttons=link.anohana)   
            
            
            
        elif 'Another' in event.pattern_match.group(1):
            await event.reply('Download Link For Another 🤍👇🏻',buttons=link.another)
        elif 'another' in event.pattern_match.group(1):
            await event.reply('Download Link For Another 🤍👇🏻',buttons=link.another)  
            
            
            
        elif 'aoi' in event.pattern_match.group(1):
            await event.reply('Download Link For Aoi Bungaku Series 🤍👇🏻',buttons=link.aoi)
        elif 'Aoi bungaku series' in event.pattern_match.group(1):
            await event.reply('Download Link For Aoi Bungaku Series 🤍👇🏻',buttons=link.aoi)  
            
            
            
        elif 'akira' in event.pattern_match.group(1):
            await event.reply('Download Link For Akira 🤍👇🏻',buttons=link.akira)
        elif 'Akria' in event.pattern_match.group(1):
            await event.reply('Download Link For Akira 🤍👇🏻',buttons=link.akira)  
            
            
            
        elif 'akira' in event.pattern_match.group(1):
            await event.reply('Download Link For Akira 🤍👇🏻',buttons=link.akira)
        elif 'Akria' in event.pattern_match.group(1):
            await event.reply('Download Link For Akira 🤍👇🏻',buttons=link.akira)  
            
            
            
        elif 'akira' in event.pattern_match.group(1):
            await event.reply('Download Link For Akira 🤍👇🏻',buttons=link.akira)
        elif 'Akria' in event.pattern_match.group(1):
            await event.reply('Download Link For Akira 🤍👇🏻',buttons=link.akira)      
            
            
            
        elif 'akira' in event.pattern_match.group(1):
            await event.reply('Download Link For Akira 🤍👇🏻',buttons=link.akira)
        elif 'Akria' in event.pattern_match.group(1):
            await event.reply('Download Link For Akira 🤍👇🏻',buttons=link.akira)       


bot.start()
bot.run_until_disconnected()
