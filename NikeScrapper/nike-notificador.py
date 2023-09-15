from os import name
import discord
import asyncio
from discord import message
from discord.ext import commands, tasks
from discord.utils import escape_markdown, get
import json
from bs4 import BeautifulSoup
import requests
from discord.ext import tasks
import mysql.connector


bot_prefix = '!'
client = commands.Bot(command_prefix=bot_prefix)
canalrestokID = 801239710725963806 ## original
#canalrestokID = 826845407619448903 ## teste


######################
# ipDoBanco = '5.183.8.41'
# usuarioBanco = 'chico'
# senhaBanco = '@Chicoze2603'# parametros para a conexao 
# database = 'boo-monitor'   # com o banco de dados

# connection = mysql.connector.connect(host=ipDoBanco,
#                              user=usuarioBanco,
#                              passwd=senhaBanco,
#                              database=database)
###############################################


async def logErro(erro):
    canalLogs = client.get_channel(820886241419198504)
    emojiDados = client.get_emoji(819283940665458699)
    emojiXis = client.get_emoji(816856671057608754) 
    await canalLogs.send(f'{emojiDados} **Crash detectado! `ERRO{erro}`** {emojiXis}')
    await canalLogs.send(canalLogs.guild.roles[0])
    await canalLogs.send('*O serviço provavelmente está online!*')



@tasks.loop(seconds = 5)
async def notificarTenis():
######################
    ipDoBanco = '5.183.8.41'
    usuarioBanco = 'chico'
    senhaBanco = '@Chicoze2603'# parametros para a conexao 
    database = 'boo-monitor'   # com o banco de dados
    
    connection = mysql.connector.connect(host=ipDoBanco,
                                 user=usuarioBanco,
                                 passwd=senhaBanco,
                                 database=database)
