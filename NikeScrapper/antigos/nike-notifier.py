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

bot_prefix = '!'
client = commands.Bot(command_prefix=bot_prefix)
canalrestokID = 801239710725963806 ## original
#canalrestokID = 826845407619448903 ## teste


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
            canalRestok = client.get_channel(canalrestokID)
            print('-------------------------- NOTIFICANDO TENIS ----------------------------')
            print(f'NOME {nome}, ESTATE {estado}, LINK {urlTenis}, IMAGEM {imagemTenis}')


            ##procurar pares
            page = requests.get(urlTenis)
            soup = BeautifulSoup(page.content, 'html.parser')            
            divImagem = soup.find("a", class_="js-produto__foto")['href']
            #imagemTenis = f'https:{divImagem}'

            #embed decorator
            emojiNike = client.get_emoji(801502654513676298)
            canalLogs = client.get_channel(820886241419198504)

            #embed as self
            embed = discord.Embed(title=f'{nome}', color=discord.Color.purple(), url=urlTenis)
            embed.set_author(name='Boo Bot', icon_url='https://cdn.discordapp.com/attachments/820779763673202698/821193787467628564/logotipo-de-mascote-de-bazuca-fantasma_188898-6.jpeg')
            embed.set_image(url=imagemTenis)
            embed.set_thumbnail(url='https://w7.pngwing.com/pngs/654/821/png-transparent-swoosh-nike-just-do-it-logo-nike-angle-adidas-symbol.png')
            embed.add_field(name=f'{emojiNike} Tenis disponivel no site Nike SNKRS', value='Estoque detectado segundos atrás')
            embed.set_footer(text='Somos o melhor monitor do Brasil!', icon_url='https://cdn.discordapp.com/attachments/820779763673202698/821193787467628564/logotipo-de-mascote-de-bazuca-fantasma_188898-6.jpeg')
            await canalRestok.send(embed=embed)
            
            #logs de controle
            await canalLogs.send(f'''tenis {nome} encontrado no estoque 
sob o estado de **{estado}** 
na loja **{loja}**  
com o link {urlTenis}
e imagem {imagemTenis}''')       

        except Exception as erro:
            print('erro na notificatio')
            
            await logErro(erro)



@tasks.loop(seconds=.2)
async def tenisNike():
    while True:
        try:
            urls = ['https://www.nike.com.br/Snkrs/Feed?p=1&demanda=true', 'https://www.nike.com.br/Snkrs/Feed?p=2&demanda=true', 'https://www.nike.com.br/Snkrs/Feed?p=3&demanda=true', 'https://www.nike.com.br/Snkrs/Feed?p=1&demanda=true', 'https://www.nike.com.br/Snkrs/Feed?p=5&demanda=true', 'https://www.nike.com.br/Snkrs/Feed?p=6&demanda=true', 'https://www.nike.com.br/Snkrs/Feed?p=7&demanda=true']
            for url in urls:
                

                page = requests.get(url)
                soup = BeautifulSoup(page.content, 'html.parser')
                results = soup.find("div", class_='box-resultados box-paginacao vitrine-content--feed grid-produtos grid-produtos--3-col')

                print('NAIKE')
                for produtos in results:

                    ############################################
                    ######## RECEBER INFO DE CADA TENIS ########    
                    ############################################  

                    #print('---------------------------')
                    string = str(produtos)
                    tagA = produtos.find('div', {'class': 'produto__imagem'})
                    urlTenis = tagA.find_all('a')[0]['href']
                    try:
                        imagemTenis = tagA.find_all('img')[0]['data-src']
                    except Exception as erro:
                        await logErro(erro)     
                        imagemTenis = 'https://cdn.discordapp.com/attachments/820779763673202698/821193787467628564/logotipo-de-mascote-de-bazuca-fantasma_188898-6.jpeg'

                    produtoDetalhe = produtos.find('h2', {'class': 'produto__detalhe-titulo'})
                    nome = produtoDetalhe.text

                    #print(f'NOME: {nome}')
                    #print(f'{urlTenis}   {imagemTenis}  ')


                    ############################################
                    ########### VERIFIC DISPONIBILIDADE ########    
                    ############################################   
                    try:
                        if '<div class="produto produto--comprar">' in string:
                            #print('Esse produto está disponivel')
                            estado = 'disponivel'

                        elif '<div class="produto produto--esgotado">' in string:
                            #print('Esse produto está esgotado')
                            estado = 'esgotado'
                        elif '<div class="produto produto--aviseme">' in string:
                            #print('Esse produto ainda não foi lançado')
                            estado = 'lancar'
                        else:
                            #print('Produto mal indentficado')
                            estado = 'nao identificado'
                    except Exception as erro:
                        #erro = '04'
                        await logErro(erro)
                    ############################################
                    ########### COMPARAR COM A DATABASE ########    
                    ############################################  

                    try:
                        with open('links-nike.txt', 'r') as json_file:
                            data = json.load(json_file)
                        verificador = urlTenis in data
                        if verificador == True:
                            #print('tenis ja conhecido dos mlk')
                            estadoOld = data[urlTenis][0]['estado']
                            if estadoOld == estado:
                                a = 1 + 1
                                #print('nada mudou')
                            else:
                                loja = 'nike'
                                with open('links-nike.txt') as json_file:
                                    json_decoded = json.load(json_file)

                                json_decoded[urlTenis] = [{'nome': nome, 'estado': estado}]

                                with open('links-nike.txt', 'w') as json_file:
                                    json.dump(json_decoded, json_file)

                                #print(f'Tenis {nome} mudou para o estado {estado}')

                                await notificarTenis(urlTenis, nome, estado, imagemTenis, loja)
                        else:
                            loja = 'nike'
                            #print(f'Tenis {nome} mudou para o estado {estado}')
                            if estado == 'disponivel':
                                await notificarTenis(urlTenis, nome, estado, imagemTenis, loja)

                            with open('links-nike.txt') as json_file:
                                json_decoded = json.load(json_file)

                            json_decoded[urlTenis] = [{'nome': nome, 'estado': estado}]

                            with open('links-nike.txt', 'w') as json_file:
                                json.dump(json_decoded, json_file)
                    except Exception as erro:
                        #erro = '03'
                        await logErro(erro)

                ############################################
                ############ GRAVAR VALOR ##################    
                ############################################       

                    try:
                        with open('links-nike.txt') as json_file:
                            json_decoded = json.load(json_file)

                        json_decoded[urlTenis] = [{'nome': nome, 'estado': estado}]

                        with open('links-nike.txt', 'w') as json_file:
                            json.dump(json_decoded, json_file)
                    except Exception as erro:
                        #erro = '02'
                        await logErro(erro)

        except Exception as erro:
            await logErro(erro)

@client.event
async def on_ready():
    print('BOT ONLINE - Nike Notifier')
    print(client.user.name)  
    print(client.user.id)
    canalLogs = client.get_channel(820886241419198504)
    await canalLogs.send('**nike online**')
    await tenisNike()
    #tenisNike.start()

@client.event
async def on_message(message):
    if message.content.startswith('ligar nike'):
        if message.author.guild_permissions.administrator == True:
            await message.channel.send('Iniciando módulo nike')
            try:
                tenisNike.start()
                await message.channel.send('Iniciado com sucesso!')
            except Exception as error:
                await message.channel.send(f'Um **erro inesperado** foi encontrado: `{error}`')    

client.run('ODIwODgyODUzMzU2MzcxOTg4.YE7ouw.3ukBewBHxWVig1Um2DFcRTLAxHA')