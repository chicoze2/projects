import discord
import asyncio
from discord.colour import Color
from discord.ext import commands, tasks
from discord.utils import get
from itertools import cycle
import time
import json
from datetime import datetime

intents = discord.Intents.all()
intents.members = True
bot_prefix = '!'
client = commands.Bot(command_prefix=bot_prefix, intents = intents)
status = cycle(['👟 ┇ Prime Notifier', 'Bot por chicoze2#6809 🥳', 'Prefixo: !'])
now = datetime.now()


## EDIT

canalLogs = 838862609876910121
cargoBetaTester = 838872527949266965
cargoVisitante = 838873046081208401
canalEntrada = 838864659057868832
canalSugestao = 838879668001439834

## MIDIAS

imagemEstatica = 'https://i.imgur.com/TmjYy6W.png'
tenisPNG = 'https://i.imgur.com/t36MDxj.png'
imagemGif = 'https://cdn.discordapp.com/attachments/766619794015256617/838903638968631316/gif_Prime.gif'




#Change status
async def Change_status():
    while True:
        await client.change_presence(activity=discord.Game(next(status)))
        await asyncio.sleep(5)
@client.command()
async def change_Status():
    client.loop.create_task(Change_status())


@client.event
async def on_ready():
    print('BOT ONLINE - Prime Monitoring')
    print(client.user.name)
    print(client.user.id)
    await change_Status()
    canalLog = client.get_channel(canalLogs)
    await canalLog.send('**Monitor Discord ON**')

@client.event
async def on_member_join(member):

    print(f'join {member.display_name}')
    user = member
    role = (discord.utils.get(user.guild.roles, id=cargoVisitante)) #carogoVisitante
    await member.add_roles(role)
    canalSend = client.get_channel(canalEntrada) ##canal entrada
    await canalSend.send(f'{member.mention}')

    embedBemVindo = discord.Embed(title=f'{member.display_name} | Bem Vindo!', description=f'Salve {member.mention}! Você acabou de chegar no 👻Prime Monitoring👻, aqui você estará informado em primeira mão sobre os próximos lançamentos e restoks!')
    embedBemVindo.add_field(name="📢 Fique atento!", value='Drops ou lançamentos serão anunciados em <#838857567806685255>!', inline=False)
    embedBemVindo.add_field(name="📌 Atenção!", value='Dê uma conferida no canal de <#838865016441667655> e <#838864125501112340> para ficar por dentro de tudo!', inline=False)
    embedBemVindo.add_field(name="🔧 Beta Teste!", value='Nosso sistema está na fase de testes, para participar do beta-test, envie `!tester` no canal <#838865256213118987>', inline=False)
    #embedBemVindo.add_field(name=f"{emojiInstagram} Siga no instagram!", value='[@Primemonitoring](https://www.instagram.com/Primemonitoring/)', inline=False)
    embedBemVindo.set_footer(text='Somos o melhor monitor do Brasil!', icon_url=tenisPNG)
    embedBemVindo.set_author(name="👻Prime Monitoring👻", url="https://discord.gg/pXfnkwBek4", icon_url=tenisPNG)
    embedBemVindo.set_thumbnail(url=imagemGif)
    await canalSend.send(embed=embedBemVindo)

    emoji = client.get_emoji(816469207180771349)
    emojiWelcome = client.get_emoji(816474493387407360)
    emojiAtenttion = client.get_emoji(816475090685394984)

    embedPV = discord.Embed(title='{} Bem vindo á nossa comunidade! {}'.format(emojiWelcome, emojiWelcome), color=discord.Color.purple())
    embedPV.add_field(name='{} Se tiver alguma dúvida, consulte alguem da nossa equipe!'.format(emoji), value='\u200b')
    embedPV.add_field(name="🔧 Beta Teste!", value='Nosso sistema está na fase de testes, para participar do beta-test, envie `!tester` no canal <#838865256213118987>', inline=False)
    embedPV.set_author(name="👻Prime Monitoring👻", url="https://discord.gg/pXfnkwBek4", icon_url=tenisPNG)  
    embedPV.set_thumbnail(url=imagemGif)
    await member.send(embed=embedPV)

    emojiAdc = client.get_emoji(817873086669127691)
    embedLogs = discord.Embed(title=f'{emojiAdc} LOG DE ENTRADA {emojiAdc}', color=discord.Color.blue())
    embedLogs.add_field(name='Novo membro no servidor:', value=f'{member.mention}')
    canalLog = client.get_channel(canalLogs)
    await canalLog.send(embed=embedLogs)

@client.event
async def on_member_remove(member):
    if member.guild.id == 838857567337316383:
        emojiDados = client.get_emoji(819283940665458699)
        embed = discord.Embed(title=f'{emojiDados} LOG de Saída {emojiDados}', color=discord.Color.blue())
        embed.add_field(name=f'{member.display_name} - saiu do servidor', value='\u200b')
        canalEnviarParadinha = client.get_channel(canalLogs)
        await canalEnviarParadinha.send(embed=embed)

@client.command(pass_context=True, aliases=['tester'])
async def betatesterJoin(ctx):
    embed=discord.Embed(title="Seja bem vindo !", description="Participando do programa de beta test, você recebe vantagens exclusivas", color=discord.Color.purple())
    embed.set_author(name="👻Prime Monitoring👻", url='https://discord.gg/pXfnkwBek4', icon_url=tenisPNG)
    embed.set_thumbnail(url=imagemGif)
    embed.add_field(name="Instruções", value="\u200b", inline=False)
    embed.add_field(name="📦┇monitor", value="Esse canal é onde você vai receber as notificações do monitor. Atualmente monitoramos mais de 600 modelos diferentes!", inline=False)
    embed.add_field(name="🔨┇atualizações", value="Aqui vão ser postadas todas as atualizações em nossa plataforma.", inline=False)
    embed.add_field(name="📢┇avisos", value="Todos os avisos sobre a nossa comunidade serão enviados nesse canal.", inline=False)
    embed.set_footer(text="Bot by @Primeze2#6809")
    await ctx.author.send(embed=embed)

    role = (discord.utils.get(ctx.author.guild.roles, id=cargoBetaTester))  
    await ctx.author.add_roles(role)   
    await ctx.message.delete()

@client.command(pass_context=True, aliases=['sugerir'])
async def sugestaoo(ctx, *, args):
    if ctx.channel.id == canalSugestao:
        await ctx.message.delete()
        embed = discord.Embed(title='📨 Nova sugestão! 📨', color=discord.Color.purple())
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.add_field(name='📝 Sugestão:', value=f'> {args}')
        embed.set_footer(text='👻 Prime Monitoring 👻')
        a = await ctx.channel.send(embed=embed)
        await a.add_reaction('👍')
        await a.add_reaction('👎')

client.run('ODM4ODY3MjM0NDAyODYxMDc2.YJBV_g.C5AknlEio3nRQKvjrCv_jyQNI9E')