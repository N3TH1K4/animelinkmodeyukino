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
        elif 'A Place Further Than The Universe' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.placefur)
        elif 'place further' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.placefur) 
            
            
        elif 'silent voice' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.slientv)
        elif 'A Silent Voice' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.slientv)
            
            
        elif 'A Whisker Away' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.whiskera)
        elif 'whisker' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.whiskera)
            
            
        elif 'After The Rain' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.afterrain)
        elif 'rain' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.afterrain)
            
            
        elif 'ahiru no' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.ahiruno)
        elif 'Ahiru No Sora' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.ahiruno)
            
            
        elif 'ajin' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.ajin)
        elif 'Ajin' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.ajin)
            
            
        elif 'akame' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.akame)
        elif 'Akame Ga Kill' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.akame)

            
        elif 'akira' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.akira)
        elif 'Akria' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.akira)       

            
        elif 'akudama' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.akudama)
        elif 'Akudama Drive' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.akudama)      
            
 
            
        elif 'angel' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.angel)
        elif 'Angel Beats' in event.pattern_match.group(1):
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
        elif 'Aoi Bungaku' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.aoi)  
            
            
            
        elif 'appare' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.appare)
        elif 'Appare Ranman' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.appare)  
            
            
            
        elif 'Assassination Classroom' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.ass)
        elif 'assassination' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.ass)  
            
            
            
        elif 'astra' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.astra)
        elif 'Astra Lost In The Space' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.astra)      
            
            
            
        elif 'Attack On Titan' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.aot)
        elif 'attack' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.aot)  
            

        elif 'azure' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.azure)
        elif 'Azure Lane' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.azure)
            
            
            
#----------------------------------------list B------------------------------------------------------------------------------#            
            
        elif 'beginning' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.b)
        elif 'Beginning' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.b)
            
        elif 'baccano' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bac)
        elif 'Baccano' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bac)    
            
        elif 'back' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.back) 
        elif 'Back' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.back)
            
        elif 'bake' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bake)
        elif 'Bake' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bake)
            
        elif 'baki' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.baki)
        elif 'Baki' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.baki)    
            
        elif 'baku' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.baku)
        elif 'Baku' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.baku)
            
        elif 'banana' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bana) 
        elif 'Banana' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bana)
            
        elif 'baraka' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bara)
        elif 'Baraka' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bara)
            
        elif 'beast' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bea)
        elif 'Beast' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bea)
            
        elif 'beck' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.beck)
        elif 'Beck' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.beck)
            
        elif 'beelz' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bee)
        elif 'Beelz' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bee)    
            
        elif 'beyond' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.beyon)
        elif 'Beyond' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.beyon)
            
        elif 'butler' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bb)
        elif 'Butler' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bb)
            
            
        elif 'clover' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bc)
        elif 'Clover' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bc)
            
        elif 'lagoon' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bl)
        elif 'Lagoon' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bl)
            
        elif 'bleach' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bleach)
        elif 'Bleach' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bleach)    
            
        elif 'blend' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bs)  
        elif 'Blend' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bs) 
            
        elif 'blood' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bc)
        elif 'Blood' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bc)    
            
        elif 'blockade' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bbb)
        elif 'Blockade' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bbb)    
            
        elif 'exorcist' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.be)
        elif 'Exorcist' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.be)
            
        elif 'period' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bp)
        elif 'Period' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bp)
            
        elif 'spring' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bsr)
        elif 'Spring' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bsr)
            
        elif 'boarding' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bsj) 
        elif 'Boarding' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bsj)
            
        elif 'boruto' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.boruto)
        elif 'Boruto' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.boruto)   
            
            
        elif 'bottom' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.btc) 
        elif 'Bottom' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.btc) 
            
        elif 'bungou' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bungo)
        elif 'Bungou' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bungo)
            
        elif 'kabaddi' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bk)
        elif 'Kabaddi' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.bk)
            
        elif 'blood' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.blood)
        elif 'Blood' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.blood)    
 #----------------------------list C -----------------------------#           

        elif 'campione' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.chm)
        elif 'Campione' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.chm)


        elif 'Cells' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.caw)
        elif 'cells' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.caw)


        elif 'Charlotte' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.char)
        elif 'charlotte' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.char)


        elif 'chihaya' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.chi)
        elif 'Chihaya' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.chi)


        elif 'clannad' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.cla)
        elif 'Clannad' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.cla)


        elif 'elite' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.ce)
        elif 'Elite' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.ce)


        elif 'code' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.cg)
        elif 'Code' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.cg)


        elif 'combatants' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.cwd)
        elif 'Combatants' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.cwd)


        elif 'corpse' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.cp)
        elif 'Corpse' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.cp)


        elif 'cowboy' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.cb)
        elif 'Cowboy' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.cb)


        elif 'Cross' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.crg)
        elif 'cross' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.crg)
        
