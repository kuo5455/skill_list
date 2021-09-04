import discord
import os
from discord import embeds
from discord import channel
from option import *

client=discord.Client()

@client.event 
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    print("System iogin")

@client.event
async def on_message(message):
    if message.author.bot:
        return None   

    if message.content == f"{prefix}봇 사용법" or message.content == f"{prefix}도움":
        embed = discord.Embed(title="기술표 도움말", description = "!봇 사용법 or !help", color=0x009bcf)
        embed.add_field(name="!캐릭터이름 커맨드", value="ex!브라이언 뒷무릎, !녹티스 66ap", inline=True)
        embed.add_field(name="!캐릭터이름 기술이름 or !기술이름", value="ex!카즈야 나락, !쌍부", inline=False)
        embed.add_field(name="등록된 캐릭터", value="녹티스, 카즈야, 샤힌, 폴, 클라우디오, 네간, 머독, 리로이, 데빌진", inline=False)
        await message.channel.send(embed=embed)


    if message.content == f"{prefix}계급표":
        embed = discord.Embed(title="계급표", description = "", color=0x009bcf)
        embed.add_field(name="추가사항", value="Tekken Lord->Tekken King로수정, 최고계급 Tekken God Omega추가", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/831066623103336459/831157990722895922/common.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}녹티스":
        embed = discord.Embed(title="녹티스 루시스 카일룸", description = "남성", color=0x009bcf)
        embed.add_field(name="나이", value="20세", inline=True)
        embed.add_field(name="출신지", value="루시스 왕국", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865482912945668146/1cfa337ec8452d13bf099da2b211266b3ac11185cd2fe7da322f5c81f4567b68ea080b678826bb097a11138c3325d8a8b4e8.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}녹티스 원투투":
        embed = discord.Embed(title="left right slice", description = "lp rp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="10", inline=True)
        embed.add_field(name="판정", value="상단", inline=False)
        embed.add_field(name="가드시", value=" -11", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883323345544826910/ezgif.com-gif-maker_32.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}녹티스 원투양손":
        embed = discord.Embed(title="left right heavy slash", description = "lp rp ap", color=0x009bcf)
        embed.add_field(name="프레임", value="10", inline=True)
        embed.add_field(name="판정", value="상상중", inline=False)
        embed.add_field(name="가드시", value=" -9(가드백있음)", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883333835004186674/lp_rp_ap.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}녹티스 rp" or message.content == f"{prefix}블리츠 러쉬":
        embed = discord.Embed(title="blitz rush", description = "rp rp rp rp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중x2상x2중(5타 히트시 하단창(1rp) 확정)", inline=False)
        embed.add_field(name="가드시", value=" -12(1타) -14(5타)", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883333818478628884/ezgif.com-gif-maker_19.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}투투 중단":
        embed = discord.Embed(title="triple assault", description = "rp rp 6rp", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -14", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883333816322768906/ezgif.com-gif-maker_30.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}투투 시프트":
        embed = discord.Embed(title="doudle assault to warp-strike", description = "rp rp 4rp", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -11", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883333835805302784/ezgif.com-gif-maker_29.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}녹티스 ap":
        embed = discord.Embed(title="cyclone slash", description = "ap(4로캔슬 가능)", color=0x009bcf)
        embed.add_field(name="프레임", value="18", inline=True)
        embed.add_field(name="판정", value="상중(호밍기)", inline=False)
        embed.add_field(name="가드시", value=" -9(1타) -14(2타)", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883333874992709652/ezgif.com-gif-maker_17.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}시프트":
        embed = discord.Embed(title="warp-strike", description = "6rp", color=0x009bcf)
        embed.add_field(name="프레임", value="20", inline=True)
        embed.add_field(name="판정", value="특수중단", inline=False)
        embed.add_field(name="가드시", value=" -9", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883323005667786772/ezgif.com-gif-maker_21.gif")
        await message.channel.send(embed=embed)


    if message.content == f"{prefix}녹티스 6lk rp":
        embed = discord.Embed(title="stinger knee to warp-strike", description = "6lk rp", color=0x009bcf)
        embed.add_field(name="프레임", value="16", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -11", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883323005667786772/ezgif.com-gif-maker_21.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}녹티스 6rk rp":
        embed = discord.Embed(title="circle slash", description = "6rk rp", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -11", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883333783095504926/ezgif.com-gif-maker_16.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}중단창":
        embed = discord.Embed(title="piercing spear", description = "6ap", color=0x009bcf)
        embed.add_field(name="프레임", value="16", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -19", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883323112173740092/ezgif.com-gif-maker_25.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}롤닷지" or message. content == f"{prefix}녹티스 6ak":
        embed = discord.Embed(title="roll-dodge", description = "6ak", color=0x009bcf)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883322817439993876/ezgif.com-gif-maker_15.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}녹티스 슬라이딩":
        embed = discord.Embed(title="tumble slide", description = "롤닷지 중 ak", color=0x009bcf)
        embed.add_field(name="프레임", value="20", inline=True)
        embed.add_field(name="판정", value="하단(히트시 오라(1ap) 확정)", inline=False)
        embed.add_field(name="가드시", value=" -20", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883333834068885534/ezgif.com-gif-maker_20.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}녹티스 자세 lp":
        embed = discord.Embed(title="rolling bash", description = "롤닷지 중 lp", color=0x009bcf)
        embed.add_field(name="프레임", value="18", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -13", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883333823880921148/ezgif.com-gif-maker_24.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}녹티스 파크":
        embed = discord.Embed(title="shlide bash", description = "6lprk", color=0x009bcf)
        embed.add_field(name="프레임", value="23", inline=True)
        embed.add_field(name="판정", value="중단(히트시 중단창(6ap)확정)", inline=False)
        embed.add_field(name="가드시", value=" -13", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883333829010546759/ezgif.com-gif-maker_31.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}녹티스 왼어퍼 투" or message.content == f"{prefix}녹티스 3lp rp":
        embed = discord.Embed(title="short uppercut to warp-strike", description = "3lp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="13", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -12(2타)", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883333806575218728/ezgif.com-gif-maker_22.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}녹티스 왼어퍼 포" or message.content == f"{prefix}녹티스 3lp rk":
        embed = discord.Embed(title="head spinner", description = "3lp rk", color=0x009bcf)
        embed.add_field(name="프레임", value="13", inline=True)
        embed.add_field(name="판정", value="중상", inline=False)
        embed.add_field(name="가드시", value=" -5", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883333808525545522/ezgif.com-gif-maker_23.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}컷칼":
        embed = discord.Embed(title="royal edge", description = "3rp", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -20", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883323246282428426/ezgif.com-gif-maker_28.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}녹티스 진군중단":
        embed = discord.Embed(title="combination raid", description = "3rk rp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="중상중", inline=False)
        embed.add_field(name="가드시", value=" -8", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883323200082169896/ezgif.com-gif-maker_27.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}녹티스 진군상단":
        embed = discord.Embed(title="combination raid", description = "3rk rp rk", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="중상상", inline=False)
        embed.add_field(name="가드시", value=" -5", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883333824690413578/ezgif.com-gif-maker_26.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}녹티스 3ap":
        embed = discord.Embed(title="heavy slash", description = "3ap", color=0x009bcf)
        embed.add_field(name="프레임", value="25", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -9(가드백있음)", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883322609121525760/ezgif.com-gif-maker_14.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}녹티스 2lp":
        embed = discord.Embed(title="whirlwind dagger", description = "2lp", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -3", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883322567878926387/ezgif.com-gif-maker_12.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}녹티스 2rp rp":
        embed = discord.Embed(title="hydra slice", description = "2rp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="20", inline=True)
        embed.add_field(name="판정", value="하상", inline=False)
        embed.add_field(name="가드시", value=" -15(1타)-9(2타)", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883322583167156294/ezgif.com-gif-maker_13.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}녹력장":
        embed = discord.Embed(title="mealstrom", description = "2rk lp ap", color=0x009bcf)
        embed.add_field(name="프레임", value="19", inline=True)
        embed.add_field(name="판정", value="하상중", inline=False)
        embed.add_field(name="가드시", value=" -31(1타)-18(3타)", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883333796768935936/ezgif.com-gif-maker_11.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}녹마찰":
        embed = discord.Embed(title="dancing edge", description = "1lp ap", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -5", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883313392125898762/ezgif.com-gif-maker.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}하단창":
        embed = discord.Embed(title="delta thrust", description = "1rp", color=0x009bcf)
        embed.add_field(name="프레임", value="24", inline=True)
        embed.add_field(name="판정", value="하단(카운터시 오라(1ap)확정)", inline=False)
        embed.add_field(name="가드시", value=" -19", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883333882508877894/ezgif.com-gif-maker_44.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}녹티스 1lk":
        embed = discord.Embed(title="sweep kick", description = "1lk", color=0x009bcf)
        embed.add_field(name="프레임", value="16", inline=True)
        embed.add_field(name="판정", value="하단", inline=False)
        embed.add_field(name="가드시", value=" -13", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883323571877851186/ezgif.com-gif-maker.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}녹티스 1rk":
        embed = discord.Embed(title="knee crusher", description = "1rk", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="하단", inline=False)
        embed.add_field(name="가드시", value=" -12", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}오라":
        embed = discord.Embed(title="royal slash", description = "1ap", color=0x009bcf)
        embed.add_field(name="프레임", value="25(홀드시46)", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -16(가드백 있음 ,홀드시+6가드백 없음)", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883333845406089258/ezgif.com-gif-maker_41.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}녹티스 4lp rp":
        embed = discord.Embed(title="shadow stab", description = "4lp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="12", inline=True)
        embed.add_field(name="판정", value="상단(2타 단독 카운터시 콤보)", inline=False)
        embed.add_field(name="가드시", value=" -9", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883333880353005658/ezgif.com-gif-maker_3.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}녹티스 4rp"or  message.content == f"{prefix}치도리":
        embed = discord.Embed(title="thunder impect", description = "1rp히트후ap(타격잡기)", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -9", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}부왕의 검"or  message.content == f"{prefix}녹티스 가불기":
        embed = discord.Embed(title="sword of the father", description = "4lkrp", color=0x009bcf)
        embed.add_field(name="프레임", value="69", inline=True)
        embed.add_field(name="판정", value="가불기", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883334150965325864/ezgif.com-gif-maker_36.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}퀵칼":
        embed = discord.Embed(title="quick stab", description = "9lp", color=0x009bcf)
        embed.add_field(name="프레임", value="13", inline=True)
        embed.add_field(name="판정", value="상단(카운터시 콤보)", inline=False)
        embed.add_field(name="가드시", value=" -4", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883333872664854558/ezgif.com-gif-maker_43.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}녹티스 컷니":
        embed = discord.Embed(title="ascension strom air", description = "9lk히트시8", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -13", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883340641311019038/5abf3196ce5ca880.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}녹티스 66rk":
        embed = discord.Embed(title="flare drive", description = "66rk", color=0x009bcf)
        embed.add_field(name="프레임", value="19", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -14", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883333871758888970/ezgif.com-gif-maker_6.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}시져스" or message. content == f"{prefix}녹티스 66ap":
        embed = discord.Embed(title="shadow scissors", description = "66ap", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단(호밍기)", inline=False)
        embed.add_field(name="가드시", value=" -9", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883333871859560448/ezgif.com-gif-maker_37.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}공참칼":
        embed = discord.Embed(title="meteor cursh", description = "666ap", color=0x009bcf)
        embed.add_field(name="프레임", value="23", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" +11", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883339337964609626/9b405cab7c0cf1b2.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}기상칼" or message. content == f"{prefix}녹티스 기상 lp rp":
        embed = discord.Embed(title="tidal slsah", description = "일어나면서lp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="13", inline=True)
        embed.add_field(name="판정", value="중단(2타 단독 카운터시 오라(1ap)확정)", inline=False)
        embed.add_field(name="가드시", value=" -13(2타)", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883340641311019038/5abf3196ce5ca880.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}녹티스 기상 lk" or message. content == f"{prefix}녹티스 기상 lk rp":
        embed = discord.Embed(title="stinger knee to warp-strike", description = "일어나면서lk rp", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -11(2타)", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883333737847337010/ezgif.com-gif-maker_8.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}녹티스 기상어퍼":
        embed = discord.Embed(title="regulus cross", description = "일어나면서rp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -14(2타)", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883333733984395274/ezgif.com-gif-maker_9.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}앉아방패":
        embed = discord.Embed(title="qiuck bash", description = "앉은상태에서3lp", color=0x009bcf)
        embed.add_field(name="프레임", value="16", inline=True)
        embed.add_field(name="판정", value="중단(히트시 오라(1ap) 확정)", inline=False)
        embed.add_field(name="가드시", value=" -9", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883333847851352064/ezgif.com-gif-maker_39.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}연칼":
        embed = discord.Embed(title="shadow slice", description = "앉은상태에서3rp", color=0x009bcf)
        embed.add_field(name="프레임", value="20", inline=True)
        embed.add_field(name="판정", value="하단", inline=False)
        embed.add_field(name="가드시", value=" -13", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883323488293781504/ezgif.com-gif-maker_40.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}녹티스 횡 오른손":
        embed = discord.Embed(title="voltex edge", description = "횡신 rp", color=0x009bcf)
        embed.add_field(name="프레임", value="18", inline=True)
        embed.add_field(name="판정", value="중단(카운터시 오라(1ap) 확정)", inline=False)
        embed.add_field(name="가드시", value=" 0", inline=False)
        await message.channel.send(embed=embed)
        
    if message.content == f"{prefix}녹티스 4rk ap":
        embed = discord.Embed(title="crescent slash combination", description = "4rk ap", color=0x009bcf)
        embed.add_field(name="프레임", value="18", inline=True)
        embed.add_field(name="판정", value="상중(2타 단독 카운터시 콤보)", inline=False)
        embed.add_field(name="가드시", value="-13(가드백 있음)", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883333890465493092/ezgif.com-gif-maker_4.gif")
        await message.channel.send(embed=embed)
        
    if message.content == f"{prefix}녹티스 4lk lp":
        embed = discord.Embed(title="night fall", description = "4lk lp", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="상중(히트시 오라(1ap) 확정)", inline=False)
        embed.add_field(name="가드시", value="-14", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883333516341964820/ezgif.com-gif-maker_2.gif")
        await message.channel.send(embed=embed)
        
    if message.content == f"{prefix}녹티스 뒤자세 rp":
        embed = discord.Embed(title="blind divide", description = "상대방에게 등을 보일떄 rp", color=0x009bcf)
        embed.add_field(name="프레임", value="20", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-9", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883323387794047036/ezgif.com-gif-maker_33.gif")
        await message.channel.send(embed=embed)
        
    if message.content == f"{prefix}녹티스 9rk":
        embed = discord.Embed(title="chaser shoot", description = "9rk", color=0x009bcf)
        embed.add_field(name="프레임", value="19", inline=True)
        embed.add_field(name="판정", value="상단(호밍기)", inline=False)
        embed.add_field(name="가드시", value="-3", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883333838821003314/ezgif.com-gif-maker_5.gif")
        await message.channel.send(embed=embed)
        
    if message.content == f"{prefix}녹티스 점프 ap":
        embed = discord.Embed(title="ari attack crush", description = "forward jump 정점에서 ap", color=0x009bcf)
        embed.add_field(name="프레임", value="18", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="+9", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883333826414256198/ezgif.com-gif-maker_35.gif")
        await message.channel.send(embed=embed)


    if message.content == f"{prefix}녹티스 레드":
        embed = discord.Embed(title="warp-strike", description = "6lkrp", color=0x009bcf)
        embed.add_field(name="프레임", value="18", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" +2(가드백있음)", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883333850372112475/ezgif.com-gif-maker_34.gif")
        await message.channel.send(embed=embed)
        
        
    if message.content == f"{prefix}녹티스 패링":
        embed = discord.Embed(title="parry", description = "4ar or 4al", color=0x009bcf)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/883333846211379240/ezgif.com-gif-maker_38.gif")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}카즈야":
        embed = discord.Embed(title="미시마 카즈야", description = "남성", color=0x009bcf)
        embed.add_field(name="나이", value="49세", inline=True)
        embed.add_field(name="출신지", value="없음(국적버림)", inline=True)
        embed.add_field(name="격투스타일", value="미시마류 가라테", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865551585123500042/f35615c93286ef30c850bb40d2a0d7a54162c1535482d9ace048d13e7079cea5fb52fb5ba2f033819ae8be81f8d6dfb5c10c.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}섬광":
        embed = discord.Embed(title="flash punch combo", description = "lp lp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="10", inline=True)
        embed.add_field(name="판정", value="상상중", inline=False)
        embed.add_field(name="가드시", value=" -17", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}카즈야 원투투" or message.content == f"{prefix}데빌진 원투투" :
        embed = discord.Embed(title="demon slayer", description = "lp rp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="10", inline=True)
        embed.add_field(name="판정", value="상단", inline=False)
        embed.add_field(name="가드시", value=" -12", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}카즈야 원투포쓰리":
        embed = discord.Embed(title="twin fang doule kick", description = "lp rp rk lk", color=0x009bcf)
        embed.add_field(name="프레임", value="10", inline=True)
        embed.add_field(name="판정", value="상상하중", inline=False)
        embed.add_field(name="가드시", value=" -13(3타)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}카즈야 쓰리원포":
        embed = discord.Embed(title="agony spear", description = "lk lp rk", color=0x009bcf)
        embed.add_field(name="프레임", value="13", inline=True)
        embed.add_field(name="판정", value="상상중", inline=False)
        embed.add_field(name="가드시", value=" -6", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}카즈야 데몬 시져스" or message.content == f"{prefix}카즈야 rp lp":
        embed = discord.Embed(title="demon sicssors", description = "[rp lp]", color=0x009bcf)
        embed.add_field(name="프레임", value="31", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -10", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}카즈야 파크":
        embed = discord.Embed(title="soul thust", description = "6rp", color=0x009bcf)
        embed.add_field(name="프레임", value="20", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -12", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}카즈야 6lk":
        embed = discord.Embed(title="oni front kick", description = "6lk", color=0x009bcf)
        embed.add_field(name="프레임", value="19", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -13", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}우종":
        embed = discord.Embed(title="right splits kick", description = "6rk", color=0x009bcf)
        embed.add_field(name="프레임", value="19", inline=True)
        embed.add_field(name="판정", value="중단(카운터시 뻥발(66rk)확정)", inline=False)
        embed.add_field(name="가드시", value=" +4", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}카즈야 왼어퍼투":
        embed = discord.Embed(title="slicing blade", description = "3lp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단(히트시 뻥발(66rk)확정)", inline=False)
        embed.add_field(name="가드시", value=" -13", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}카즈야 왼어퍼포":
        embed = discord.Embed(title="slaughter high kick", description = "3lp rk", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중상", inline=False)
        embed.add_field(name="가드시", value=" -3", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}카즈야 3lp 6rp":
        embed = discord.Embed(title="devastator", description = "3lp 6rp", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -12", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}카즈야 기원권":
        embed = discord.Embed(title="abolishing fist", description = "3rp", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="중단(호밍기,카운터시 콤보)", inline=False)
        embed.add_field(name="가드시", value=" -12", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}사자":
        embed = discord.Embed(title="lion slayer", description = "1rp", color=0x009bcf)
        embed.add_field(name="프레임", value="20", inline=True)
        embed.add_field(name="판정", value="중단(히트시 뻥발(66rk)확정)", inline=False)
        embed.add_field(name="가드시", value=" -9", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}퇴쇠":
        embed = discord.Embed(title="stature smash", description = "1rk", color=0x009bcf)
        embed.add_field(name="프레임", value="20", inline=True)
        embed.add_field(name="판정", value="하단", inline=False)
        embed.add_field(name="가드시", value=" -11", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}카즈야 4lp rp":
        embed = discord.Embed(title="sokushitsu goda", description = "4lp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="12", inline=True)
        embed.add_field(name="판정", value="상중", inline=False)
        embed.add_field(name="가드시", value=" -14", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}카즈야 몸지랄":
        embed = discord.Embed(title="demon's wrath", description = "4lk lp rk lp", color=0x009bcf)
        embed.add_field(name="프레임", value="18", inline=True)
        embed.add_field(name="판정", value="상상하중", inline=False)
        embed.add_field(name="가드시", value=" -14", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}카즈야 4rk":
        embed = discord.Embed(title="flash tornado", description = "4rk", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="상단", inline=False)
        embed.add_field(name="가드시", value=" -4", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}카즈야 가불기":
        embed = discord.Embed(title="lightning screw uppercut", description = "4lprk", color=0x009bcf)
        embed.add_field(name="프레임", value="63", inline=True)
        embed.add_field(name="판정", value="가불기", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}중단나락":
        embed = discord.Embed(title="roundhouse to triple spin kick", description = "9rkx4", color=0x009bcf)
        embed.add_field(name="프레임", value="25", inline=True)
        embed.add_field(name="판정", value="중하", inline=False)
        embed.add_field(name="가드시", value=" -12(1타) -22(2타)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}좌종":
        embed = discord.Embed(title="left splits kick", description = "66lk", color=0x009bcf)
        embed.add_field(name="프레임", value="20", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -4", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}카즈야 뻥발":
        embed = discord.Embed(title="devil's steel petal", description = "66rk", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="중단(카운터시 콤보)", inline=False)
        embed.add_field(name="가드시", value=" -9", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}뇌신권":
        embed = discord.Embed(title="dragon uppercut", description = "6n23lp", color=0x009bcf)
        embed.add_field(name="프레임", value="22", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -16", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}초풍":
        embed = discord.Embed(title="god wind fist", description = "6n23rp", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="상단", inline=False)
        embed.add_field(name="가드시", value=" -10(저스트시 +5 가드백)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}카즈야 나락":
        embed = discord.Embed(title="spinning demon to left hook", description = "3lp 6rp", color=0x009bcf)
        embed.add_field(name="프레임", value="16", inline=True)
        embed.add_field(name="판정", value="하중", inline=False)
        embed.add_field(name="가드시", value=" -23(1타) -16(2타)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}카즈야 공참각":
        embed = discord.Embed(title="leaping sidekick", description = "666lk", color=0x009bcf)
        embed.add_field(name="프레임", value="22", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" +10", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}카즈야 떠퍼" or message.content == f"{prefix}카즈야 기상 lp rp":
        embed = discord.Embed(title="twin pistons", description = "일어나면서 lp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="13", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -12", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}마신권"  or message.content == f"{prefix}카즈야 기상rp":
        embed = discord.Embed(title="demon god fist", description = "일어나면서 rp", color=0x009bcf)
        embed.add_field(name="프레임", value="16", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -16", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}카즈야 기상킥" :
        embed = discord.Embed(title="tsuanmi kick", description = "일어나면서 rk rk", color=0x009bcf)
        embed.add_field(name="프레임", value="11", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -15(2타)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}창 밖을 봐라"  or message.content == f"{prefix}카즈야 기상ap":
        embed = discord.Embed(title="fujin uraken", description = "일어나면서 ap", color=0x009bcf)
        embed.add_field(name="프레임", value="13", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -9", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}카즈야 레이져" :
        embed = discord.Embed(title="inferno", description = "데빌상태에서 ap", color=0x009bcf)
        embed.add_field(name="프레임", value="43", inline=True)
        embed.add_field(name="판정", value="상단 가불기", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}카즈야 레이져2" :
        embed = discord.Embed(title="devil blaster", description = "데빌상태에서 ak", color=0x009bcf)
        embed.add_field(name="프레임", value="69", inline=True)
        embed.add_field(name="판정", value="가불기", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}카즈야 레이져3" :
        embed = discord.Embed(title="reverse devil blaster", description = "데빌상태에서 ak ak", color=0x009bcf)
        embed.add_field(name="프레임", value="85", inline=True)
        embed.add_field(name="판정", value="가불기", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌카즈야 떠퍼" :
        embed = discord.Embed(title="twin pistons", description = "데빌상태에서 3lp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -13", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}헤븐즈" :
        embed = discord.Embed(title="heaven's door", description = "6n23lp(히트시 9입력)", color=0x009bcf)
        embed.add_field(name="프레임", value="22", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -16", inline=False)
        await message.channel.send(embed=embed)


    if message.content == f"{prefix}카즈야 데빌 트위스터" :
        embed = discord.Embed(title="devil twister", description = "데빌상태에서 횡신 rp", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -22", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}카즈야 레드":
        embed = discord.Embed(title="rage drive" , description = "6n23lprk9", color=0x009bcf)
        embed.add_field(name="프레임", value="18", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="+5(가드백 있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌":
        embed = discord.Embed(title="샤힌", description = "남성", color=0x009bcf)
        embed.add_field(name="출신지", value="사우디아라비아", inline=True)
        embed.add_field(name="격투스타일", value="군대식 격투술 ", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865657170170609704/943c297908708fee05b861f91554894c353d74f76d0ce3c2fad60ade7f7d750335b5fb269b52695bc135e5f3323dda18138a.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 원투투" :
        embed = discord.Embed(title="spica gut punch", description = "lp rp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="10", inline=True)
        embed.add_field(name="판정", value="상상중", inline=False)
        embed.add_field(name="가드시", value=" -11", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 원투쓰리" :
        embed = discord.Embed(title="spica bloinding sands to stealth step", description = "lp rp lk(3입력으로 자세이행)", color=0x009bcf)
        embed.add_field(name="프레임", value="10", inline=True)
        embed.add_field(name="판정", value="상단", inline=False)
        embed.add_field(name="가드시", value=" -8(자세이행시 -1)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 원투포" :
        embed = discord.Embed(title="spica wheel spin", description = "lp rp rk", color=0x009bcf)
        embed.add_field(name="프레임", value="10", inline=True)
        embed.add_field(name="판정", value="상상중", inline=False)
        embed.add_field(name="가드시", value=" -13", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 투원 " :
        embed = discord.Embed(title="cut in", description = "rp lp", color=0x009bcf)
        embed.add_field(name="프레임", value="10", inline=True)
        embed.add_field(name="판정", value="상중", inline=False)
        embed.add_field(name="가드시", value=" -4", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 투쓰리" :
        embed = discord.Embed(title="porrima bliding sand to stealth step", description = "rp lk(3입력으로 자세이행)", color=0x009bcf)
        embed.add_field(name="프레임", value="10", inline=True)
        embed.add_field(name="판정", value="상단", inline=False)
        embed.add_field(name="가드시", value=" -8(자세이행시 -1)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 lk" :
        embed = discord.Embed(title="bliding sand to stealth step", description = "lk(3입력으로 자세이행)", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="상단", inline=False)
        embed.add_field(name="가드시", value=" -8(자세이행시 -1)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 rk lp" :
        embed = discord.Embed(title="hallux kick to algenib ", description = "rk lp", color=0x009bcf)
        embed.add_field(name="프레임", value="11", inline=True)
        embed.add_field(name="판정", value="상단", inline=False)
        embed.add_field(name="가드시", value=" -5", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 rk lk" :
        embed = discord.Embed(title="hallux kick to high slahing kick", description = "rk rk", color=0x009bcf)
        embed.add_field(name="프레임", value="11", inline=True)
        embed.add_field(name="판정", value="상중", inline=False)
        embed.add_field(name="가드시", value=" -13", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 12딜캐" or message.content == f"{prefix}샤힌 6rp lk":
        embed = discord.Embed(title="silent sting", description = "6rp lk", color=0x009bcf)
        embed.add_field(name="프레임", value="12", inline=True)
        embed.add_field(name="판정", value="상단", inline=False)
        embed.add_field(name="가드시", value=" -12", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 rk rk" :
        embed = discord.Embed(title="hallux kick to ra'd ", description = "rk lp", color=0x009bcf)
        embed.add_field(name="프레임", value="11", inline=True)
        embed.add_field(name="판정", value="상단", inline=False)
        embed.add_field(name="가드시", value=" -5", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 6rp rk" :
        embed = discord.Embed(title="slient flow to stealth step ", description = "6rp rk(3입력으로 자세이행)", color=0x009bcf)
        embed.add_field(name="프레임", value="12", inline=True)
        embed.add_field(name="판정", value="상하", inline=False)
        embed.add_field(name="가드시", value=" -13(2타,자세이행시-18)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 6rp rk rk" :
        embed = discord.Embed(title="slient flow ", description = "6rp rk rk", color=0x009bcf)
        embed.add_field(name="프레임", value="12", inline=True)
        embed.add_field(name="판정", value="상하상", inline=False)
        embed.add_field(name="가드시", value=" -13(2타),-8(3타)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 6lk" :
        embed = discord.Embed(title="crescent moon ", description = "6lk", color=0x009bcf)
        embed.add_field(name="프레임", value="20", inline=True)
        embed.add_field(name="판정", value="중단(호밍기,카운터시 콤보)", inline=False)
        embed.add_field(name="가드시", value=" -5", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 6rk" :
        embed = discord.Embed(title="piercing talon ", description = "6rk", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="상단(호밍기)", inline=False)
        embed.add_field(name="가드시", value=" -5", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 3LK" :
        embed = discord.Embed(title="whirwind kick ", description = "3lk", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="중단(호밍기)", inline=False)
        embed.add_field(name="가드시", value=" -9", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 3rk" or message.content == f"{prefix}샤힌 오리발":
        embed = discord.Embed(title="whirwind kick ", description = "3lk", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -9", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 2rp":
        embed = discord.Embed(title="gut impact", description = "2rp", color=0x009bcf)
        embed.add_field(name="프레임", value="18", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -6", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 아래왼발" or message.content == f"{prefix}샤힌 2lk":
        embed = discord.Embed(title="slient rigel to stealth step", description = "2lk(3입력으로 자세이행)", color=0x009bcf)
        embed.add_field(name="프레임", value="16", inline=True)
        embed.add_field(name="판정", value="하단", inline=False)
        embed.add_field(name="가드시", value=" -14(자세이행시 -10)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 아래오른발" or message.content == f"{prefix}샤힌 2rk":
        embed = discord.Embed(title="vicious stomp", description = "2rk", color=0x009bcf)
        embed.add_field(name="프레임", value="19", inline=True)
        embed.add_field(name="판정", value="하단", inline=False)
        embed.add_field(name="가드시", value=" -12", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 1rp":
        embed = discord.Embed(title="raid strike to stealth step", description = "1rp(3입력으로 자세이행)", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -10(자세이행시 -3)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 1rp lp":
        embed = discord.Embed(title="raid strike", description = "1rp lp", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="중상", inline=False)
        embed.add_field(name="가드시", value=" -11(가드백있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 로하이":
        embed = discord.Embed(title="snake's bite rising scimitar", description = "1lk rk", color=0x009bcf)
        embed.add_field(name="프레임", value="20", inline=True)
        embed.add_field(name="판정", value="하상", inline=False)
        embed.add_field(name="가드시", value=" -17(1타) -13(2타)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 가불기":
        embed = discord.Embed(title="shaula", description = "1ap", color=0x009bcf)
        embed.add_field(name="프레임", value="64", inline=True)
        embed.add_field(name="판정", value="가불기", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 뒤왼손"or message. content == f"{prefix}샤힌 4lp":
        embed = discord.Embed(title="achernar", description = "4lp", color=0x009bcf)
        embed.add_field(name="프레임", value="19", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="+2", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 뒤오른손" or message. content == f"{prefix}샤힌 카운터 잡기":
        embed = discord.Embed(title="dust storm", description = "1rp", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단(카운터 잡기)", inline=False)
        embed.add_field(name="가드시", value=" -9", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 뒤왼발"or message. content == f"{prefix}샤힌 4lk":
        embed = discord.Embed(title="heel strike", description = "4lk", color=0x009bcf)
        embed.add_field(name="프레임", value="18", inline=True)
        embed.add_field(name="판정", value="중단(카운터시 뻥발(4rk)확정)", inline=False)
        embed.add_field(name="가드시", value=" 0", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 뻥발":
        embed = discord.Embed(title="broken mirage", description = "4rk", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="중단(카운터시 콤보)", inline=False)
        embed.add_field(name="가드시", value=" -15", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 플라잉 휠":
        embed = discord.Embed(title="crescent cleaver", description = "9lk", color=0x009bcf)
        embed.add_field(name="프레임", value="25", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -7", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 컷킥":
        embed = discord.Embed(title="altair", description = "9rk", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-13", inline=False)
        await message.channel.send(embed=embed)
        
    if message.content == f"{prefix}샤힌 66lk"or message.content == f"{prefix}샤힌 666lk":
        embed = discord.Embed(title="hunting falcon dive", description = "66lk or 666lk", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-12", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 파크":
        embed = discord.Embed(title="elnath", description = "66rk", color=0x009bcf)
        embed.add_field(name="프레임", value="16", inline=True)
        embed.add_field(name="판정", value="상단", inline=False)
        embed.add_field(name="가드시", value="-11(가드백있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 타격잡기" or message. content == f"{prefix}샤힌 64rp":
        embed = discord.Embed(title="hornet", description = "64rp", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="상단", inline=False)
        embed.add_field(name="가드시", value="-4(가드백 있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 공참손":
        embed = discord.Embed(title="antares", description = "666rp", color=0x009bcf)
        embed.add_field(name="프레임", value="20", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="+6", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 자세lp":
        embed = discord.Embed(title="blimding snake", description = "stealth step 도중 lp", color=0x009bcf)
        embed.add_field(name="프레임", value="12", inline=True)
        embed.add_field(name="판정", value="상단(카운터시 6rp lk확정)", inline=False)
        embed.add_field(name="가드시", value="-1", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 자세rp":
        embed = discord.Embed(title="blimding snake", description = "stealth step 도중 rp", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-9", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 자세rk lp":
        embed = discord.Embed(title="serpens", description = "stealth step 도중 rk lp", color=0x009bcf)
        embed.add_field(name="프레임", value="16", inline=True)
        embed.add_field(name="판정", value="하상(카운터시 2타 확정)", inline=False)
        embed.add_field(name="가드시", value="-15(1타)", inline=False)
        await message.channel.send(embed=embed)
        
    if message.content == f"{prefix}샤힌 자세 lk":
        embed = discord.Embed(title="hunting falcon dive", description = "stealth step 도중 lk", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-12", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 자세ak":
        embed = discord.Embed(title="low glide", description = "stealth step 도중 ak", color=0x009bcf)
        embed.add_field(name="프레임", value="26", inline=True)
        embed.add_field(name="판정", value="하단(카운터시 콤보)", inline=False)
        embed.add_field(name="가드시", value="-19", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 기상어퍼":
        embed = discord.Embed(title="hawk edge", description = "일어나면서 rp", color=0x009bcf)
        embed.add_field(name="프레임", value="16", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-17", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 기상 lk":
        embed = discord.Embed(title="doudle scorpion", description = "일어나면서 lk lk", color=0x009bcf)
        embed.add_field(name="프레임", value="13", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-11(1타) -13(2타)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤힌 슬라이딩":
        embed = discord.Embed(title="sand storm", description = "앉은상태에서 363lk", color=0x009bcf)
        embed.add_field(name="프레임", value="16", inline=True)
        embed.add_field(name="판정", value="하단", inline=False)
        embed.add_field(name="가드시", value="-23", inline=False)
        await message.channel.send(embed=embed)


    if message.content == f"{prefix}샤힌 레드":
        embed = discord.Embed(title="rage drive", description = "1rp rk(3입력으로 자세이행)", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="중상(재스크류)", inline=False)
        embed.add_field(name="가드시", value="+6(가드백 있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}폴" or message.content == f"{prefix}솟":
        embed = discord.Embed(title="폴 피닉스", description = "남성", color=0x009bcf)
        embed.add_field(name="나이", value="48세", inline=True)
        embed.add_field(name="출신지", value="미국", inline=True)
        embed.add_field(name="격투스타일", value="유도를 바탕으로한 종합격투기", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/869231712117338112/070dbf9a9071e1888e0aa1a0be86bf1310e8077bf763594487f364819062252ad3231c12eed0c37840678517e331e9224334.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}폴 헤머링":
        embed = discord.Embed(title="hammer of th gods ", description = "6ap", color=0x009bcf)
        embed.add_field(name="프레임", value="20", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="+3", inline=False)
        await message.channel.send(embed=embed)
        
    if message.content == f"{prefix}폴 진군":
        embed = discord.Embed(title="pison fire ", description = "lk rp (4입력시 스웨이)", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="중상", inline=False)
        embed.add_field(name="가드시", value="-3 +4(스웨이)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}횡산고":
        embed = discord.Embed(title="shoulder tackle" , description = "6lprk", color=0x009bcf)
        embed.add_field(name="프레임", value="21", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-14", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}폴 6rplk":
        embed = discord.Embed(title="chain" , description = "6rplk", color=0x009bcf)
        embed.add_field(name="프레임", value="20", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-14", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}폴 3lp lp rp":
        embed = discord.Embed(title="lion's roar" , description = "3lp lp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="중상중", inline=False)
        embed.add_field(name="가드시", value="-5", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}폴 왼어퍼":
        embed = discord.Embed(title="body blow tp sway" , description = "3lp(4입력으로 스웨이)", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-2 +3(스웨이)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}기와":
        embed = discord.Embed(title="hammer punch" , description = "2lp", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-9", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}기와 붕권":
        embed = discord.Embed(title="hammer punch to power punch" , description = "2lp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-17(2타,홀드시+20가드백 있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}기와 낙엽":
        embed = discord.Embed(title="hang over" , description = "2lp rk rp", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="중하중", inline=False)
        embed.add_field(name="가드시", value="-31(2타) -14(3타)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}벽력장":
        embed = discord.Embed(title="demolition man" , description = "2rk rp ap", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="하중중", inline=False)
        embed.add_field(name="가드시", value="-31(1타) -18(2타) -17(3타,가드백있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}철산고":
        embed = discord.Embed(title="shoulder smash" , description = "2ap", color=0x009bcf)
        embed.add_field(name="프레임", value="12", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-16", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}폴 1rp":
        embed = discord.Embed(title="shoot the moon" , description = "1rp", color=0x009bcf)
        embed.add_field(name="프레임", value="19", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-11", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}쌍부":
        embed = discord.Embed(title="doule axe swing" , description = "4lp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="12", inline=True)
        embed.add_field(name="판정", value="상단(호밍기)", inline=False)
        embed.add_field(name="가드시", value="-5", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}폴 뒷무릎" or message. content == f"{prefix}폴 4lk":
        embed = discord.Embed(title="light out" , description = "4kl", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-6", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}폴 4rk":
        embed = discord.Embed(title="leg sweep" , description = "4rk", color=0x009bcf)
        embed.add_field(name="프레임", value="20", inline=True)
        embed.add_field(name="판정", value="하단", inline=False)
        embed.add_field(name="가드시", value="-13", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}폴 파크":
        embed = discord.Embed(title="hassou strike" , description = "4ap", color=0x009bcf)
        embed.add_field(name="프레임", value="24", inline=True)
        embed.add_field(name="판정", value="상단", inline=False)
        embed.add_field(name="가드시", value="0(가드백 있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}북치기":
        embed = discord.Embed(title="wrecking ball" , description = "7rp", color=0x009bcf)
        embed.add_field(name="프레임", value="20", inline=True)
        embed.add_field(name="판정", value="중단(호밍기)", inline=False)
        embed.add_field(name="가드시", value="-9", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}쌍비":
        embed = discord.Embed(title="shredder" , description = "9lk rk", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-16(1타) -13(2타)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}용포 중단":
        embed = discord.Embed(title="juggernaut" , description = "66rp lp", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-12", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}용포 저스트":
        embed = discord.Embed(title="phoenix bone breaker" , description = "66rp lp(저스트입력)", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중상", inline=False)
        embed.add_field(name="가드시", value="-4(가드백 있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}용포 하단":
        embed = discord.Embed(title="bulldozer" , description = "66rp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="하단", inline=False)
        embed.add_field(name="가드시", value="-19(가드백 있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}폴 66rk":
        embed = discord.Embed(title="neutron bomb" , description = "66rk", color=0x009bcf)
        embed.add_field(name="프레임", value="20", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-1", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}폴 가불기":
        embed = discord.Embed(title="burning fist" , description = "44ap(88로 캔슬)", color=0x009bcf)
        embed.add_field(name="프레임", value="63", inline=True)
        embed.add_field(name="판정", value="가불기", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}이질풍":
        embed = discord.Embed(title="thruster" , description = "236lp", color=0x009bcf)
        embed.add_field(name="프레임", value="16", inline=True)
        embed.add_field(name="판정", value="상단", inline=False)
        embed.add_field(name="가드시", value="-4", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}붕권":
        embed = discord.Embed(title="phoenix smasher" , description = "236rp", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-17(가드백 있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}현월":
        embed = discord.Embed(title="gengetsu" , description = "236lk", color=0x009bcf)
        embed.add_field(name="프레임", value="18", inline=True)
        embed.add_field(name="판정", value="하단(카운터시 넘어짐)", inline=False)
        embed.add_field(name="가드시", value="-14", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}발산":
        embed = discord.Embed(title="mountain raze" , description = "236ak", color=0x009bcf)
        embed.add_field(name="프레임", value="19", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-9", inline=False)
        await message.channel.send(embed=embed)
        
    if message.content == f"{prefix}214lp":
        embed = discord.Embed(title="god hammer punch" , description = "214lp", color=0x009bcf)
        embed.add_field(name="프레임", value="18", inline=True)
        embed.add_field(name="판정", value="중단(카운터시 콤보)", inline=False)
        embed.add_field(name="가드시", value="0", inline=False)
        await message.channel.send(embed=embed)
        
    if message.content == f"{prefix}214lk":
        embed = discord.Embed(title="sway and low kick" , description = "214lk", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="하단", inline=False)
        embed.add_field(name="가드시", value="-21", inline=False)
        await message.channel.send(embed=embed)
        
    if message.content == f"{prefix}214lk rp lp":
        embed = discord.Embed(title="rapid fire to phoenix smasher" , description = "214lk rp lp", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="하중상", inline=False)
        embed.add_field(name="가드시", value="-21, -10(3타, 가드백 있음)", inline=False)
        await message.channel.send(embed=embed)
        
    if message.content == f"{prefix}214lk rp lk":
        embed = discord.Embed(title="rapid fire to lightning breaker" , description = "214lk rp lk", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="하중중(3타 단독 카운터시 콤보)", inline=False)
        embed.add_field(name="가드시", value="-21, -13(3타)", inline=False)
        await message.channel.send(embed=embed)
        
    if message.content == f"{prefix}214ap":
        embed = discord.Embed(title="higaku" , description = "214ap", color=0x009bcf)
        embed.add_field(name="프레임", value="18", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-14)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}와구":
        embed = discord.Embed(title="kawaragoma" , description = "214rk", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="상단(카운터시 콤보)", inline=False)
        embed.add_field(name="가드시", value="+1", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}주문하신 음식"  or message. content == f"{prefix}폴 기상어퍼":
        embed = discord.Embed(title="thunder palm" , description = "일어나면서 rp", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-14", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}사응":
        embed = discord.Embed(title="shioh" , description = "일어나면서 lk rp", color=0x009bcf)
        embed.add_field(name="프레임", value="13", inline=True)
        embed.add_field(name="판정", value="중상", inline=False)
        embed.add_field(name="가드시", value="-9", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}폴 손나락":
        embed = discord.Embed(title="gunba" , description = "앉은상태에서 3ap", color=0x009bcf)
        embed.add_field(name="프레임", value="32", inline=True)
        embed.add_field(name="판정", value="하단", inline=False)
        embed.add_field(name="가드시", value="-12", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}부지화":
        embed = discord.Embed(title="pump in peldal" , description = "횡신 lk", color=0x009bcf)
        embed.add_field(name="프레임", value="19", inline=True)
        embed.add_field(name="판정", value="하단(카운터시 쌍부(4lp rp),철산고(2ap)확정)", inline=False)
        embed.add_field(name="가드시", value="-12", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}암운 조이기" or message. content == f"{prefix}킹운 조이기":
        embed = discord.Embed(title="ultimate punishment" , description = "태클중에 rp 2lp lp n rk lp ap", color=0x009bcf)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}레붕":
        embed = discord.Embed(title="rage drive" , description = "236ap", color=0x009bcf)
        embed.add_field(name="프레임", value="20", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="+7(가드백 있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}폴 레아":
        embed = discord.Embed(title="rage art" , description = "ap(4입력으로캔슬) ", color=0x009bcf)
        embed.add_field(name="프레임", value="22", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-22", inline=False)
        await message.channel.send(embed=embed)

    
    if message.content == f"{prefix}클라우디오":
        embed = discord.Embed(title="클라우디오 세라피노", description = "남성", color=0x009bcf)
        embed.add_field(name="나이", value="불명", inline=True)
        embed.add_field(name="출신지", value="이탈리아", inline=True)
        embed.add_field(name="격투스타일", value="시리우스류 퇴마술", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/869231511092752424/80fe9d12d1302ca6e840fa1494795237f99c709b12e972baa219c74644c120559f6f842bbcd98d8ad8808105ba59ee335fe6.png")
        await message.channel.send(embed=embed)


    if message.content == f"{prefix}클라 앞투투" or message. content == f"{prefix}클라 12딜캐":
        embed = discord.Embed(title="deadly sin to sarbust" , description = "6rp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="12", inline=True)
        embed.add_field(name="판정", value="상중", inline=False)
        embed.add_field(name="가드시", value="-26(가드백 있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}클라 우종":
        embed = discord.Embed(title="into the abyss" , description = "6rk", color=0x009bcf)
        embed.add_field(name="프레임", value="22", inline=True)
        embed.add_field(name="판정", value="중단(카운터시 아케디아(1lk),롤링스피어(ak)확정)", inline=False)
        embed.add_field(name="가드시", value="+4", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}내장뽑기":
        embed = discord.Embed(title="cross arm strike" , description = "6ap ap", color=0x009bcf)
        embed.add_field(name="프레임", value="16", inline=True)
        embed.add_field(name="판정", value="중단(starbust 상태일시 콤보)", inline=False)
        embed.add_field(name="가드시", value="-18(1타) -14(2타,starbust 상태일시-9)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}클라 떠퍼":
        embed = discord.Embed(title="sky's arc" , description = "3lp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-15", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}클라 기원권" or message. content == f"{prefix}클라 3rp":
        embed = discord.Embed(title="chaos fist" , description = "3rp", color=0x009bcf)
        embed.add_field(name="프레임", value="13", inline=True)
        embed.add_field(name="판정", value="중단(카운터시 콤보)", inline=False)
        embed.add_field(name="가드시", value="-13", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}디스펠 매직":
        embed = discord.Embed(title="dispel magic" , description = "3lk lp", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-12", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}디스펠 포스":
        embed = discord.Embed(title="dispel force" , description = "3lk rp", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="중상", inline=False)
        embed.add_field(name="가드시", value="-2", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}클라 2lp rp":
        embed = discord.Embed(title="axion" , description = "2lp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-9(starbust 상태일시 +8)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}클라 손나락":
        embed = discord.Embed(title="gravity point" , description = "2rp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="20", inline=True)
        embed.add_field(name="판정", value="하단(starbust 상태일시 콤보)", inline=False)
        embed.add_field(name="가드시", value="-11", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}클산고":
        embed = discord.Embed(title="Superbia" , description = "2ap", color=0x009bcf)
        embed.add_field(name="프레임", value="13", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-18", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}아케디아":
        embed = discord.Embed(title="Acedia" , description = "1lk", color=0x009bcf)
        embed.add_field(name="프레임", value="24", inline=True)
        embed.add_field(name="판정", value="하단(카운터시 콤보)", inline=False)
        embed.add_field(name="가드시", value="-15", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}클라 4lp" or message. content == f"{prefix}클라 호밍기":
        embed = discord.Embed(title="vanishing strom" , description = "4lp", color=0x009bcf)
        embed.add_field(name="프레임", value="18", inline=True)
        embed.add_field(name="판정", value="중단(호밍기)", inline=False)
        embed.add_field(name="가드시", value="-5", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}클라 뒷무릎" or message.content == f"{prefix}클라 4lk":
        embed = discord.Embed(title="crescent heel" , description = "4lk lk", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="중단(2타카운터시 콤보)", inline=False)
        embed.add_field(name="가드시", value="-12(2타)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}클라 4rk rp":
        embed = discord.Embed(title="shining ray to star bust" , description = "4rk rp", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="중단(히트시 star bust)", inline=False)
        embed.add_field(name="가드시", value="-12", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}클라 가불기":
        embed = discord.Embed(title="big bang" , description = "4lkrp", color=0x009bcf)
        embed.add_field(name="프레임", value="72", inline=True)
        embed.add_field(name="판정", value="가불기", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}제노사이드 커터"or message. content == f"{prefix}클라 컷킥":
        embed = discord.Embed(title="sky slash nova" , description = "9rk", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-13", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}클라 66rk":
        embed = discord.Embed(title="Invidia" , description = "66rk", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-5", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}클라 통발":
        embed = discord.Embed(title="orbit slient to star bust" , description = "66ap", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="중단(히트시 star bust)", inline=False)
        embed.add_field(name="가드시", value="-8(가드백 있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}번너클":
        embed = discord.Embed(title="ira to star bust" , description = "666rp", color=0x009bcf)
        embed.add_field(name="프레임", value="13", inline=True)
        embed.add_field(name="판정", value="상단(히트시 star bust)", inline=False)
        embed.add_field(name="가드시", value="+7", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}클라 기상 lp":
        embed = discord.Embed(title="noble step" , description = "일어나면서 lp lp", color=0x009bcf)
        embed.add_field(name="프레임", value="13", inline=True)
        embed.add_field(name="판정", value="중상", inline=False)
        embed.add_field(name="가드시", value="-12(2타)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}클라 기상어퍼":
        embed = discord.Embed(title="sylvia to star bust" , description = "일어나면서 rp", color=0x009bcf)
        embed.add_field(name="프레임", value="13", inline=True)
        embed.add_field(name="판정", value="중단(히트시 star bust)", inline=False)
        embed.add_field(name="가드시", value="-14", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}클라 횡rk":
        embed = discord.Embed(title="Luxuria" , description = "횡신 rk", color=0x009bcf)
        embed.add_field(name="프레임", value="20", inline=True)
        embed.add_field(name="판정", value="하단", inline=False)
        embed.add_field(name="가드시", value="-12", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}클라 레드":
        embed = discord.Embed(title="rage drive" , description = "4rk rp6", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="중단(발동시 star bust)", inline=False)
        embed.add_field(name="가드시", value="+7", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간":
        embed = discord.Embed(title="네간", description = "남성", color=0x009bcf)
        embed.add_field(name="나이", value="53세", inline=True)
        embed.add_field(name="출신지", value="미국", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865647897008930826/a1ed2cc6e4432dccc1c2f18c881656300e7f43c96b690fc55574e4722d428d11da76aa4a880e084d245f4155a4e969cb662c.png")
        await message.channel.send(embed=embed)
    
    if message.content == f"{prefix}네간 원원투":
        embed = discord.Embed(title="sadstic combination" , description = "lp lp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="10", inline=True)
        embed.add_field(name="판정", value="상상중", inline=False)
        embed.add_field(name="가드시", value="-5", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 원투":
        embed = discord.Embed(title="jab to hilt shot to intimidation" , description = "lp rp(rp홀드시 자세이행)", color=0x009bcf)
        embed.add_field(name="프레임", value="10", inline=True)
        embed.add_field(name="판정", value="상단", inline=False)
        embed.add_field(name="가드시", value="-5", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 원투투":
        embed = discord.Embed(title="heavy rain" , description = "lp rp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="10", inline=True)
        embed.add_field(name="판정", value="상상중(3타 히트시 콤보)", inline=False)
        embed.add_field(name="가드시", value="+4", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 원투포":
        embed = discord.Embed(title="dark night combination" , description = "lp rp rk", color=0x009bcf)
        embed.add_field(name="프레임", value="10", inline=True)
        embed.add_field(name="판정", value="상단", inline=False)
        embed.add_field(name="가드시", value="-9(가드백 있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 투원포":
        embed = discord.Embed(title="ahin smasher" , description = "rp lp rk", color=0x009bcf)
        embed.add_field(name="프레임", value="11", inline=True)
        embed.add_field(name="판정", value="상상하", inline=False)
        embed.add_field(name="가드시", value="-12", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 rp":
        embed = discord.Embed(title="excutioner rush" , description = "rpx4", color=0x009bcf)
        embed.add_field(name="프레임", value="11", inline=True)
        embed.add_field(name="판정", value="상중x3", inline=False)
        embed.add_field(name="가드시", value="-8(1타) -14(2타~)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 ap":
        embed = discord.Embed(title="swtch hitter" , description = "ap", color=0x009bcf)
        embed.add_field(name="프레임", value="13", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-14", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 자세":
        embed = discord.Embed(title="intimdation" , description = "ak(적의 하단공격과 동시에 입력하면 하단패링)", color=0x009bcf)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 자세lp rp":
        embed = discord.Embed(title="slughter strike" , description = "intimdation 도중 lp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-13", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 자세rp":
        embed = discord.Embed(title="beatdwon" , description = "intimdation 도중 rp", color=0x009bcf)
        embed.add_field(name="프레임", value="20", inline=True)
        embed.add_field(name="판정", value="중단(히트시 밟기(2ak)확정)", inline=False)
        embed.add_field(name="가드시", value="+7", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 자세lk":
        embed = discord.Embed(title="push kick to intimdation" , description = "intimdation 도중 lk", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-2(가드백 있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 자세rk":
        embed = discord.Embed(title="corpse kick to intimdation" , description = "intimdation 도중 rk", color=0x009bcf)
        embed.add_field(name="프레임", value="20", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-7(가드백 있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 자세ap"or message. content == f"{prefix}네간 자세 파크":
        embed = discord.Embed(title="grand slam" , description = "intimdation 도중 ap", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="상단", inline=False)
        embed.add_field(name="가드시", value="-9(가드백 있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 가불기":
        embed = discord.Embed(title="punishment" , description = "intimdation 도중 lkrp(4입력으로 취소)", color=0x009bcf)
        embed.add_field(name="프레임", value="60", inline=True)
        embed.add_field(name="판정", value="가불기", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 자세3rp":
        embed = discord.Embed(title="blast off" , description = "intimdation 도중 rp", color=0x009bcf)
        embed.add_field(name="프레임", value="19", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-20(가드백 있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 자세2rp":
        embed = discord.Embed(title="terrible pain" , description = "intimdation 도중 2rp", color=0x009bcf)
        embed.add_field(name="프레임", value="21", inline=True)
        embed.add_field(name="판정", value="하단", inline=False)
        embed.add_field(name="가드시", value="-13", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 푸싱" or message. content == f"{prefix}네간 lkrp":
        embed = discord.Embed(title="shove to intimdation" , description = "lkrp", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="중단(카운터시 자세lp rp확정)", inline=False)
        embed.add_field(name="가드시", value="-7(가드백 있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 6rp rp":
        embed = discord.Embed(title="face grinder" , description = "6rp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="상중(1타 카운터시 2타 확정)", inline=False)
        embed.add_field(name="가드시", value="-12", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 7rp":
        embed = discord.Embed(title="matmador" , description = "7rp", color=0x009bcf)
        embed.add_field(name="프레임", value="25", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-20", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 4lp rp":
        embed = discord.Embed(title="molotov cocktail" , description = "4lp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="16", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-10", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 파크" or message. content == f"{prefix}네간 6ap":
        embed = discord.Embed(title="walker maker" , description = "6ap", color=0x009bcf)
        embed.add_field(name="프레임", value="24", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-15", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 6lkrp":
        embed = discord.Embed(title="trip wire" , description = "6lkrp", color=0x009bcf)
        embed.add_field(name="프레임", value="28", inline=True)
        embed.add_field(name="판정", value="하단", inline=False)
        embed.add_field(name="가드시", value="-12", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 3lp lp rp":
        embed = discord.Embed(title="side swipe smash" , description = "3lp lp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="13", inline=True)
        embed.add_field(name="판정", value="중상중", inline=False)
        embed.add_field(name="가드시", value="-13(3타,가드백 있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 왼어퍼투":
        embed = discord.Embed(title="tendezer to intimidation" , description = "3lp rp(rp홀드시 자세이행)", color=0x009bcf)
        embed.add_field(name="프레임", value="13", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-11", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 3rp":
        embed = discord.Embed(title="blood moon to intimidation" , description = "3rp(rp홀드시 자세이행)", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-14", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 3rk rp":
        embed = discord.Embed(title="front kick to temple smash to intimidation" , description = "3rk rp(rp홀드시 자세이행)", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="중상", inline=False)
        embed.add_field(name="가드시", value="+1", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 3ap":
        embed = discord.Embed(title="no exceptions" , description = "3ap", color=0x009bcf)
        embed.add_field(name="프레임", value="21", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-14", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 2rp":
        embed = discord.Embed(title="death penalty" , description = "2rp", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="중단(카운터잡기)", inline=False)
        embed.add_field(name="가드시", value="-9", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 9rk":
        embed = discord.Embed(title="blunt force" , description = "9rk", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="중단(카운터시 콤보)", inline=False)
        embed.add_field(name="가드시", value="-7", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 짠발":
        embed = discord.Embed(title="kneecapper" , description = "2lk", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="하단", inline=False)
        embed.add_field(name="가드시", value="-12", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 1rp":
        embed = discord.Embed(title="agony to intimidation" , description = "1rp", color=0x009bcf)
        embed.add_field(name="프레임", value="24", inline=True)
        embed.add_field(name="판정", value="하단(히트시 자세이행)", inline=False)
        embed.add_field(name="가드시", value="-14", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 4rp rp":
        embed = discord.Embed(title="back swing brain tp death penalty" , description = "4rp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="16", inline=True)
        embed.add_field(name="판정", value="상중(호밍기,타격 잡기,1타 카운터시 2타 확정)", inline=False)
        embed.add_field(name="가드시", value="-11", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 4rp lk":
        embed = discord.Embed(title="back swing funneral" , description = "4rp lk", color=0x009bcf)
        embed.add_field(name="프레임", value="16", inline=True)
        embed.add_field(name="판정", value="상중(호밍기)", inline=False)
        embed.add_field(name="가드시", value="-6(가드백 있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 4lk":
        embed = discord.Embed(title="murder stomp" , description = "4lk", color=0x009bcf)
        embed.add_field(name="프레임", value="23", inline=True)
        embed.add_field(name="판정", value="하단", inline=False)
        embed.add_field(name="가드시", value="-12", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 빠따" or message. content == f"{prefix}네간 4ap":
        embed = discord.Embed(title="wretched hammer" , description = "2ap", color=0x009bcf)
        embed.add_field(name="프레임", value="22", inline=True)
        embed.add_field(name="판정", value="중단(카운터시 콤보)", inline=False)
        embed.add_field(name="가드시", value="+4", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 66rp":
        embed = discord.Embed(title="justice served" , description = "66rp", color=0x009bcf)
        embed.add_field(name="프레임", value="18", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-9", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 66rk":
        embed = discord.Embed(title="savior spike" , description = "66rk", color=0x009bcf)
        embed.add_field(name="프레임", value="24", inline=True)
        embed.add_field(name="판정", value="중단(월바운드)", inline=False)
        embed.add_field(name="가드시", value="+4", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 66ap":
        embed = discord.Embed(title="gutless" , description = "66ap", color=0x009bcf)
        embed.add_field(name="프레임", value="28", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-6", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 칼빵" or  message.content == f"{prefix}네간 236lp":
        embed = discord.Embed(title="secret weapon" , description = "236lp", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="중단(히트시 밟기(2ak)확정)", inline=False)
        embed.add_field(name="가드시", value="-19", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 666rp":
        embed = discord.Embed(title="rush down" , description = "666rp", color=0x009bcf)
        embed.add_field(name="프레임", value="20", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="+9", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 기상lp rp":
        embed = discord.Embed(title="qiuck tendenrizer to intimidation" , description = "일어나면서 lp rp(rp홀드시 자세이행)", color=0x009bcf)
        embed.add_field(name="프레임", value="12", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-11", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 기상어퍼":
        embed = discord.Embed(title="malice impact to intimidation" , description = "일어나면서 rp(rp홀드시 자세이행)", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-16", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 기상lk rp":
        embed = discord.Embed(title="shock and awe" , description = "일어나면서 lk rp", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-19(가드백 있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 레드1":
        embed = discord.Embed(title="rage drive1" , description = "4lkrp", color=0x009bcf)
        embed.add_field(name="프레임", value="22", inline=True)
        embed.add_field(name="판정", value="중단(히트시 밟기(2ak)확정)", inline=False)
        embed.add_field(name="가드시", value="+8", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 레드2":
        embed = discord.Embed(title="rage drive2" , description = "4lkrp6", color=0x009bcf)
        embed.add_field(name="프레임", value="22", inline=True)
        embed.add_field(name="판정", value="중단(월바운드)", inline=False)
        embed.add_field(name="가드시", value="+6(가드백 있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}네간 레드3":
        embed = discord.Embed(title="rage drive3" , description = "4lkrp4", color=0x009bcf)
        embed.add_field(name="프레임", value="22", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-8(가드백 있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머독" or message.content == f"{prefix}머덕":
        embed = discord.Embed(title="크레이그 머독", description = "남성", color=0x009bcf)
        embed.add_field(name="나이", value="28세", inline=True)
        embed.add_field(name="출신지", value="호주", inline=True)
        embed.add_field(name="격투스타일", value="발리 투도 ", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865655200596885544/cf25bef82d0df5a31467ebdedd52a1c559a6060bb608e90d4bc22f4af135d880e39d7bd52d88cf0e6a32b18cf8ea1402f0da.png")
        await message.channel.send(embed=embed)

    
    if message.content == f"{prefix}머덕 lp rp lk ap":
        embed = discord.Embed(title="left right gut check to ready position" , description = "lp rp lk ap(ak로자세이행)", color=0x009bcf)
        embed.add_field(name="프레임", value="10", inline=True)
        embed.add_field(name="판정", value="상상중상", inline=False)
        embed.add_field(name="가드시", value="-16(3타) +4(4타)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 원투":
        embed = discord.Embed(title="left right to ready position" , description = "lp rp(ak로자세이행)", color=0x009bcf)
        embed.add_field(name="프레임", value="10", inline=True)
        embed.add_field(name="판정", value="상단", inline=False)
        embed.add_field(name="가드시", value="-1 (자세이행시 -3)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 푸싱":
        embed = discord.Embed(title="shove" , description = "ap", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단(카운터시 콤보)", inline=False)
        embed.add_field(name="가드시", value="-9", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 자세":
        embed = discord.Embed(title="ready position" , description = "ak", color=0x009bcf)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 마운트":
        embed = discord.Embed(title="double leg take down" , description = "자세도중 ap", color=0x009bcf)
        embed.add_field(name="프레임", value="24", inline=True)
        embed.add_field(name="판정", value="상단", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 자세 2ap" or message.content == f"{prefix}머덕 밥상":
        embed = discord.Embed(title="python explosion" , description = "자세도중 2ap", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="하단", inline=False)
        embed.add_field(name="가드시", value="-31", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 6rk":
        embed = discord.Embed(title="stampede" , description = "6rk", color=0x009bcf)
        embed.add_field(name="프레임", value="19", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-8", inline=False)
        await message.channel.send(embed=embed)
        
    if message.content == f"{prefix}머덕 6lk rp":
        embed = discord.Embed(title="mammoth charge" , description = "6lk rp", color=0x009bcf)
        embed.add_field(name="프레임", value="23", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-11", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 6ap":
        embed = discord.Embed(title="double thruster" , description = "6ap", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="상단(파크)", inline=False)
        embed.add_field(name="가드시", value="-10", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 6ak":
        embed = discord.Embed(title="shoulder bash cancel to reaby position" , description = "6ak(ak로캔슬,자세이행)", color=0x009bcf)
        embed.add_field(name="프레임", value="32", inline=True)
        embed.add_field(name="판정", value="상단(가불기)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 몸통박치기" or message. content == f"{prefix}머덕 6rklp":
        embed = discord.Embed(title="blitz" , description = "6rklp", color=0x009bcf)
        embed.add_field(name="프레임", value="21", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-18", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 왼어퍼" or message. content == f"{prefix}머덕 3lp":
        embed = discord.Embed(title="air lift uppercut" , description = "3lp", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-13", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 박치기" or message. content == f"{prefix}머덕 3ap":
        embed = discord.Embed(title="cannonball" , description = "6rklp", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-11", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}니슬라":
        embed = discord.Embed(title="knee slicer" , description = "2rk", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="하단", inline=False)
        embed.add_field(name="가드시", value="-16", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 2ap":
        embed = discord.Embed(title="battering ram" , description = "2ap", color=0x009bcf)
        embed.add_field(name="프레임", value="19", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-12", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 오찌":
        embed = discord.Embed(title="flash hook" , description = "1rp", color=0x009bcf)
        embed.add_field(name="프레임", value="16", inline=True)
        embed.add_field(name="판정", value="중단(카운터시 콤보)", inline=False)
        embed.add_field(name="가드시", value="-8", inline=False)
        await message.channel.send(embed=embed)


    if message.content == f"{prefix}머덕 1lk rk":
        embed = discord.Embed(title="revolving trap kick cancel to double leg take down" , description = "1lk rk(ap로캔슬,마운트)", color=0x009bcf)
        embed.add_field(name="프레임", value="18", inline=True)
        embed.add_field(name="판정", value="하중", inline=False)
        embed.add_field(name="가드시", value="-12(1타) -13(2타)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 1rk":
        embed = discord.Embed(title="crab leg" , description = "1rk", color=0x009bcf)
        embed.add_field(name="프레임", value="23", inline=True)
        embed.add_field(name="판정", value="하단", inline=False)
        embed.add_field(name="가드시", value="-26", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 1ap":
        embed = discord.Embed(title="annihilator hammer" , description = "1ap", color=0x009bcf)
        embed.add_field(name="프레임", value="26", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-22", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 4ap":
        embed = discord.Embed(title="double fist hammer" , description = "4ap", color=0x009bcf)
        embed.add_field(name="프레임", value="21", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-14", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 4rp":
        embed = discord.Embed(title="spinning blackfist" , description = "4rp", color=0x009bcf)
        embed.add_field(name="프레임", value="22", inline=True)
        embed.add_field(name="판정", value="중단(호밍기)", inline=False)
        embed.add_field(name="가드시", value="-8", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 가불기":
        embed = discord.Embed(title="death bringer cancel to double leg take down" , description = "4lkrp (ap로캔슬,마운트)", color=0x009bcf)
        embed.add_field(name="프레임", value="80", inline=True)
        embed.add_field(name="판정", value="가불기", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 9ap":
        embed = discord.Embed(title="mongoilan chop" , description = "9ap", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="상단", inline=False)
        embed.add_field(name="가드시", value="-6", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 9ak":
        embed = discord.Embed(title="foot stomp" , description = "9ak", color=0x009bcf)
        embed.add_field(name="프레임", value="31", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-3", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 바벨":
        embed = discord.Embed(title="warhammer" , description = "236rp", color=0x009bcf)
        embed.add_field(name="프레임", value="24", inline=True)
        embed.add_field(name="판정", value="하단(카운터잡기)", inline=False)
        embed.add_field(name="가드시", value="-12", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 공참각":
        embed = discord.Embed(title="bicycle kick" , description = "666lk", color=0x009bcf)
        embed.add_field(name="프레임", value="32", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="+6", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 기상lp rp":
        embed = discord.Embed(title="heavy artillery" , description = "일어나면서 lp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="11", inline=True)
        embed.add_field(name="판정", value="중상", inline=False)
        embed.add_field(name="가드시", value="-7", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 기상rp":
        embed = discord.Embed(title="tornado hook" , description = "일어나면서 rp", color=0x009bcf)
        embed.add_field(name="프레임", value="19", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-8", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 기상lk":
        embed = discord.Embed(title="power punt" , description = "일어나면서 lk", color=0x009bcf)
        embed.add_field(name="프레임", value="18", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-13", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 기상rk":
        embed = discord.Embed(title="stun knee" , description = "일어나면서 rk", color=0x009bcf)
        embed.add_field(name="프레임", value="13", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-9", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 기상ap":
        embed = discord.Embed(title="quick uppercut" , description = "일어나면서 ap", color=0x009bcf)
        embed.add_field(name="프레임", value="11", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-3", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 잡기":
        embed = discord.Embed(title="soplex bomb" , description = "641236lp", color=0x009bcf)
        embed.add_field(name="프레임", value="11", inline=True)
        embed.add_field(name="판정", value="상단(잡기)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 중단잡기":
        embed = discord.Embed(title="power bomb, ultimate knee" , description = "2al or 2ar", color=0x009bcf)
        embed.add_field(name="프레임", value="13", inline=True)
        embed.add_field(name="판정", value="중단(잡기)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 다운잡기1":
        embed = discord.Embed(title="hercules's hammer" , description = "상대방이 쓰러져 있을 떄 1al", color=0x009bcf)
        embed.add_field(name="프레임", value="18", inline=True)
        embed.add_field(name="판정", value="중단(잡기)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 다운잡기2":
        embed = discord.Embed(title="reversi throw" , description = "상대방이 쓰러져 있을 떄 발 쪽에서 1ar", color=0x009bcf)
        embed.add_field(name="프레임", value="18", inline=True)
        embed.add_field(name="판정", value="중단(잡기)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 다운잡기3":
        embed = discord.Embed(title="alarm knee" , description = "상대방이 쓰러져 있을 떄 머리 쪽에서 1ar", color=0x009bcf)
        embed.add_field(name="프레임", value="18", inline=True)
        embed.add_field(name="판정", value="중단(잡기)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}머덕 반격기":
        embed = discord.Embed(title="trap" , description = "상대방의 공격과 동시에 4al or 4ar", color=0x009bcf)

    if message.content == f"{prefix}머덕 레드":
        embed = discord.Embed(title="rage drive" , description = "6lkrp", color=0x009bcf)
        embed.add_field(name="프레임", value="21", inline=True)
        embed.add_field(name="판정", value="중단(히트시 마운트)", inline=False)
        embed.add_field(name="가드시", value="+8", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이":
        embed = discord.Embed(title="리로이 스미스", description = "남성", color=0x009bcf)
        embed.add_field(name="나이", value="50대후반~60대초반(추정)", inline=True)
        embed.add_field(name="출신지", value="미국", inline=True)
        embed.add_field(name="격투스타일", value="영춘권", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865653682909872128/5d680d0f024e6adc0557dda3840f2265abdbca61339bab90380270ada8610442b3649019d4a4deb78bb66afcc665821268cb.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 원투원":
        embed = discord.Embed(title="front palm pulsing fist" , description = "lp rp lp", color=0x009bcf)
        embed.add_field(name="프레임", value="10", inline=True)
        embed.add_field(name="판정", value="상단", inline=False)
        embed.add_field(name="가드시", value="-6(가드백 있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 원투쓰리":
        embed = discord.Embed(title="front palm xuan feng jiao" , description = "lp rp lk", color=0x009bcf)
        embed.add_field(name="프레임", value="10", inline=True)
        embed.add_field(name="판정", value="상단", inline=False)
        embed.add_field(name="가드시", value="-6", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 원투포":
        embed = discord.Embed(title="front palm snap kick to hermit" , description = "lp rp rp(자세이행)", color=0x009bcf)
        embed.add_field(name="프레임", value="10", inline=True)
        embed.add_field(name="판정", value="상상중", inline=False)
        embed.add_field(name="가드시", value="-9", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 ap ap lp":
        embed = discord.Embed(title="chain punch: stem" , description = "ap ap lp", color=0x009bcf)
        embed.add_field(name="프레임", value="12", inline=True)
        embed.add_field(name="판정", value="상상중", inline=False)
        embed.add_field(name="가드시", value="-17(3타)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 자세":
        embed = discord.Embed(title="hermit" , description = "ak", color=0x009bcf)
        embed.add_field(name="상대 하단공격 자동반격", value="", inline=True)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 자세 lp":
        embed = discord.Embed(title="tan zhang" , description = "hermit 도중 lp", color=0x009bcf)
        embed.add_field(name="프레임", value="24", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-9", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 자세 rp lp":
        embed = discord.Embed(title="horizontal elbow stlike" , description = "hermit 도중 rp lp", color=0x009bcf)
        embed.add_field(name="프레임", value="12", inline=True)
        embed.add_field(name="판정", value="상단", inline=False)
        embed.add_field(name="가드시", value="-4", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 자세 lk rk":
        embed = discord.Embed(title="stampeding dragon" , description = "hermit 도중 lk rk", color=0x009bcf)
        embed.add_field(name="프레임", value="16", inline=True)
        embed.add_field(name="판정", value="하중", inline=False)
        embed.add_field(name="가드시", value="-13(1타) -15(2타)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 자세 rk ap":
        embed = discord.Embed(title="caution dragon" , description = "hermit 도중 rk ap", color=0x009bcf)
        embed.add_field(name="프레임", value="11", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-14(2타)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 자세 ap":
        embed = discord.Embed(title="twin dragon stlike" , description = "hermit 도중 ap", color=0x009bcf)
        embed.add_field(name="프레임", value="16", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-10", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 자세 6lp":
        embed = discord.Embed(title="villain slayer" , description = "hermit 도중 6lp", color=0x009bcf)
        embed.add_field(name="프레임", value="16", inline=True)
        embed.add_field(name="판정", value="상단", inline=False)
        embed.add_field(name="가드시", value="0", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 자세 6rk":
        embed = discord.Embed(title="duan tou xuan feng jiao" , description = "hermit 도중 6rk", color=0x009bcf)
        embed.add_field(name="프레임", value="26", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="0", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 자세 4lp":
        embed = discord.Embed(title="prayer fist" , description = "hermit 도중 4lp", color=0x009bcf)
        embed.add_field(name="프레임", value="20", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="+4", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 자세 4rk":
        embed = discord.Embed(title="razor saweep" , description = "hermit 도중 4rk", color=0x009bcf)
        embed.add_field(name="프레임", value="20", inline=True)
        embed.add_field(name="판정", value="하단(호밍기)", inline=False)
        embed.add_field(name="가드시", value="-13", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 lkrp":
        embed = discord.Embed(title="go sugar" , description = "lkrp", color=0x009bcf)
        embed.add_field(name="프레임", value="110", inline=True)
        embed.add_field(name="판정", value="하단", inline=False)
        embed.add_field(name="가드시", value="-16(거리에 따라 달라짐)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 6rk rk":
        embed = discord.Embed(title="lao weng xuan feng joao" , description = "6rk rk", color=0x009bcf)
        embed.add_field(name="프레임", value="16", inline=True)
        embed.add_field(name="판정", value="중상", inline=False)
        embed.add_field(name="가드시", value="-6", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 가불기":
        embed = discord.Embed(title="piercing charge" , description = "6ak6", color=0x009bcf)
        embed.add_field(name="프레임", value="56", inline=True)
        embed.add_field(name="판정", value="가불기", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 3lp lp":
        embed = discord.Embed(title="chopping chain fist" , description = "3lp lp", color=0x009bcf)
        embed.add_field(name="프레임", value="13", inline=True)
        embed.add_field(name="판정", value="중상", inline=False)
        embed.add_field(name="가드시", value="-1", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 왼어퍼포":
        embed = discord.Embed(title="copping snap kick to hermit" , description = "3lp rk(자세이행)", color=0x009bcf)
        embed.add_field(name="프레임", value="13", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-9", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 떠퍼":
        embed = discord.Embed(title="rising dragon" , description = "3rp ap", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-18(2타)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 3rk":
        embed = discord.Embed(title="snap kick to hermit" , description = "3rk(자세이행)", color=0x009bcf)
        embed.add_field(name="프레임", value="13", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-6", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 3rk lk":
        embed = discord.Embed(title="snap kick knee" , description = "3rk lk", color=0x009bcf)
        embed.add_field(name="프레임", value="13", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-9", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 파크":
        embed = discord.Embed(title="cornered dragon" , description = "3ap", color=0x009bcf)
        embed.add_field(name="프레임", value="24", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-14", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 2rp rk":
        embed = discord.Embed(title="falling fist aweep" , description = "2rp rk", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="하단", inline=False)
        embed.add_field(name="가드시", value="-15(1타) -13(2타)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 로하이":
        embed = discord.Embed(title="twin snake stlike to hermit" , description = "2lk rp(자세이행)", color=0x009bcf)
        embed.add_field(name="프레임", value="16", inline=True)
        embed.add_field(name="판정", value="하상", inline=False)
        embed.add_field(name="가드시", value="-13(1타)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 2rk rk":
        embed = discord.Embed(title="razor kick to hermit" , description = "2rk rk(자세이행)", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="하중", inline=False)
        embed.add_field(name="가드시", value="-12(1타) -11(2타)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 2ap":
        embed = discord.Embed(title="chanhui zhang" , description = "2ap", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-4", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 나락":
        embed = discord.Embed(title="twin dragon acceptanance" , description = "1lk ap", color=0x009bcf)
        embed.add_field(name="프레임", value="18", inline=True)
        embed.add_field(name="판정", value="하중", inline=False)
        embed.add_field(name="가드시", value="-26(1타) -16(2타)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 1rk":
        embed = discord.Embed(title="fan sweep" , description = "1rk", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="하단", inline=False)
        embed.add_field(name="가드시", value="-14", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 4lp":
        embed = discord.Embed(title="knee snap" , description = "4lp", color=0x009bcf)
        embed.add_field(name="프레임", value="11", inline=True)
        embed.add_field(name="판정", value="상단(카운터 잡기)", inline=False)
        embed.add_field(name="가드시", value="-6", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 4rk":
        embed = discord.Embed(title="zhuan shen jiao" , description = "4rk", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="중단(호밍기)", inline=False)
        embed.add_field(name="가드시", value="-8", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 촌경":
        embed = discord.Embed(title="outcast arrow" , description = "4ap", color=0x009bcf)
        embed.add_field(name="프레임", value="12", inline=True)
        embed.add_field(name="판정", value="중단(카운터시 콤보)", inline=False)
        embed.add_field(name="가드시", value="-9", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 9rp":
        embed = discord.Embed(title="zhuan shen long fang quan" , description = "9rp", color=0x009bcf)
        embed.add_field(name="프레임", value="24", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="+1", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 플라잉휠":
        embed = discord.Embed(title="floating axe drop" , description = "9rk", color=0x009bcf)
        embed.add_field(name="프레임", value="23", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-8", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 236rp":
        embed = discord.Embed(title="chakra fist" , description = "236rp", color=0x009bcf)
        embed.add_field(name="프레임", value="16", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-6", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 공참각":
        embed = discord.Embed(title="dragon's heel" , description = "666lk", color=0x009bcf)
        embed.add_field(name="프레임", value="24", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="+7", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 기상 lp rk":
        embed = discord.Embed(title="elbow slash snap kick to hermit" , description = "일어남녀서 lp rk(자세이행)", color=0x009bcf)
        embed.add_field(name="프레임", value="13", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-6", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 기상 어퍼":
        embed = discord.Embed(title="arrow shower" , description = "일어나면서 rp", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-14", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 기상 lk ap rk":
        embed = discord.Embed(title="stlike of the five precepts" , description = "일어나면서 lk ap rk", color=0x009bcf)
        embed.add_field(name="프레임", value="14", inline=True)
        embed.add_field(name="판정", value="중상중", inline=False)
        embed.add_field(name="가드시", value="-12(2타) -16(3타)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 횡신 rk":
        embed = discord.Embed(title="lone drgon slice" , description = "횡신 rk", color=0x009bcf)
        embed.add_field(name="프레임", value="18", inline=True)
        embed.add_field(name="판정", value="하단", inline=False)
        embed.add_field(name="가드시", value="-12", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 1rp ap":
        embed = discord.Embed(title="tremor punch" , description = "상대방이 쓰러져 있을 때 1rp ap", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="하단", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}지팡이"or message. content == f"{prefix}킹팡이":
        embed = discord.Embed(title="master's lesson" , description = "3lkrp(한 시합에 한 번)", color=0x009bcf)
        embed.add_field(name="프레임", value="22", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-7", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 패링":
        embed = discord.Embed(title="twin dragon gate" , description = "4rp(패링후 lp or rp)", color=0x009bcf)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리로이 레드":
        embed = discord.Embed(title="rage drive" , description = "6ap", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="+2(가드백 있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진" or message.content == f"{prefix}뎁둘기":
        embed = discord.Embed(title="데빌진", description = "남성", color=0x009bcf)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865649328580067344/5f8c15549b8549dbfc226de000a4cabdddc121fb1354aae9770cb7378a558202b639997de8a0a2f65622673f2acac4618d65.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 원투투":
        embed = discord.Embed(title="demon slyaer" , description = "lp rp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="10", inline=True)
        embed.add_field(name="판정", value="상단", inline=False)
        embed.add_field(name="가드시", value="-12", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}비공" or message.content == f"{prefix}데빌진 ak":
        embed = discord.Embed(title="fly" , description = "ak", color=0x009bcf)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 자세lp":
        embed = discord.Embed(title="near death" , description = "비공중 lp", color=0x009bcf)
        embed.add_field(name="프레임", value="18", inline=True)
        embed.add_field(name="판정", value="상단(카운터시 스크류)", inline=False)
        embed.add_field(name="가드시", value="-8(가드백 있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 자세rp":
        embed = discord.Embed(title="infernal annihilation" , description = "비공중 rp", color=0x009bcf)
        embed.add_field(name="프레임", value="36", inline=True)
        embed.add_field(name="판정", value="상단가불기(타격잡기)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 자세lk":
        embed = discord.Embed(title="amara" , description = "비공중 lk", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-15", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 자세ap":
        embed = discord.Embed(title="infernal destruction" , description = "비공중 ap", color=0x009bcf)
        embed.add_field(name="프레임", value="50", inline=True)
        embed.add_field(name="판정", value="가불기", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 자세6ap":
        embed = discord.Embed(title="cross infernal destruction" , description = "비공중 6ap", color=0x009bcf)
        embed.add_field(name="프레임", value="44", inline=True)
        embed.add_field(name="판정", value="가불기", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 6rk lk":
        embed = discord.Embed(title="twisted samsara" , description = "6rk lk(8입력시 비공이행)", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-33(2타) -13(비공 이행시)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 6ap":
        embed = discord.Embed(title="tsujikage" , description = "6ap(4입력으로 캔슬)", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="중단(호밍기)", inline=False)
        embed.add_field(name="가드시", value="-12(2타) -18(캔슬시)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 6ak":
        embed = discord.Embed(title="hisou" , description = "6ak", color=0x009bcf)
        embed.add_field(name="프레임", value="16", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-16", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 왼어퍼투":
        embed = discord.Embed(title="twin lancer" , description = "3lp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="13", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-8", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 3rk rk":
        embed = discord.Embed(title="tsunami kick" , description = "3rk rk", color=0x009bcf)
        embed.add_field(name="프레임", value="13", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-15(2타)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 파크":
        embed = discord.Embed(title="corpse thrust" , description = "2lp", color=0x009bcf)
        embed.add_field(name="프레임", value="18", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="-14", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 2lk":
        embed = discord.Embed(title="broken plate" , description = "2lk", color=0x009bcf)
        embed.add_field(name="프레임", value="18", inline=True)
        embed.add_field(name="판정", value="하단", inline=False)
        embed.add_field(name="가드시", value="-12", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 악마손":
        embed = discord.Embed(title="malicious mace" , description = "1rp", color=0x009bcf)
        embed.add_field(name="프레임", value="2", inline=True)
        embed.add_field(name="판정", value="하단(카운터시 대쉬뻥발 확정)", inline=False)
        embed.add_field(name="가드시", value="-13", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}카메하메하":
        embed = discord.Embed(title="demopn's spear" , description = "1(H)ap", color=0x009bcf)
        embed.add_field(name="프레임", value="61(홀드시)", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value="+17(홀드시)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 4lp rp":
        embed = discord.Embed(title="brimstone strike" , description = "4lp rp(4입력으로 캔슬)", color=0x009bcf)
        embed.add_field(name="프레임", value="12", inline=True)
        embed.add_field(name="판정", value="상중", inline=False)
        embed.add_field(name="가드시", value="-18(캔슬시) -14(2타)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 4rp lp":
        embed = discord.Embed(title="rakshasa's rampage to heaven's door" , description = "4rp lp(히트시 9입력)", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="상중", inline=False)
        embed.add_field(name="가드시", value="-15(1타) -16(2타)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 뻥발":
        embed = discord.Embed(title="devil's steel petal", description = "4rk", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="중단(카운터시 콤보)", inline=False)
        embed.add_field(name="가드시", value=" -8", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 가불기":
        embed = discord.Embed(title="lighting uppercut", description = "4pklp", color=0x009bcf)
        embed.add_field(name="프레임", value="43(홀드시63)", inline=True)
        embed.add_field(name="판정", value="가불기", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 7ap":
        embed = discord.Embed(title="hellfire blast", description = "7ap", color=0x009bcf)
        embed.add_field(name="프레임", value="40", inline=True)
        embed.add_field(name="판정", value="상단가불기", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}윤회":
        embed = discord.Embed(title="samsara", description = "8rk(8홀드시 비공이행)", color=0x009bcf)
        embed.add_field(name="프레임", value="20", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -36, -16(비공이행시)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 9lk":
        embed = discord.Embed(title="peaper's scythe", description = "9lk", color=0x009bcf)
        embed.add_field(name="프레임", value="28", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" +3", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}비혼축":
        embed = discord.Embed(title="wraith kick", description = "9rk", color=0x009bcf)
        embed.add_field(name="프레임", value="18", inline=True)
        embed.add_field(name="판정", value="중단(히트시 뻥발 확정)", inline=False)
        embed.add_field(name="가드시", value=" -8", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 통발":
        embed = discord.Embed(title="demon's paw", description = "66rp", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -8(가드백있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 66rk":
        embed = discord.Embed(title="last rites", description = "66rk", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="상단(호밍기)", inline=False)
        embed.add_field(name="가드시", value=" +5(가드백 있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}나살문":
        embed = discord.Embed(title="laser cannon", description = "46rp lp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -10(2타) ,-8(3타, 가드백 있음)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 나락":
        embed = discord.Embed(title="spinning demon", description = "6n23rk rk", color=0x009bcf)
        embed.add_field(name="프레임", value="16", inline=True)
        embed.add_field(name="판정", value="하중", inline=False)
        embed.add_field(name="가드시", value=" -23(1타), -16(2타)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 공참각":
        embed = discord.Embed(title="leaping side kick", description = "666lk", color=0x009bcf)
        embed.add_field(name="프레임", value="22", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" +9", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 기상lp rp":
        embed = discord.Embed(title="twin pitons", description = "일어나면서 lp rp", color=0x009bcf)
        embed.add_field(name="프레임", value="13", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -7", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 기상lp rk":
        embed = discord.Embed(title="twin revival", description = "일어나면서 lp rk", color=0x009bcf)
        embed.add_field(name="프레임", value="13", inline=True)
        embed.add_field(name="판정", value="중상", inline=False)
        embed.add_field(name="가드시", value=" -5", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 기상rp":
        embed = discord.Embed(title="uppercut", description = "일어나면서 rp", color=0x009bcf)
        embed.add_field(name="프레임", value="15", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -12", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 기상킥" :
        embed = discord.Embed(title="tsuanmi kick", description = "일어나면서 rk rk", color=0x009bcf)
        embed.add_field(name="프레임", value="11", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -15(2타)", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 데빌 트위스터" or message.content == f"{prefix}데빌진 횡rp" :
        embed = discord.Embed(title="devil twister", description = "횡신 rp(지상히트시 8입력)", color=0x009bcf)
        embed.add_field(name="프레임", value="17", inline=True)
        embed.add_field(name="판정", value="중단", inline=False)
        embed.add_field(name="가드시", value=" -22", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 2ap" :
        embed = discord.Embed(title="hellfire incinerator", description = "상대방이 쓰러져 있을 때 2ap", color=0x009bcf)
        embed.add_field(name="프레임", value="25", inline=True)
        embed.add_field(name="판정", value="하단", inline=False)
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}데빌진 레드" :
        embed = discord.Embed(title="rage drive", description = "6n23rk ak", color=0x009bcf)
        embed.add_field(name="프레임", value="16", inline=True)
        embed.add_field(name="판정", value="하중", inline=False)
        embed.add_field(name="가드시", value=" -14(2타)", inline=False)
        await message.channel.send(embed=embed)
        

    if message.content == f"{prefix}화랑"or message.content == f"{prefix}솟랑":
        embed = discord.Embed(title="화랑(별명)", description = "남성", color=0x009bcf)
        embed.add_field(name="나이", value="21세", inline=True)
        embed.add_field(name="출신지", value="한국", inline=True)
        embed.add_field(name="격투스타일", value="ITF태권도", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865645706429202472/7b8bf3dbe5db31c7d3e381f98cffe3cd0c332989715f39f2a798ffb63d26c15acd8a1ae025ff8d62fdef7b306f0c29040e6f.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}간류":
        embed = discord.Embed(title="간류", description = "남성", color=0x009bcf)
        embed.add_field(name="나이", value="55세", inline=True)
        embed.add_field(name="출신지", value="일본", inline=True)
        embed.add_field(name="격투스타일", value="스모", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865646856108900372/8a768955a0f73d304f0998c98644663197ec9aee6f3c81720546eb318ce4bb91ad99e667bf2d828ed88d32e488dab6a1f8c2.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}기가스":
        embed = discord.Embed(title="기가스", description = "불명", color=0x009bcf)
        embed.add_field(name="나이", value="불명", inline=True)
        embed.add_field(name="출신지", value="불명", inline=True)
        embed.add_field(name="격투스타일", value="파괴충동", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865647262750605353/042c4a49e12bd50846ecf20aa80f4b89bc3b37c5836da38ba5d009702dc4afaf659fa94868012a6b76b90b1dadae9e57b4aa.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}기스":
        embed = discord.Embed(title="기스 하워드", description = "남성", color=0x009bcf)
        embed.add_field(name="나이", value="67세(추정)", inline=True)
        embed.add_field(name="출신지", value="미국", inline=True)
        embed.add_field(name="격투스타일", value="고무술", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865647695929933824/89c745d1da89f90830d5e46b6404f937d692cfae9d09b71034d8638991b8360053b9c7ffe773b969f07ef3e4e6ba1437533b.png")
        await message.channel.send(embed=embed)


    if message.content == f"{prefix}니나":
        embed = discord.Embed(title="니나 윌리엄스", description = "여성", color=0x009bcf)
        embed.add_field(name="나이", value="43세(신체나이 24세)", inline=True)
        embed.add_field(name="출신지", value="아일랜드", inline=True)
        embed.add_field(name="격투스타일", value="암살격투술", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865648716908199956/d580baf1dc6a1796560cf417e6cfb899e5a18ad7013a054ccafdb9d4682cf38a662d71d5b55d7b5aef2a7d8619d23bf9d994.png")
        await message.channel.send(embed=embed)


    if message.content == f"{prefix}드라구노프":
        embed = discord.Embed(title="세르게이 드라구노프", description = "남성", color=0x009bcf)
        embed.add_field(name="나이", value="26세", inline=True)
        embed.add_field(name="출신지", value="러시아", inline=True)
        embed.add_field(name="격투스타일", value="컴뱃 삼보", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865649874942558208/b2dff2c948666b87e451d1c0c0eecc5c2d399be8423857e37e33ba135baa7207a962ac915b2c03fc4de793a1cc9eec3ed317.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}라스":
        embed = discord.Embed(title="라스 알렉산데르손", description = "남성", color=0x009bcf)
        embed.add_field(name="나이", value="28세", inline=True)
        embed.add_field(name="출신지", value="스웨덴", inline=True)
        embed.add_field(name="격투스타일", value="철권중 특수부대 격투술", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865650294067167242/49f459cde5fa9ccc6f09b070067b7256f7879bd13006a2c2af98aed04cc38a8bb2e3a9145358ff82cd227515a2d4e5935c8b.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}럭키":
        embed = discord.Embed(title="럭키 클로에(예명)", description = "여성", color=0x009bcf)
        embed.add_field(name="나이", value="20대로추정", inline=True)
        embed.add_field(name="출신지", value="불명", inline=True)
        embed.add_field(name="격투스타일", value="자유형 율동", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865650760057356288/7b1373a86135002eb933f1a506db3a8d31d1b4b7b974b99ea7bebc0abae9a874b49c3abb8fdb8dd4b254bb20ad6db609748d.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}레오":
        embed = discord.Embed(title="엘'레오'노르 클리젠", description = "불명", color=0x009bcf)
        embed.add_field(name="나이", value="19세", inline=True)
        embed.add_field(name="출신지", value="독일", inline=True)
        embed.add_field(name="격투스타일", value="팔극권", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865651345804230696/378690dfa80196792a49c1bdbb061ac6e227c012ee1b76431e570fc25accf2869630ecb28f2877f46c44cb4c5c4503045f5b.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}레이":
        embed = discord.Embed(title="레이 우롱", description = "남성", color=0x009bcf)
        embed.add_field(name="나이", value="47세", inline=True)
        embed.add_field(name="출신지", value="홍콩", inline=True)
        embed.add_field(name="격투스타일", value="오형권+각종 권법+취권", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865651906236252160/cb242dc72ca49d3017f50af63c4fd23b8fd604e0c0ddefa4bd20a5cf4c6ebc4de1ff70975c098f180880da853aada0bb92eb.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}로우":
        embed = discord.Embed(title="마샬 로우", description = "남성", color=0x009bcf)
        embed.add_field(name="나이", value="48세", inline=True)
        embed.add_field(name="출신지", value="미국(중국계 미국인)", inline=True)
        embed.add_field(name="격투스타일", value="마샬아츠", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865652324306649148/b3ccfa3138321262795e6c29b3fe69302ad39ac7aa23d52f051051b63050ae62315b17a9d2c220f0c91a654778bf3024b40f.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리":
        embed = discord.Embed(title="리 차오랑", description = "남성", color=0x009bcf)
        embed.add_field(name="나이", value="48세", inline=True)
        embed.add_field(name="출신지", value="일본(중국출생)", inline=True)
        embed.add_field(name="격투스타일", value="마샬아츠", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865652732492251146/1686fc87ae0efe178e4ef0138d19569a233b6336288070a6549c9e7db01fbc13d2048eec57bab5823a991de2468eba28a460.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}리디아":
        embed = discord.Embed(title="리디아 소비에스카", description = "여성", color=0x009bcf)
        embed.add_field(name="나이", value="29세", inline=True)
        embed.add_field(name="출신지", value="폴란드", inline=True)
        embed.add_field(name="격투스타일", value="전통파 가라테", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865653099971739708/881ab5f0b78a072a54267e68b4a3fc269798bc96253cc646da166fb784479554b2f76da9e0acb0027b5561d533c99b5bfd2b.png")
        await message.channel.send(embed=embed)

    

    if message.content == f"{prefix}리리":
        embed = discord.Embed(title="에밀리 드 로슈포르", description = "여성", color=0x009bcf)
        embed.add_field(name="나이", value="16세", inline=True)
        embed.add_field(name="출신지", value="모나코", inline=True)
        embed.add_field(name="격투스타일", value="트릭킹", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865654294544253019/f56a9a7685e037a17c73c0931f2a6f6235d4499070b60037c058ee19010eb200011720c2f580647cbb74ef2dc9196eda5d76.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}마레":
        embed = discord.Embed(title="마스터 레이븐", description = "여성", color=0x009bcf)
        embed.add_field(name="나이", value="불명", inline=True)
        embed.add_field(name="출신지", value="불명", inline=True)
        embed.add_field(name="격투스타일", value="닌자술", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865654617902809108/5c6a7911cc1a5174e68746494d4945524844cccd6f7f90ebcc2bf6607fca5f2816f86c227d6c19f33c6515d02a8164f53b2a.png")
        await message.channel.send(embed=embed)

    

    if message.content == f"{prefix}미겔":
        embed = discord.Embed(title="미겔 카바예로 로호", description = "남성", color=0x009bcf)
        embed.add_field(name="나이", value="26세", inline=True)
        embed.add_field(name="출신지", value="스페인", inline=True)
        embed.add_field(name="격투스타일", value="없음 ", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865655659487690773/175060232298d8432c97bdc557386f14f00fff4762acffd83696000548a6b9c40b96b7bc9fbbcc2ca603fa650e4489b0455a.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}밥":
        embed = discord.Embed(title="로버트 리쳐드", description = "남성", color=0x009bcf)
        embed.add_field(name="출신지", value="미국", inline=True)
        embed.add_field(name="격투스타일", value="자유형 가라테 ", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865656069735841852/50042dce268e5c973edfdbd17cb79212712a0f7feaf3041d7bbc57d5c71b4a126267dcd269b2930cf7ad54ebf87dbb47cc78.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}브라이언":
        embed = discord.Embed(title="브라이언 퓨리", description = "남성", color=0x009bcf)
        embed.add_field(name="나이", value="31세", inline=True)
        embed.add_field(name="출신지", value="미국", inline=True)
        embed.add_field(name="격투스타일", value="킥복싱 ", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865656364666978344/1fb12b9e3e5e517ed832942b00a9ccd2d96ec1636e07f799522c584a825d0bea8771e7afea098d8ca708a58b17c6df3d7ce4.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}샤오유":
        embed = discord.Embed(title="링 샤오유", description = "여성", color=0x009bcf)
        embed.add_field(name="나이", value="18세", inline=True)
        embed.add_field(name="출신지", value="중국", inline=True)
        embed.add_field(name="격투스타일", value="팔괘장, 벽괘장 + 각종 중국 권법 ", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865656835553230880/282403cd19a4fc0861f54ab6b014a4624f833ec187f41e69ba589ebb9111eaf9d1b259aaa224e0d4bb95a17d5e61c6c6adca.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}스티브":
        embed = discord.Embed(title="스티브 폭스", description = "남성", color=0x009bcf)
        embed.add_field(name="나이", value="32세", inline=True)
        embed.add_field(name="출신지", value="영국", inline=True)
        embed.add_field(name="격투스타일", value="복싱 ", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865657488006447174/42e8c39f6aeb81df5601854edcdb38205d3e87982656d2b9959d4138f29ceba39b38a6d7765a0c98891d71a2bf6714b37e1f.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}아머킹":
        embed = discord.Embed(title="아머킹", description = "남성", color=0x009bcf)
        embed.add_field(name="격투스타일", value="프로레슬링 ", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865657644484001842/365b0c2b7f3665b61e148089feff8a6291b0ed27f9d21cbbea1024613cc243b1bf24f98b58bd99618ec41a65c67bd905d4c9.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}아스카":
        embed = discord.Embed(title="아스카 카자마", description = "여성", color=0x009bcf)
        embed.add_field(name="나이", value="17세", inline=True)
        embed.add_field(name="출신지", value="일본", inline=True)
        embed.add_field(name="격투스타일", value="카자마류 고무술 ", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865658373680005120/c19574eff46836618a87ec58b52858215f7561b0feaddfcede38ba19ea1a97c163ec19be39a6c7e9ca85ed4bd8a395811236.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}고우키"or message.content == f"{prefix}아쿠마":
        embed = discord.Embed(title="고우키", description = "남성", color=0x009bcf)
        embed.add_field(name="나이", value="불명", inline=True)
        embed.add_field(name="출신지", value="일본", inline=True)
        embed.add_field(name="격투스타일", value="불명", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865658478840512522/8e7010ea99ad5ff9c9b01a5dc90ec56fcec89b6923fa700e6b5568fd5922abb47423c09460e24a5cc654ebe3670401308008.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}안나":
        embed = discord.Embed(title="안나윌리엄스", description = "여성", color=0x009bcf)
        embed.add_field(name="나이", value="41세", inline=True)
        embed.add_field(name="출신지", value="아일랜드", inline=True)
        embed.add_field(name="격투스타일", value="암살 격투술 ", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865887673733349386/24ea3d1d6b9c1ae574188ac213b304a867c2e837e5cbec47c3c666c740098d1c204e46141132550b675034808d0d4bd4a103.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}알리사":
        embed = discord.Embed(title="알리사 보스코노비치", description = "여성", color=0x009bcf)
        embed.add_field(name="나이", value="불명", inline=True)
        embed.add_field(name="출신지", value="러시아", inline=True)
        embed.add_field(name="격투스타일", value="반동추진기를 이용한고강도 기동전투", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865888076457967626/5adc17218a5124a87530fb84deb35d7ec9e34c9fbe12701f85e736de41fb2ffd3344c466bea1bb20c659577a99dbda60ab05.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}에디":
        embed = discord.Embed(title="에디 고르두", description = "남성", color=0x009bcf)
        embed.add_field(name="나이", value="29세", inline=True)
        embed.add_field(name="출신지", value="브라질", inline=True)
        embed.add_field(name="격투스타일", value="카포에라", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865888656416571443/3144e39ad7d562fc3b6a88bd78e714bbb4fc881f5d90208261b76cbf210ccdd3282b3e9b627fb4b3cf9a8f7d08f382cee857.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}엘리자":
        embed = discord.Embed(title="엘리자", description = "여성", color=0x009bcf)
        embed.add_field(name="나이", value="1000세(추정)", inline=True)
        embed.add_field(name="출신지", value="루마니아", inline=True)
        embed.add_field(name="격투스타일", value="불명", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865889030527647754/0d867341a4577d901890ecfe0b498b86952b8fba86c5b46d06d2b0121d213e4e056e4af3b85c71e178d175a4c1acf4c38d66.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}요시미츠" or message. content == f"{prefix}요시":
        embed = discord.Embed(title="요시미츠", description = "남성", color=0x009bcf)
        embed.add_field(name="나이", value="불명", inline=True)
        embed.add_field(name="출신지", value="없음(전 일본)", inline=True)
        embed.add_field(name="격투스타일", value="만인술 진화형", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865889638535397376/9c7c802c3d76091fbbc09a34744522571dd47865a8e161d639d77692dfdde338e97c8ca872a65dfd2c1c2f9983f95fc2a1d9.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}자피나":
        embed = discord.Embed(title="자피나", description = "여성", color=0x009bcf)
        embed.add_field(name="나이", value="23세", inline=True)
        embed.add_field(name="출신지", value="이집트(추정)", inline=True)
        embed.add_field(name="격투스타일", value="고대 암살술", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/869231220997881896/4332abded459d60461e17a5f5135fa326a8f2fc84d76a410f48970baaaa5cd15086e3b271fc1a78a3992968138ddd9af29b0.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}잭":
        embed = discord.Embed(title="잭-7", description = "", color=0x009bcf)
        embed.add_field(name="생산지", value="로켓공학연구소", inline=True)
        embed.add_field(name="격투스타일", value="힘으로 밀어붙이기", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/869231172297834596/e50b2b85abd47ae0bd4203c99c654551c3fa0e6bdb0c8518916fd73e83c7322760907398c66b689b25e0f1f2b96d91568a2e.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}조시":
        embed = discord.Embed(title="조시 리잘", description = "여성", color=0x009bcf)
        embed.add_field(name="나이", value="불명", inline=True)
        embed.add_field(name="출신지", value="필라핀", inline=True)
        embed.add_field(name="격투스타일", value="에스크리마 기반 킥복싱", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865891259183923240/468ec31acbe7fbb73306aed7ba6a94c1ed1fc0d450d3a1349d3e75a3fb5bd728469d83a283d5cd302e885462679844fd3477.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}줄리아":
        embed = discord.Embed(title="줄리아 창", description = "여성", color=0x009bcf)
        embed.add_field(name="나이", value="20세", inline=True)
        embed.add_field(name="출신지", value="미국(아메리카 원주민)", inline=True)
        embed.add_field(name="격투스타일", value="심의육합권 및 팔극권 기반 각종 권법", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/869231277134446602/ea335598e15275d390559873b435311d400d3c37279dc49568772b193aa91034ce1ea46046d01f9416016128d8867826daec.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}진" or message.content == f"{prefix}놈진":
        embed = discord.Embed(title="카자마 진", description = "남성", color=0x009bcf)
        embed.add_field(name="나이", value="21세", inline=True)
        embed.add_field(name="출신지", value="일본", inline=True)
        embed.add_field(name="격투스타일", value="정통 가라테", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/869231354653601842/4e1a9e86d40836b3cd63f72c7b0491af035bddbb9ee44b099b1ed22c70f3bc7c667b3456da60d57f4c6340165a20a89086fd.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}카즈미":
        embed = discord.Embed(title="미시마 카즈미", description = "여성", color=0x009bcf)
        embed.add_field(name="나이", value="불명", inline=True)
        embed.add_field(name="출신지", value="일본", inline=True)
        embed.add_field(name="격투스타일", value="하치조류 가라테", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/869231392431685632/77665e762de42ce1889f99390fe88e5cf4dc9bb217d765e583191c5c9c961dbf2cafbd7b10d4ac194a70859deb48b6823b4a.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}카타리나":
        embed = discord.Embed(title="카타리나 아우베스", description = "여성", color=0x009bcf)
        embed.add_field(name="나이", value="20대중반~30대초반으로추정", inline=True)
        embed.add_field(name="출신지", value="브라질", inline=True)
        embed.add_field(name="격투스타일", value="사바트", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/869232389208027206/fdf23bbb14531ce5d8ff532310db83547af7d75634067e401b7cded15fedf9f1c47917b7d88cd1bbac4a01a8aae3202d9732.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}쿠니미츠" or message.content == f"{prefix}쿠니":
        embed = discord.Embed(title="쿠니미츠", description = "여성", color=0x009bcf)
        embed.add_field(name="나이", value="불명", inline=True)
        embed.add_field(name="출신지", value="일본", inline=True)
        embed.add_field(name="격투스타일", value="만인술", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/869231437658882098/c1daaa7a178172b59979c2af037e0dc9f9df2cd6ee3b0028fcfa29ed8f9517e0ff6ac2642aa434120416665242a536a5b3d0.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}쿠마":
        embed = discord.Embed(title="쿠마", description = "수컷", color=0x009bcf)
        embed.add_field(name="나이", value="사람나이로 18~20", inline=True)
        embed.add_field(name="출신지", value="없음", inline=True)
        embed.add_field(name="격투스타일", value="헤이하치류 웅진권(개량형)", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/869231474690371594/c619f3c8441ca891c04c9f49d1fe1a5b394379fa9db22609f9f37e2038191f25c8dc30c5b20dc30a799815c141f9e2613f47.png")
        await message.channel.send(embed=embed)


    if message.content == f"{prefix}킹":
        embed = discord.Embed(title="킹", description = "남성", color=0x009bcf)
        embed.add_field(name="나이", value="30세", inline=True)
        embed.add_field(name="출신지", value="멕시코", inline=True)
        embed.add_field(name="격투스타일", value="프로레슬링", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/869231558052163604/ab4d7bd7459c538eb2a451a09ced2f406678a567fdfbf20ad1f3cc17820f3ca928d09d2fbe9f0fa80e4efc1467308246d10e.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}파캄람"or  message.content == f"{prefix}파쿰람":
        embed = discord.Embed(title="파캄람", description = "남성", color=0x009bcf)
        embed.add_field(name="나이", value="28세", inline=True)
        embed.add_field(name="출신지", value="태국", inline=True)
        embed.add_field(name="격투스타일", value="무에타이", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/865900834977742858/321cd7c7292ef5c3e9a703c756e017a149ee9d87a0426a82184deaedcc7f3237668c1bf3d791c9a73d1a0dd7a4f1b4650892.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}판다":
        embed = discord.Embed(title="판다", description = "암컷", color=0x009bcf)
        embed.add_field(name="나이", value="사람 나이로 16~18세", inline=True)
        embed.add_field(name="출신지", value="중국", inline=True)
        embed.add_field(name="격투스타일", value="헤이하치류 웅진권 (개량형)", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/869231616441090058/d9b727a155013265d1e6760499c6099db1951e6eddd6c7166208c675949a854c024579a910c0f322ca3db01c88ed89b2aa88.png")
        await message.channel.send(embed=embed)

    if message.content == f"{prefix}펭":
        embed = discord.Embed(title="펑 웨이", description = "남성", color=0x009bcf)
        embed.add_field(name="나이", value="26세", inline=True)
        embed.add_field(name="출신지", value="중국", inline=True)
        embed.add_field(name="격투스타일", value="신권류 중국권법", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/869231654395314247/ebf15896cad3e69042edf79585aa2ea7a902f2ee4fb4e03ceccf035a40a8f46add2d54959f6cc37e594b577528c67c4d6cee.png")
        await message.channel.send(embed=embed)

    
    if message.content == f"{prefix}헤이하치":
        embed = discord.Embed(title="미시마 헤이하치", description = "남성", color=0x009bcf)
        embed.add_field(name="나이", value="75세", inline=True)
        embed.add_field(name="출신지", value="일본", inline=True)
        embed.add_field(name="격투스타일", value="미시마류 싸움 가라테", inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/865482695256440843/869231763510140988/212a89e5d369e75a9b83ccb3d9f1c6edcb7bd9c432980dd8c39d7836a313987270835589bedd49526bb9e4a78caf9df31d86.png")
        await message.channel.send(embed=embed)

    


    
    




    







    







  


client.run(os.environ['token'])
