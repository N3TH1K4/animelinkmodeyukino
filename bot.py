import requests
import link as link
#"https://source.unsplash.com/1600x900/?{keyword},{keyword}"
from telethon.sync import TelegramClient ,events ,Button
api_id = 4091096
api_hash = '6bb0682b4af56456201c3b9d8b99c94a'
bot_token = '2025919134:AAGAyAXR9hTJZu6v75-5ho8ao95mcppXacU'

# We have to manually call "start" if we want an explicit bot token
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
txt = '🤍 Choose Any Button To Get The Animes That Can Download Using /anime <name> 🤍'
dwn = 'Is This The One You Were Searching? Here Some Download Links According To The Searched Query 🤍👇'

with bot:
    @bot.on(events.NewMessage(pattern="^/anime (.*)"))
    
    async def start(event):   
 
        if 'naruto shippuden' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.naruto)
        elif 'Naruto' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.naruto)
        elif 'NARUTO' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.naruto)
            
            
 #Letter "A"           
        elif 'a place further than the universe' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.placefur)
        elif 'place further' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.placefur) 
            
            
        elif 'silent voice' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.slientv)
        elif 'a silent voice' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.slientv)
            
            
        elif 'whisker away' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.whiskera)
        elif 'whisker' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.whiskera)
            
            
        elif 'after the rain' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.afterrain)
        elif 'rain' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.afterrain)
            
            
        elif 'ahiru no' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.ahiruno)
        elif 'ahiru no sora' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.ahiruno)
            
            
        elif 'ajin' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.ajin)
        elif 'Ajin' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.ajin)
            
            
        elif 'akame' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.akame)
        elif 'akame ga kill' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.akame)

            
        elif 'akira' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.akira)
        elif 'Akria' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.akira)       

            
        elif 'akudama' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.akudama)
        elif 'akudama drive' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.akudama)      
            
 
            
        elif 'angel' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.angel)
        elif 'angel beats' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.angel)   
            
            
        elif 'anohana' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.anohana)
        elif 'Anohana' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.anohana)   
            
            
            
        elif 'Another' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.another)
        elif 'another' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.another)  
            
            
            
        elif 'aoi' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.aoi)
        elif 'Aoi bungaku' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.aoi)  
            
            
            
        elif 'appare' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.appare)
        elif 'Appare ranman' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.appare)  
            
            
            
        elif 'assassination classroom' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.ass)
        elif 'assassination' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.ass)  
            
            
            
        elif 'astra' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.astra)
        elif 'Astra lost in the space' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.astra)      
            
            
            
        elif 'attack on titan' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.aot)
        elif 'attack' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.aot)  
            

        elif 'azure' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.azure)
        elif 'Azure lane' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.azure)
            
            
            
#----------------------------------------list B------------------------------------------------------------------------------#            
            
        elif 'beginning' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.b)
           
         elif 'baccano' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bac)
            
        elif 'back' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.back) 
            
        elif 'bake' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bake)
            
        elif 'baki' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.baki)  
            
        elif 'baku' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.baku)
            
        elif 'banana' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bana) 
            
        elif 'baraka' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bara)
            
        elif 'beast' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bea)
            
        elif 'beck' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.beck)
            
        elif 'beelz' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bee)  
            
        elif 'beyond' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.beyon)
            
        elif 'butler' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bb)  
            
        elif 'clover' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bc)
            
        elif 'lagoon' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bl)
            
        elif 'bleach' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bleach)
            
        elif 'blend' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bs)  
            
        elif 'blood' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bc)
            
        elif 'blockade' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bbb)
            
        elif 'exorcist' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.be)
            
        elif 'period' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bp)
            
        elif 'spring' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bsr)
            
        elif 'boarding' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bsj) 
            
        elif 'boruto' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.boruto)
            
        elif 'bottom' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.btc) 
            
        elif 'bungou' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bungo)
            
        elif 'kabaddi' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bk)
            
        elif 'blood' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.blood)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
 #index buttons mode 

    @bot.on(events.NewMessage(pattern="^/index"))
    async def index(event):
            await event.reply(txt,buttons=[[ Button.inline('A', data =b'a'),Button.inline('B', data =b'b')],[ Button.inline('Back', data =b'left')],])
            
            
            
            
            
            
            
            
            
            
            
 #callback Queries 

    @bot.on(events.CallbackQuery)
    async def callback(event):
        if event.data == b'a':
            await event.edit("""Anime Names Started with Letter A

🤍 `A Place Further Than The Universe`
🤍 `A Silent Voice: Koe no katachi`
🤍 `A Whisker Away`
🤍 `After the Rain`
🤍 `Ahiru No Sora`
🤍 `Ajin` 
🤍 `Akame Ga Kill`
🤍 `Akira`
🤍 `Akudama Drive`
🤍 `Angel Beats`
🤍 `Anohana : The Flower We Saw That Day`
🤍 `Another`
🤍 `Aoi Bungaku Series`
🤍 `Appare-Ranman!`
🤍 `Assassination Classroom`
🤍 `Astra Lost in Space`
🤍 `Attack on Titan`
🤍 `Azur Lane`

@Yukinonthecutebot""",buttons=[[ Button.inline('Back', data =b'back')],])
        
        elif event.data == b'b':
            await event.edit("""Anime Names Started with Letter B

🤍 `B: The Beginning`


@Yukinonthecutebot""",buttons=[[ Button.inline('Back', data =b'back')],])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #leave
        elif event.data == b'left':
                await event.delete()
        
        #back mod
        elif event.data == b'back':
                await event.edit(txt,buttons=[[ Button.inline('A', data =b'a'),Button.inline('B', data =b'b')],[ Button.inline('Back', data =b'left')],])
                
                

bot.start()
bot.run_until_disconnected()