#--------------------------------------list D-----------------------------------------#        
        elif 'Gray' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.gray)
        elif 'gray' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.gray)


        elif 'dangan' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.dan)
        elif 'Dangan' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.dan)


        elif 'DanMachi' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.danma)
        elif 'danmachi' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.danma)


        elif 'Darker' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.dtb)
        elif 'darker' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.dtb)


        elif 'darwin' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.darling)
        elif 'Darwin' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.darling)


        elif 'Date' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.dal)
        elif 'date' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.dal)


        elif 'death' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.dn)
        elif 'Death' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.dn)


        elif 'Death' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.dp)
        elif 'Death Parade' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.dp)


        elif 'deca' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.dd)
        elif 'Deca' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.dd)


        elif 'Demon' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.ds)
        elif 'demon' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.ds)


        elif 'dennou' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.denn)
        elif 'Dennou' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.denn)


        elif 'conan' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.dc)
        elif 'Conan' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.dc)


        elif 'Detroit' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.dmc)
        elif 'detroit' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.dmc)


        elif 'Devilman' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.dmcb)
        elif 'devilman' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.dmcb)


        elif 'domestic' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.domes)
        elif 'Dosmestic' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.domes)


        elif 'Nagatoro' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.nagato)
        elif 'nagotoro' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.nagato)
            
            
        elif 'Dorohe' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.dorohe)
        elif 'dorohe' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.dorohe)
        
        elif 'dororo' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.dororo)
        elif 'Dororo' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.dororo)
        

        elif 'dragon' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.drgb)
        elif 'Dragon' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.drgb)

            
        elif 'dr stone' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.drstone)
        elif 'Dr Stone' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.drstone)
    
        elif 'durara' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.durara)
        elif 'Durara' in event.pattern_match.group(1):
            await event.reply(dwn,buttons=link.durara)
        
        
    
#--------------------------------------list else-------------------------------------#            
        else:
            await bot.send_sticker("CAACAgUAAx0CZJRACwACCkFhzFGBIsJu5crwkkXi08pdUMmIBgAC4QYAAn5ncyba4FPm_fvrBiME")
            
            


           
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
 #index buttons mode 

    @bot.on(events.NewMessage(pattern="^/index"))
    async def index(event):
            await event.reply(txt,buttons=[[ Button.inline('A', data =b'a'),Button.inline('B', data =b'b'),Button.inline('C', data =b'c'),Button.inline('D', data =b'd')],[ Button.inline('Back', data =b'left')],])
            
            
            
            
            
            
            
            
            
            
            
 #callback Queries 

    @bot.on(events.CallbackQuery)
    async def callback(event):
        if event.data == b'a':
            await event.edit(""" **Anime Names Started with Letter A**

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
            await event.edit(""" **Anime Names Started with Letter B**

🤍 `B: The Beginning`
🤍 `Baccano!`
🤍 `Backflip`
🤍 `Bakemonogatari`
🤍 `Baki`
🤍 `Bakuman`
🤍 `Banana Fish`
🤍 `Barakamon`
🤍 `Beastars`
🤍 `Beck: Mongolian Chop Squad`
🤍 `Beelzebub`
🤍 `Beyond the Boundary`
🤍 `Black Butler`
🤍 `Black Clover` 
🤍 `Black Lagoon`
🤍 `Bleach`
🤍 `Blend S`
🤍 `Blood +`
🤍 `Blood-C`
🤍 `Blood Blockade Battlefront`
🤍 `Blue Exorcist`
🤍 `Blue Period`
🤍 `Blue Spring Ride : Ao Haru Ride`
🤍 `Boarding School Juliet`
🤍 `Boruto: Naruto Next Generations`
🤍 `Bottom-Tier Character Tomozaki`
🤍 `Bungou Stray Dogs`
🤍 `Burning Kabaddi`

@Yukinonthecutebot""",buttons=[[ Button.inline('Back', data =b'back')],])
        
        
        elif event.data == b'c':
            await event.edit(""" **Anime Names Started with Letter C**
            
🤍 `Campione`
🤍 `Cells at Work!`
🤍 `Charlotte`
🤍 `Chihayafuru`
🤍 `Clannad`
🤍 `Classroom of the Elite`
🤍 `Code Geass`
🤍 `Combatants Will Be Dispatched!`
🤍 `Corpse Party`
🤍 `Cowboy Bebop`
🤍 `Cross Game`            
            
 @Yukinonthecutebot""",buttons=[[ Button.inline('Back', data =b'back')],])           
       
        
        
        elif event.data == b'd':
            await event.edit(""" **Anime Names Started with Letter D**

🤍 `D.Gray-Man`
🤍 `Danganronpa`
🤍 `DanMachi : Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka` 
🤍 `Darker than BLACK`
🤍 `Darling in the FRANXX`
🤍 `Darwin's Game`
🤍 `Date A Live`
🤍 `Death Note`
🤍 `Death Parade`
🤍 `Deca-Dence`
🤍 `Demon Slayer` 
🤍 `Dennou Coil`
🤍 `Detective Conan`
🤍 `Detroit Metal City`
🤍 `Devilman Crybaby`
🤍 `Domestic Girlfriend`
🤍 `Don't Toy With Me Nagatoro san : Ijiranaide, Nagatoro-san`
🤍 `Dorohedoro`
🤍 `Dororo`
🤍 `Dragon Ball`
🤍 `Dr. Stone` 
🤍 `Durarara!!`
            
  @Yukinonthecutebot""",buttons=[[ Button.inline('Back', data =b'back')],])              
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #leave
        elif event.data == b'left':
                await event.delete()
        
        #back mod
        elif event.data == b'back':
                await event.edit(txt,buttons=[[ Button.inline('A', data =b'a'),Button.inline('B', data =b'b'),Button.inline('C', data =b'c'),Button.inline('D', data =b'd')],[ Button.inline('Back', data =b'left')],])
                
                

bot.start()
bot.run_until_disconnected()
