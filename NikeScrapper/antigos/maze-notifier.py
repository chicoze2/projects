import discord
import asyncio
from discord import message
from discord.ext import commands, tasks
from discord.utils import get
import json
from bs4 import BeautifulSoup
import requests
from discord.ext import tasks

bot_prefix = '!'
client = commands.Bot(command_prefix=bot_prefix)
#canalrestokID = 801239710725963806 ## original
canalrestokID = 826845407619448903 ## teste


async def logErro(erro):
    canalLogs = client.get_channel(820886241419198504)
    emojiDados = client.get_emoji(819283940665458699)
    emojiXis = client.get_emoji(816856671057608754) 
    await canalLogs.send(f'{emojiDados} **Crash detectado! `ERRO{erro}`** {emojiXis}')
    await canalLogs.send(canalLogs.guild.roles[0])
    await canalLogs.send('*O serviço provavelmente está online!*')



async def notificarMaze(urlTenis, nome, estado, preco):
    if estado == 'disponivel':
        try:
            canalLogs = client.get_channel(820886241419198504)

            page = requests.get(urlTenis)
            soup = BeautifulSoup(page.content, 'html.parser')            
            divImagem = soup.find("img", class_="ui image small centered")['src']
            imagemTenis = f'https:{divImagem}'

            print('-------------------------- NOTIFICANDO TENIS ----------------------------')
            print(f'NOME {nome}, ESTATE {estado}, LINK {urlTenis}, IMAGEM {imagemTenis}')

            emojiMoney = client.get_emoji(818633385635217458)
            canalRestok = client.get_channel(canalrestokID)
            embed = discord.Embed(title=f'{nome}', color=discord.Color.purple(), url=urlTenis)
            embed.set_author(name='Boo Bot', icon_url='https://cdn.discordapp.com/attachments/820779763673202698/821193787467628564/logotipo-de-mascote-de-bazuca-fantasma_188898-6.jpeg')
            embed.set_image(url=imagemTenis)
            embed.set_thumbnail(url='https://www.maze.com.br/assets/image/logo/logo.png')
            embed.add_field(name=f'Tenis disponivel no site Maze', value='Estoque detectado segundos atrás')
            embed.add_field(name=f'{emojiMoney} Valor registrado:', value=f'{preco}', inline=False)
            embed.set_footer(text='Somos o melhor monitor do Brasil!', icon_url='https://cdn.discordapp.com/attachments/820779763673202698/821193787467628564/logotipo-de-mascote-de-bazuca-fantasma_188898-6.jpeg')
            await canalRestok.send(embed=embed)
            await canalLogs.send(f'''tenis {nome} encontrado no estoque 
sob o estado de **{estado}**  
com o link {urlTenis}
e imagem ''')       


        except Exception as erro:
            await logErro(erro)

