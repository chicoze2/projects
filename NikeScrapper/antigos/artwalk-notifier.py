from os import terminal_size
import discord
import asyncio
from discord.ext import commands, tasks
from discord.utils import get
import json
from bs4 import BeautifulSoup
import requests
from discord.ext import tasks

bot_prefix = '!'
client = commands.Bot(command_prefix=bot_prefix)

async def logErro(erro):
    canalLogs = client.get_channel(820886241419198504)
    emojiDados = client.get_emoji(819283940665458699)
    emojiXis = client.get_emoji(816856671057608754) 
    await canalLogs.send(f'{emojiDados} **Crash detectado! `ERRO{erro}`** {emojiXis}')
    await canalLogs.send(canalLogs.guild.roles[0])
    await canalLogs.send('*O serviço provavelmente está online!*')

async def notificarTenis(urlTenis, nome, estado, imagemTenis, loja):
    if estado == 'disponivel':
        try:
            canalLogs = client.get_channel(820886241419198504)
            canalRestok = client.get_channel(829038305454063646)  ##canal original 
            #canalRestok = client.get_channel(826845407619448903) ## canal teste
            print('AAAAAAAAAAAAAAAAAAAAA NOTIFICANDO TENIS AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
            print(f'NOME {nome}, ESTATE {estado}, LOJA {loja}, LINK {urlTenis}, IMAGEM {imagemTenis}')

            if loja == 'artwalk':
                emojiArtwalk = client.get_emoji(824736057429590056)
                embed = discord.Embed(title=f'{nome}', color=discord.Color.purple(), url=urlTenis)
                embed.set_author(name='Boo Bot', icon_url='https://cdn.discordapp.com/attachments/820779763673202698/821193787467628564/logotipo-de-mascote-de-bazuca-fantasma_188898-6.jpeg')
                embed.set_image(url=imagemTenis)
                embed.set_thumbnail(url='https://cuponomia-a.akamaihd.net/img/stores/original/artwalk.png')
                embed.add_field(name=f'{emojiArtwalk} Tenis disponivel no site ArtWalk', value='Estoque detectado segundos atrás')
                embed.set_footer(text='Somos o melhor monitor do Brasil!', icon_url='https://cdn.discordapp.com/attachments/820779763673202698/821193787467628564/logotipo-de-mascote-de-bazuca-fantasma_188898-6.jpeg')
                await canalLogs.send(f'''tenis {nome} encontrado no estoque 
sob o estado de **{estado}** 
na loja **{loja}**  
com o link {urlTenis}
e imagem {imagemTenis}''')
                await canalRestok.send(embed=embed)
            
        except Exception as erro:
            await logErro(erro)


@tasks.loop(seconds=.1)
async def tenisArtwalk():
    
  
    try:
        urls = ['https://www.artwalk.com.br/buscapagina?fq=specificationFilter_16%3aT%C3%AAnis&fq=specificationFilter_15%3aJordan&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=2', 'https://www.artwalk.com.br/buscapagina?fq=specificationFilter_16%3aT%C3%AAnis&fq=specificationFilter_15%3aJordan&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=3', 'https://www.artwalk.com.br/buscapagina?fq=specificationFilter_16%3aT%C3%AAnis&fq=specificationFilter_15%3aJordan&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=4', 'https://www.artwalk.com.br/buscapagina?fq=specificationFilter_16%3aT%C3%AAnis&fq=specificationFilter_15%3aJordan&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=5', 'https://www.artwalk.com.br/buscapagina?fq=specificationFilter_16%3aT%C3%AAnis&fq=specificationFilter_15%3aJordan&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=6', 'https://www.artwalk.com.br/buscapagina?fq=specificationFilter_16%3aT%C3%AAnis&fq=specificationFilter_17%3aNMD&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=1','https://www.artwalk.com.br/buscapagina?fq=specificationFilter_16%3aT%C3%AAnis&fq=specificationFilter_17%3aNMD&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=2','https://www.artwalk.com.br/buscapagina?fq=specificationFilter_16%3aT%C3%AAnis&fq=specificationFilter_17%3aNMD&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=3','https://www.artwalk.com.br/buscapagina?fq=specificationFilter_16%3aT%C3%AAnis&fq=specificationFilter_17%3aNMD&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=4',
'https://www.artwalk.com.br/buscapagina?ft=air+force&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=2', 'https://www.artwalk.com.br/buscapagina?ft=air+force&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=3', 'https://www.artwalk.com.br/buscapagina?ft=air+force&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=4','https://www.artwalk.com.br/buscapagina?ft=air+force&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=5']
        for url in urls:
            print('ARTWALK')
            page = requests.get(url, timeout=(20, 27))
            soup = BeautifulSoup(page.content, 'html.parser')
            results = soup.find("div", class_='QD prateleira row qd-xs n1colunas')


            for produtos in results:

                ############################################
                ######## RECEBER INFO DE CADA TENIS ########    
                ############################################  

                #print('---------------------------')
                #print(produtos)
                divEspecifica = produtos.find('div', class_='col-xs-22 col-xs-offset-1')
                urlTenis = divEspecifica.find_all('a')[0]['href']
                nome = divEspecifica.find_all('a')[0].text
                string = str(produtos)


               ############################################
               ########### VERIFIC DISPONIBILIDADE ########    
               ############################################   

                if '<span class="best-price"' in string:
                    #print('Esse produto está disponivel')
                    estado = 'disponivel'

                elif '<span class="shelf-no-stock font-size-xs color-orange bold"><i class="fa fa-exclamation-triangle fa-6"></i>Avise-me Quando Chegar</span>' in string:
                    #print('Esse produto está esgotado')
                    #print(urlTenis)
                    estado = 'esgotado'

                else:
                    #print('Produto mal indentficado')
                    estado = 'nao identificado'

               ############################################
               ########### COMPARAR COM A DATABASE ########    
               ############################################  


                with open('links-artwalk.txt', 'r') as json_file:
                    data = json.load(json_file)
                verificador = nome in data
                if verificador == True:
                    estadoOld = data[nome][0]['estado']
                    if estadoOld == estado:
                        a = 1 + 1
                    else:

                        if estado == 'disponivel':
                            with open('links-artwalk.txt') as json_file:
                                json_decoded = json.load(json_file)

                            json_decoded[nome] = [{'url': urlTenis, 'estado': 'disponivel'}]

                            with open('links-artwalk.txt', 'w') as json_file:
                                json.dump(json_decoded, json_file)

                            ##montar notificação
                            divEspecificaIMG = produtos.find("div", class_='shelf-image')
                            imagemTenis = divEspecificaIMG.find_all('img')[0]['src']
                            loja = 'artwalk'
                        
                            await notificarTenis(urlTenis, nome, estado, imagemTenis, loja)
                            #await gravarValor(nome, urlTenis, estado)
                else:
                    with open('links-artwalk.txt') as json_file:
                        json_decoded = json.load(json_file)

                    json_decoded[nome] = [{'url': urlTenis, 'estado': estado}]

                    with open('links-artwalk.txt', 'w') as json_file:
                        json.dump(json_decoded, json_file)
                    urlTenis = urlTenis
                    imagemTenis = 'https://www.ciadosdescontos.com/static/2020/12/artwalk-250x250.png'
                    loja = 'artwalk'
                    await notificarTenis(imagemTenis, urlTenis, nome, estado, loja)

    except Exception as erro:
        #erro = 'função principal artwalk'
        await logErro(erro)

@client.event
async def on_ready():
    print('BOT ONLINE - Nike Notifier')
    print(client.user.name)  
    print(client.user.id)

    tenisArtwalk.start()

@client.event
async def on_message(message):
    if message.content.startswith('ligar nike'):
        if message.author.guild_permissions.administrator == True:
            await message.channel.send('Iniciando módulo artwalk')
            try:
                tenisArtwalk.start()
                await message.channel.send('Iniciado com sucesso!')
            except Exception as error:
                await message.channel.send(f'Um **erro inesperado** foi encontrado: `{error}`')    

client.run('ODIwODgyODUzMzU2MzcxOTg4.YE7ouw.3ukBewBHxWVig1Um2DFcRTLAxHA')

client.run('ODIwODgyODUzMzU2MzcxOTg4.YE7ouw.3ukBewBHxWVig1Um2DFcRTLAxHA')