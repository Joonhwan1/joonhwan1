from idna import valid_contextj
from youtube_dl import YoutubeDL
from bs4 import BeautifulSoup
import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.utils import get
from discord import FFmpegPCMAudio
import asyncio
import time


# 토큰 숨기기------------------------------

import os 
from dotenv import load_dotenv
load_dotenv()
token = os.gentenv("OTg0NjU1NTAzMzIzOTYzNDcz.GgCkAo.0cAS8azayNkr8Zdv6apN7DrZGaQyIY4blUe70w")

#------ 버튼
from discord.ui import Button, View
intents = discord.Intents.all()



bot = commands.Bot(command_prefix='?', intents=intents)

user = []     # 유저가 입력한 노래 정보
musictitle = []     #  가공된 정보의 노래 제목
song_queue = []    # 가공된 정보의 노래 링크
musicnow = []   # 현재 출력되는 노래 배열

def title(msg):
    global music
    global entireText
    music = musicnow[0]

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("headless") 
         
        
    driver = webdriver.Chrome(executable_path = r"C:\Users\준환\Desktop\ffmpeg\chromedriver\chromedriver.exe",options=options)
    #                 "C:\\Users\\준환\\Desktop\\ffmpeg\\chromedriver\\chromedriver.exe",options=options
        
    driver.get("https://www.youtube.com/results?search_query="+msg+"+lyrics")
    source = driver.page_source
    bs = BeautifulSoup(source, 'lxml')
    entire = bs.find_all('a', {'id': 'video-title'})
    entireNum = entire[0]                          
    entireText = entireNum.text.strip()
    musicurl = entireNum.get('href')
    url = 'https://www.youtube.com'+musicurl 

    with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
    URL = info['formats'][0]['url']
    return music, URL

def play(ctx):
    global vc
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    URL = song_queue[0]
    del user[0]
    del musictitle[0]
    del song_queue[0]
    vc = get(bot.voice_clients, guild=ctx.guild)
    if not vc.is_playing():


        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after=lambda e: play_next(ctx)) 



def play_next(ctx):
    if len(musicnow) - len(user) >= 2:
        for i in range(len(musicnow) - len(user) - 1):
            del musicnow[0]
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    if len(user) >= 1:
        if not vc.is_playing():
            del musicnow[0]
            URL = song_queue[0]
            del user[0]
            del musictitle[0]
            del song_queue[0]
            vc.play(discord.FFmpegPCMAudio(URL,**FFMPEG_OPTIONS), after=lambda e: play_next(ctx))





@bot.event
async def on_ready():
    print('로그인 했숑: ')
    print(bot.user.name)
    print('음악')
    await bot.change_presence(status=discord.Status.online, activity=None)



@bot.event
async def on_message(message):

    if message.content == ("머핀"):
        await message.channel.send("웨 ㅇㅂㅇ?")
    await bot.process_commands(message)

    if message.content == ("11"):
        await message.channel.send("웨?")
    await bot.process_commands(message)

    if message.content == ("12"):
        await message.channel.send("나와의 대화ㅋ")
    await bot.process_commands(message)

    if message.content == ("별기디"):
        await message.channel.send(f"<@872376750858981416>")
    await bot.process_commands(message)

    if message.content == ("ㅇㅁㅇ?"):
        await message.channel.send(f"<@960559298923073617>")
    await bot.process_commands(message)

    if message.content == ("부리부리"):
        await message.channel.send(f"<@476398338409889802>")
    await bot.process_commands(message)

    if message.content == ("스님"):
        await message.channel.send(f"<@637703099158626315>")
    await bot.process_commands(message)

    if message.content == ("계절4대장"):
        await message.channel.send(f"<@589093318533578771>") #크리
    await bot.process_commands(message)

    if message.content == ("계절4대장"):
        await message.channel.send(f"<@476398338409889802>") #몽실
    await bot.process_commands(message)

    if message.content == ("계절4대장"):
        await message.channel.send(f"<@935914811424915567>") #부닥
    await bot.process_commands(message)

    if message.content == ("계절4대장"):
        await message.channel.send(f"<@462260484666687488>") #묘니
    await bot.process_commands(message)

    if message.content == ("나"):
        await message.channel.send(f"<@752697173254209546>") 
    await bot.process_commands(message)




