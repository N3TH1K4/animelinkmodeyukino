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
            await event.reply('Download Link For A Place Further Than The Universe :Sora yori mo Tooi Basho (2018) 🤍👇🏻',buttons=link.placefur)
        elif 'place further' in event.pattern_match.group(1):
            await event.reply('Download Link For  A Place Further Than The Universe :Sora yori mo Tooi Basho (2018) 🤍👇🏻',buttons=link.placefur) 
            
            
        elif 'slient voice' in event.pattern_match.group(1):
            await event.reply('Download Link For A Silent Voice : Koe no Katachi (2016) 🤍👇🏻',buttons=link.silentv)
        elif 'a silent voice' in event.pattern_match.group(1):
            await event.reply('Download Link For A Silent Voice : Koe no Katachi (2016) 🤍👇🏻',buttons=link.silentv)
            
            
        elif 'whisker away' in event.pattern_match.group(1):
            await event.reply('Download Link For A Whisker Away (2020) 🤍👇🏻',buttons=link.whiskera)
        elif 'whisker' in event.pattern_match.group(1):
            await event.reply('Download Link For A Whisker Away (2020) 🤍👇🏻',buttons=link.whiskera)
            
            
        elif 'after the rain' in event.pattern_match.group(1):
            await event.reply('Download Link For After the Rain : Koi wa Ameagari no You ni (2018) 🤍👇🏻',buttons=link.afterrain)
        elif 'rain' in event.pattern_match.group(1):
            await event.reply('Download Link For After the Rain : Koi wa Ameagari no You ni (2018) 🤍👇🏻',buttons=link.afterrain)
            
            
        elif 'ahiru no' in event.pattern_match.group(1):
            await event.reply('Download Link For Ahiru no Sora (2019) 🤍👇🏻',buttons=link.ahiruno)
        elif 'ahiru no sora' in event.pattern_match.group(1):
            await event.reply('Download Link For Ahiru no Sora (2019) 🤍👇🏻',buttons=link.ahiruno)
            
            
        elif 'ajin' in event.pattern_match.group(1):
            await event.reply(' Download Link For Ajin (2016) 🤍👇🏻',buttons=link.ajin)
        elif 'Ajin' in event.pattern_match.group(1):
            await event.reply('Download Link For Ajin (2016) 🤍👇🏻',buttons=link.ajin)
            
            
        elif 'akame' in event.pattern_match.group(1):
            await event.reply('Download Link For Akame ga Kill! (2014) 🤍👇🏻',buttons=link.akame)
        elif 'akame ga kill' in event.pattern_match.group(1):
            await event.reply('Download Link For Akame ga Kill! (2014) 🤍👇🏻',buttons=link.akame)

            
        elif 'akira' in event.pattern_match.group(1):
            await event.reply('Download Link For Akira (1988) 🤍👇🏻',buttons=link.akira)
        elif 'Akria' in event.pattern_match.group(1):
            await event.reply('Download Link For Akira (1988) 🤍👇🏻',buttons=link.akira)       

            
        elif 'akudama' in event.pattern_match.group(1):
            await event.reply('Download Link For Akudama Drive (2020) 🤍👇🏻',buttons=link.akudama)
        elif 'akudama drive' in event.pattern_match.group(1):
            await event.reply('Download Link For Akudama Drive (2020) 🤍👇🏻',buttons=link.akudama)      
            
 
            
        elif 'angel' in event.pattern_match.group(1):
            await event.reply('Download Link For Angel Beats (2010) 🤍👇🏻',buttons=link.angel)
        elif 'angel beats' in event.pattern_match.group(1):
            await event.reply('Download Link For Angel Beats (2010) 🤍👇🏻',buttons=link.angel)   
            
            
        elif 'anohana' in event.pattern_match.group(1):
            await event.reply('Download Link For Anohana : The Flower We Saw That Day (2011) 🤍👇🏻',buttons=link.anohana)
        elif 'Anohana' in event.pattern_match.group(1):
            await event.reply('Download Link For Anohana : The Flower We Saw That Day (2011) 🤍👇🏻',buttons=link.anohana)   
            
            
            
        elif 'Another' in event.pattern_match.group(1):
            await event.reply('Download Link For Another (2012) 🤍👇🏻',buttons=link.another)
        elif 'another' in event.pattern_match.group(1):
            await event.reply('Download Link For Another (2012) 🤍👇🏻',buttons=link.another)  
            
            
            
        elif 'aoi' in event.pattern_match.group(1):
            await event.reply('Download Link For Aoi Bungaku Series (2009)  🤍👇🏻',buttons=link.aoi)
        elif 'Aoi bungaku series' in event.pattern_match.group(1):
            await event.reply('Download Link For Aoi Bungaku Series (2009)  🤍👇🏻',buttons=link.aoi)  
            
            
            
        elif 'appare' in event.pattern_match.group(1):
            await event.reply('Download Link For Appare-Ranman! (2020) 🤍👇🏻',buttons=link.appare)
        elif 'Appare ranman' in event.pattern_match.group(1):
            await event.reply('Download Link For Appare-Ranman! (2020) 🤍👇🏻',buttons=link.appare)  
            
            
            
        elif 'assassination classroom' in event.pattern_match.group(1):
            await event.reply('Download Link For Assassination Classroom; Ansatsu Kyoushitsu (2015) 🤍👇🏻',buttons=link.ass)
        elif 'assassination' in event.pattern_match.group(1):
            await event.reply('Download Link For Assassination Classroom; Ansatsu Kyoushitsu (2015) 🤍👇🏻',buttons=link.ass)  
            
            
            
        elif 'astra' in event.pattern_match.group(1):
            await event.reply('Download Link For Astra Lost in Space : Kanata no Astra (2019) 🤍👇🏻',buttons=link.astra)
        elif 'Astra lost in the space' in event.pattern_match.group(1):
            await event.reply('Download Link For Astra Lost in Space : Kanata no Astra (2019) 🤍👇🏻',buttons=link.astra)      
            
            
            
        elif 'attack on titan' in event.pattern_match.group(1):
            await event.reply('Download Link For Attack on Titan : Shingeki no kyojin (2013) 🤍👇🏻',buttons=link.aot)
        elif 'attack' in event.pattern_match.group(1):
            await event.reply('Download Link For Attack on Titan : Shingeki no kyojin (2013) 🤍👇🏻',buttons=link.aot)  
            

        elif 'azure' in event.pattern_match.group(1):
            await event.reply('Download Link For Azur Lane (2019) 🤍👇🏻',buttons=link.azure)
        elif 'Azure lane' in event.pattern_match.group(1):
            await event.reply('Download Link For Azur Lane (2019) 🤍👇🏻',buttons=link.azure)
      
    @bot.on(events,InlineQuery)
    async def iquery(query):
        if query.text =='help':
            result = query.builder.article('Help' , text='This is inline query' , buttons=[
                [ Button.inline('A') , Button.inline('b') ],])
            await query.answer([result])
  

bot.start()
bot.run_until_disconnected()