###############################################
    print('pai ta rodando')
    ##requerir estado antigo
    querry_string = f"SELECT url_tenis, preco, estado, nome, imagem_link FROM produtos_nike WHERE notificar = '1';"
    cursor = connection.cursor()
    cursor.execute(querry_string)   
    data = cursor.fetchall()
    
    for registro_tenis in data: ##para cada tenis registrado que cumpre o SELECT acima
        print(registro_tenis)

        urlTenis = registro_tenis[0]
        preco = registro_tenis[1]
        estado = registro_tenis[2]
        nome = registro_tenis[3]
        imagemTenis = registro_tenis[4]

        print(f'INFORMAÇÕES DO TENIS NOME:{nome}  PRECO:{preco} ESTADO:{estado}  IMAGEM:{imagemTenis}')

        if estado == 'disponivel':

           try:
               canalRestok = client.get_channel(canalrestokID)
               print('-------------------------- NOTIFICANDO TENIS ----------------------------')
               print(f'NOME {nome}, ESTATE {estado}, LINK {urlTenis}, IMAGEM {imagemTenis}')
   
   
               ##procurar preco
               page = requests.get(urlTenis)
               soup = BeautifulSoup(page.content, 'html.parser')                    
               preco = soup.find("span", class_="js-valor-por").text
   
   
               #embed decorator
               emojiNike = client.get_emoji(801502654513676298)
               canalLogs = client.get_channel(820886241419198504)
               emojiMoney = client.get_emoji(818633385635217458)
   
               #embed as self
               embed = discord.Embed(title=f'{nome}', color=discord.Color.purple(), url=urlTenis)
               embed.set_author(name='Boo Bot', icon_url='https://cdn.discordapp.com/attachments/820779763673202698/821193787467628564/logotipo-de-mascote-de-bazuca-fantasma_188898-6.jpeg')
               embed.set_image(url=imagemTenis)
               embed.set_thumbnail(url='https://w7.pngwing.com/pngs/654/821/png-transparent-swoosh-nike-just-do-it-logo-nike-angle-adidas-symbol.png')
               embed.add_field(name=f'{emojiMoney} Valor registrado:', value=f'{preco}', inline=False)
               embed.add_field(name=f'{emojiNike} Tenis disponivel no site Nike SNKRS', value='Estoque detectado segundos atrás')
               embed.set_footer(text='Somos o melhor monitor do Brasil!', icon_url='https://cdn.discordapp.com/attachments/820779763673202698/821193787467628564/logotipo-de-mascote-de-bazuca-fantasma_188898-6.jpeg')
               await canalRestok.send(embed=embed)
               
               #logs de controle
               await canalLogs.send(f'''tenis {nome} encontrado no estoque 
sob o estado de **{estado}** 
na loja **nike**  
com o link {urlTenis}
e imagem {imagemTenis}''')       

                #### fazer o update do status notificar
               querry_string = f"UPDATE produtos_nike SET estado = '{estado}', notificar = '0' WHERE url_tenis = '{urlTenis}';"
               cursor = connection.cursor()
               cursor.execute(querry_string)
               connection.commit()



           except Exception as erro:
               print('erro na notificatio')
               
               await logErro(erro)
        else:
            emojiDados = client.get_emoji(819283940665458699)
            canalLogs = client.get_channel(820886241419198504)
            emojiErro = client.get_emoji(826185098763829328)
            embed = discord.Embed(title=f'{emojiDados} Log de erro {emojiErro}')
            embed.add_field(name='Tenis com falso positivo entre o banco de dados e a página do produto', value='\u200b', inline=False)
            embed.add_field(name='NOME', value=f'{nome}')
            embed.add_field(name='LINK', value=f'{urlTenis}')
            embed.add_field(name='ESTADO ATUAL DO PRODUTO', value=f'{estado}')

            await canalLogs.send(embed=embed)
            querry_string = f"UPDATE produtos_nike SET estado = '{estado}', notificar = '0' WHERE url_tenis = '{urlTenis}';"
            cursor = connection.cursor()
            cursor.execute(querry_string)
            connection.commit()


    ##detect variação de preço 
    querry_string = f"SELECT url_tenis, preco, estado, nome, imagem_link, variacao_preco FROM produtos_nike WHERE notificar_preco = '1';"
    cursor = connection.cursor()
    cursor.execute(querry_string)   
    data = cursor.fetchall()

    for registro_tenis in data:
    
        urlTenis = registro_tenis[0]
        preco = registro_tenis[1]
        estado = registro_tenis[2]
        nome = registro_tenis[3]
        imagemTenis = registro_tenis[4]
        precoOld = registro_tenis[5]

        #embed decorator
        emojiNike = client.get_emoji(801502654513676298)
        canalLogs = client.get_channel(820886241419198504)
        emojiMoney = client.get_emoji(818633385635217458)
        #embed as self
        embed = discord.Embed(title=f'{nome}', color=discord.Color.purple(), url=urlTenis)
        embed.set_author(name='Boo Bot', icon_url='https://cdn.discordapp.com/attachments/820779763673202698/821193787467628564/logotipo-de-mascote-de-bazuca-fantasma_188898-6.jpeg')
        embed.set_image(url=imagemTenis)
        embed.set_thumbnail(url='https://w7.pngwing.com/pngs/654/821/png-transparent-swoosh-nike-just-do-it-logo-nike-angle-adidas-symbol.png')
        embed.add_field(name=f'{emojiMoney} Variação de preço detectada:', value=f'\u200b', inline=False)
        embed.add_field(name=f'{emojiNike} Preço antigo:', value=f'{precoOld}')
        embed.add_field(name=f'{emojiNike} Preço novo:', value=f'{preco}')
        embed.set_footer(text='Somos o melhor monitor do Brasil!', icon_url='https://cdn.discordapp.com/attachments/820779763673202698/821193787467628564/logotipo-de-mascote-de-bazuca-fantasma_188898-6.jpeg')
        canalRestok = client.get_channel(canalrestokID)
        await canalRestok.send(embed=embed)       

        querry_string = f"UPDATE produtos_nike SET notificar_preco = '0', variacao_preco = '0' WHERE url_tenis = '{urlTenis}';"
        cursor = connection.cursor()
        cursor.execute(querry_string)
        connection.commit()        

@client.event
async def on_ready():
    print('BOT ONLINE - Nike Notifier')
    print(client.user.name)  
    print(client.user.id)
    canalLogs = client.get_channel(820886241419198504)
    await canalLogs.send('**nike online**')
    notificarTenis.start()

@client.event
async def on_message(message):
    if message.content.startswith('ligar nike'):
        if message.author.guild_permissions.administrator == True:
            await message.channel.send('Iniciando módulo nike')
            try:
                notificarTenis.start()
                await message.channel.send('Iniciado com sucesso!')
            except Exception as error:
                await message.channel.send(f'Um **erro inesperado** foi encontrado: `{error}`')    

client.run('ODIwODgyODUzMzU2MzcxOTg4.YE7ouw.3ukBewBHxWVig1Um2DFcRTLAxHA')