#-------- 버튼 추가   2022  06 18 토

@bot.command()
async def 버튼(ctx):
    button1 = Button(label="목걸이 강화", url="https://kinfolksoft.com/%ec%9b%8c%ed%81%ac%ec%ba%a0work-cam-%ed%82%a4%eb%b3%b4%eb%93%9c-%eb%a7%88%ec%9a%b0%ec%8a%a4-%eb%a7%a4%ed%81%ac%eb%a1%9c/" )
    button2 = Button(label="쿠팡 로켓배송", url="https://www.coupang.com/np/campaigns/82")
    button3 = Button(label="미니머핀", emoji= "🏃", style = discord.ButtonStyle.green)
    button4 = Button(label="몽실", style = discord.ButtonStyle.green)
    

    async def button_callback1(interaction):
        await ctx.send("ㄱㄷ 링크 이동함")

    async def button_callback2(interaction):
        await ctx.send("밥이나 함 찾아보재이")

    async def button_callback3(interaction):
        await ctx.send("ㅇㅂㅇ")

    async def button_callback4(interaction):
        await ctx.send("부리부리")



    button1.callback = button_callback1
    button2.callback = button_callback2
    button3.callback = button_callback3
    button4.callback = button_callback4
    

    view = View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)
    

    await ctx.send(embed = discord.Embed(title='메뉴',description="버튼 선택하3", colour=discord.Colour.blue()), view=view)
#------------------------------------------------------------



@bot.command()
async def 복사(ctx, *, text):
    await ctx.send(text)

@bot.command()
async def 하의1(ctx):
        global vc
        vc = await ctx.message.author.voice.channel.connect()

@bot.command()
async def 바의1(ctx):
        global vc
        await vc.disconnect()

@bot.command()
async def URL재생(ctx, *, url):
    YDL_OPTIONS = {'format': 'bestaudio','noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    global vc
    vc = ctx.message.guild.voice_client
    
    if not vc.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        await ctx.send(embed = discord.Embed(title= "노래 재생", description = "현재 " + url + "재생중.", color = 0x00ff00))        
    else:
        await ctx.send("노래 이미 재생중ㅎ")

@bot.command()
async def 재생(ctx, *, msg):
    global vc
    vc = ctx.message.guild.voice_client

    if vc is None:
        voiceChannel = ctx.message.author.voice.channel
        await voiceChannel.connect()
        print("Connected to voice")
        vc = discord.utils.get(bot.voice_clients, guild=ctx.guild)


    if not vc.is_playing():
        global entireText
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}



        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("headless")   
        
        driver = webdriver.Chrome(executable_path = r"C:\Users\준환\Desktop\ffmpeg\chromedriver\chromedriver.exe",options=options)
        #     경로는 둘 중 하나            "C:\\Users\\준환\\Desktop\\ffmpeg\\chromedriver\\chromedriver.exe",options=options

        driver.get("https://www.youtube.com/results?search_query="+msg+"+lyrics")
        source = driver.page_source
        bs = BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id': 'video-title'})
        entireNum = entire[0]
        entireText = entireNum.text.strip()
        musicurl = entireNum.get('href')
        url = 'https://www.youtube.com'+musicurl

        driver.quit()
        musicnow.insert(0,entireText)

        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        await ctx.send(embed = discord.Embed(title= "ㅇㅂㅇ♬", description = "현재 " + musicnow[0] + "-", color = 0x00ff00))
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after=lambda e: play_next(ctx))
    #else:
        #await ctx.send("이미 노래 재생 중이얌ㅎ")


@bot.command()
async def 일시정지(ctx):
    global vc
    vc = ctx.message.guild.voice_client

    if vc.is_playing():
        vc.pause()
        await ctx.send(embed = discord.Embed(title= "ㅇㅂㅇ?", description = musicnow[0] + "-", color = 0x00ff00))
    #else:
        #await ctx.send("지금 노래 재생 안됨")