async def tenisMaze():
    while True:
        try:
            urls = ['https://www.maze.com.br/product/getproductscategory/?path=%2Fcategoria%2Fnike%2Fdunk&viewList=g&pageNumber=1&pageSize=12&order=&brand=&category=127152&group=&keyWord=&initialPrice=&finalPrice=&variations=&idAttribute=&idEventList=&idCategories=&idGroupingType=',
'https://www.maze.com.br/product/getproductscategory/?path=%2Fcategoria%2Fnike%2Fdunk&viewList=g&pageNumber=2&pageSize=12&order=&brand=&category=127152&group=&keyWord=&initialPrice=&finalPrice=&variations=&idAttribute=&idEventList=&idCategories=&idGroupingType=',
'https://www.maze.com.br/product/getproductscategory/?path=%2Fcategoria%2Fnike%2Fjordan&viewList=g&pageNumber=1&pageSize=12&order=&brand=&category=124814&group=&keyWord=&initialPrice=&finalPrice=&variations=&idAttribute=&idEventList=&idCategories=&idGroupingType=',
'https://www.maze.com.br/product/getproductscategory/?path=%2Fcategoria%2Fnike%2Fjordan&viewList=g&pageNumber=2&pageSize=12&order=&brand=&category=124814&group=&keyWord=&initialPrice=&finalPrice=&variations=&idAttribute=&idEventList=&idCategories=&idGroupingType=',
'https://www.maze.com.br/product/getproductscategory/?path=%2Fcategoria%2Fnike%2Fjordan&viewList=g&pageNumber=3&pageSize=12&order=&brand=&category=124814&group=&keyWord=&initialPrice=&finalPrice=&variations=&idAttribute=&idEventList=&idCategories=&idGroupingType=',
'https://www.maze.com.br/product/getproductscategory/?path=%2Fcategoria%2Fnike%2Fair-force&viewList=g&pageNumber=3&pageSize=12&order=&brand=&category=124804&group=&keyWord=&initialPrice=&finalPrice=&variations=&idAttribute=&idEventList=&idCategories=&idGroupingType=',
'https://www.maze.com.br/product/getproductscategory/?path=%2Fcategoria%2Fnike%2Fair-force&viewList=g&pageNumber=2&pageSize=12&order=&brand=&category=124804&group=&keyWord=&initialPrice=&finalPrice=&variations=&idAttribute=&idEventList=&idCategories=&idGroupingType=',
'https://www.maze.com.br/product/getproductscategory/?path=%2Fcategoria%2Fnike%2Fair-force&viewList=g&pageNumber=1&pageSize=12&order=&brand=&category=124804&group=&keyWord=&initialPrice=&finalPrice=&variations=&idAttribute=&idEventList=&idCategories=&idGroupingType=',
'https://www.maze.com.br/categoria/adidas/yeezy']
            for url in urls:
                print('maze')
                user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'
                headers = {'User-Agent': user_agent}
                page = requests.get(url, headers=headers)
                soup = BeautifulSoup(page.content, 'html.parser')
                results = soup.find_all("div", {"class": "ui card produto product-in-card"})
                for item in results:
                    divEspecifica = item.find('div', class_='dados')

                    ############################################
                    ######## RECEBER INFO DE CADA TENIS ########    
                    ############################################ 

                    urlTenis1 = divEspecifica.find_all('a')[0]['href']
                    urlTenis = f'https://www.maze.com.br/{urlTenis1}'

                    nome1 = divEspecifica.find_all('span')[0].text.replace('  ', '')        
                    nome = nome1.replace('\n', '')

                    preco1 = divEspecifica.find('span', class_="preco").text.replace('  ', '')    
                    preco = preco1.replace('\n', '')

                    #divContent = item.find('div', class_='content')
                    #imagem = divContent.find_all('img')[0]['src']
#
                    #print(imagem)
#
                   #print('---------------------------')
                   #print(f'{nome}')
                   #print(f'{preco}')
                   #print(f'LINKE DO BAOT: {urlTenis}')
                    #await asyncio.sleep(10)
                   ############################################
                   ########### VERIFIC DISPONIBILIDADE ########    
                   ############################################   

                    div_botoes_centered = item.find('div', class_='botoes centered')
                    spanCompreAgora = div_botoes_centered.find('a', title='Comprar')

                    if spanCompreAgora:
                        estado = 'disponivel'
                    else:
                        estado = 'esgotado'

                ############################################
                ########### COMPARAR COM A DATABASE ########    
                ############################################

                    with open('links-maze.txt', 'r') as json_file:
                        data = json.load(json_file)
                    verificador = urlTenis in data
                    if verificador == True:
                        #print('tenis ja conhecido dos mlk')
                        estadoOld = data[urlTenis][0]['estado']
                        if estadoOld == estado:
                            a = 1 + 1
                            #print('nada mudou')
                        else:
                            loja = 'maze'
                            with open('links-maze.txt') as json_file:
                                json_decoded = json.load(json_file)

                            json_decoded[urlTenis] = [{'nome': nome, 'estado': estado}]

                            with open('links-maze.txt', 'w') as json_file:
                                json.dump(json_decoded, json_file)

                            #print(f'Tenis {nome} mudou para o estado {estado}')

                            await notificarMaze(urlTenis, nome, estado, preco)
                    else:
                        loja = 'maze'
                        #print(f'Tenis {nome} mudou para o estado {estado}')
                        if estado == 'disponivel':
                            await notificarMaze(urlTenis, nome, estado, preco)

                        with open('links-maze.txt') as json_file:
                            json_decoded = json.load(json_file)

                        json_decoded[urlTenis] = [{'nome': nome, 'estado': estado}]

                        with open('links-maze.txt', 'w') as json_file:
                                json.dump(json_decoded, json_file)                   
            #await tenisNike()
        except Exception as erro:
            print(erro)


@client.event
async def on_ready():
    print('BOT ONLINE - Nike Notifier')
    print(client.user.name)  
    print(client.user.id)
    canalLogs = client.get_channel(820886241419198504)
    await canalLogs.send('**maze online**')
    await tenisMaze()

    #tenisNike.start()


client.run('ODIwODgyODUzMzU2MzcxOTg4.YE7ouw.3ukBewBHxWVig1Um2DFcRTLAxHA')