@bot.command()
async def 다시재생(ctx):
    global vc
    vc = ctx.message.guild.voice_client

    try:
        vc.resume()
    except:
         await ctx.send("지금 노래 재생 안됨ㅋ")
    #else:
         #await ctx.send(embed = discord.Embed(title= "아나 ㅇㅂㅇ", description = musicnow[0]  + "-", color = 0x00ff00))

@bot.command()
async def 노래끄기(ctx):
    global vc
    vc = ctx.message.guild.voice_client

    if vc.is_playing():
        vc.stop()
        await ctx.send(embed = discord.Embed(title= "바의", description = musicnow[0]  + "-", color = 0x00ff00))
    #else:
        #await ctx.send("ㅋ")




#   ---------------------------새로운 기능 추가  2022-06-05 일 12:37am   -------------------------------------



@bot.command()
async def 대기열추가(ctx, *, msg):
    user.append(msg)
    result, URLTEST = title(msg)
    song_queue.append(URLTEST)
    await ctx.send(result + "을/를 재생목록에 추가했썰!")

@bot.command()
async def 대기열삭제(ctx, *, number):
    try:
        ex = len(musicnow) - len(user)
        del user[int(number) - 1]
        del musictitle[int(number) - 1]
        del song_queue[int(number)-1]
        del musicnow[int(number)-1+ex]
            
        await ctx.send("대기열이 정상적으로 삭제됨")
    except:
        if len(list) == 0:
            await ctx.send("대기열에 노래가 없")
        else:
            if len(list) < int(number):
                await ctx.send("숫자의 범위가 목록개수를 벗어났어")
            else:
                await ctx.send("숫자만 입력하3")

@bot.command()
async def 목록(ctx):
    if len(musictitle) == 0:
        await ctx.send("아직 아무 노래도 등록안했")
    else:
        global Text
        Text = ""
        for i in range(len(musictitle)):
            Text = Text + "\n" + str(i + 1) + ". " + str(musictitle[i])
            
        await ctx.send(embed = discord.Embed(title= "노래목록", description = Text.strip(), color = 0x00ff00))

@bot.command()
async def 목록초기화(ctx):
    try:
        ex = len(musicnow) - len(user)
        del user[:]
        del musictitle[:]
        del song_queue[:]
        while True:
            try:
                del musicnow[ex]
            except:
                break
        await ctx.send(embed = discord.Embed(title= "목록초기화", description = """목록이 정상적으로 초기화되었습니다. 이제 노래를 등록해볼까요?""", color = 0x00ff00))
    except:
        await ctx.send("아직 아무 노래도 등록안했")

@bot.command()
async def 목록재생(ctx):

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    
    if len(user) == 0:
        await ctx.send("아직 아무 노래도 등록안했")
    else:
        if len(musicnow) - len(user) >= 1:
            for i in range(len(musicnow) - len(user)):
                del musicnow[0]
        if not vc.is_playing():
            play(ctx)
        #else:
            #await ctx.send("노래 이미 재생중ㅋ")

#   ------------ 2022 06 05 월     새로 추가-------
@bot.command()
async def 멜론차트(ctx):
    global vc
    vc = ctx.message.guild.voice_client

    if not vc.is_playing():
        
        options = webdriver.ChromeOptions()
        options.add_argument("headless")

        global entireText
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("headless") 
         
        
        driver = webdriver.Chrome(executable_path = r"C:\Users\준환\Desktop\ffmpeg\chromedriver\chromedriver.exe",options=options)
        driver.get("https://www.youtube.com/results?search_query=멜론차트")
        source = driver.page_source
        bs = BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id': 'video-title'})
        entireNum = entire[0]
        entireText = entireNum.text.strip()
        musicurl = entireNum.get('href')
        url = 'https://www.youtube.com'+musicurl 

        driver.quit()

        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        await ctx.send(embed = discord.Embed(title= "멜론차트", description = "현재 " + entireText + "재생중ㅋ", color = 0x00ff00))
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    #else:
        #await ctx.send("이미 노래 재생 중ㅎ")














bot.run('OTg0NjU1NTAzMzIzOTYzNDcz.GgCkAo.0cAS8azayNkr8Zdv6apN7DrZGaQyIY4blUe70w')


