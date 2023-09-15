import requests
import os
from bs4 import BeautifulSoup
import json
import time
import threading
import asyncio
import discord
import random
from discord.ext import commands, tasks
from discord.utils import get
import mysql.connector
import sys


bot_prefix = '!'
client = commands.Bot(command_prefix=bot_prefix)
canalrestokID = 826845407619448903 ## teste

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

def logErro(erro):
    print(erro)

def fornecerInfoBanco():  ### essa função pesquisa todos os tenis no feed da nike snkrs e salva as url no banco de dados
  try:
      cursor = connection.cursor()
      urls = ['https://www.nike.com.br/Snkrs/Feed?p=1&demanda=true', 'https://www.nike.com.br/Snkrs/Feed?p=2&demanda=true', 'https://www.nike.com.br/Snkrs/Feed?p=3&demanda=true', 'https://www.nike.com.br/Snkrs/Feed?p=1&demanda=true', 'https://www.nike.com.br/Snkrs/Feed?p=5&demanda=true', 'https://www.nike.com.br/Snkrs/Feed?p=6&demanda=true', 'https://www.nike.com.br/Snkrs/Feed?p=7&demanda=true']
      for url in urls:
          
          print(f'Lendo página {url}')
          page = requests.get(url)
          soup = BeautifulSoup(page.content, 'html.parser')
          results = soup.find("div", class_='box-resultados box-paginacao vitrine-content--feed grid-produtos grid-produtos--3-col')

          for produtos in results:
              tagA = produtos.find('div', {'class': 'produto__imagem'})
              urlTenis = tagA.find_all('a')[0]['href']

              querry_string = f"INSERT INTO produtos_nike (url_tenis) VALUES ('{urlTenis}');"
              try:
                cursor.execute(querry_string)
              except Exception as erro:
                print(erro)
              connection.commit()

  except Exception as erro:
    print(erro)                  


def receber_info_tenis(urlTenis, verific):  ## essa função recebe como parametro o urlTenis e tem como obejtivo receber os parametros (preco, estado, nome)
  connection = mysql.connector.connect(host=ipDoBanco,
                               user=usuarioBanco,
                               passwd=senhaBanco,
                               database=database)
  download = []
  print(f'url tenis recebido: {urlTenis}')
  page = requests.get(urlTenis).text 
  soup = BeautifulSoup(page, features="html.parser") 
  download.append(soup) 

  for file in download: # file é o HTML de uma página urlTenis

    ##procurar preco                    
    preco = file.find("span", class_="js-valor-por").text

    ##procurar estado
    if file.find('p', class_='mb-0 mt-5 esgotado'):
        estado = 'esgotado'
    elif file.find('button', class_='btn btn-black btn-avisar'):
        estado = 'lancar'
    elif file.find('p', class_='mb-0 mt-5 esgotado hidden'):
        estado = 'disponivel'

    ##procurar imagem
    
    try:
        tagA = file.find('a', {'class': 'js-produto__foto'})
        imagemTenis = tagA['href']
    except Exception as erro:
        logErro(erro)     
        imagemTenis = 'https://cdn.discordapp.com/attachments/820779763673202698/821193787467628564/logotipo-de-mascote-de-bazuca-fantasma_188898-6.jpeg'

    #procurar nome
    produtoDetalhe = file.find('div', {'class': 'nome-preco-produto'})
    nome = produtoDetalhe.text

    ##requerir estado antigo
    querry_string = f"SELECT estado, preco FROM produtos_nike WHERE url_tenis = '{urlTenis}';" 
    cursor = connection.cursor()
    cursor.execute(querry_string)   
    data = cursor.fetchone()
    estadoOld = (str(data[0]))
    precoOld = (str(data[1]))
  
    def compararPreco(preco, precoOld):
      #print('entrei na função')
      if precoOld != preco:
        print('diferença detect')
        querry_string = f"UPDATE produtos_nike SET preco = '{preco}', variacao_preco = '{precoOld}', notificar_preco = '1' WHERE url_tenis = '{urlTenis}'; "
        cursor = connection.cursor()
        cursor.execute(querry_string)
        connection.commit()
        print(f'preco atual {preco}, precoOld = {precoOld}, url_tenis = {urlTenis}')


    #fazer compração
    if estado == estadoOld:
        print('nao mudo')
      

    else:
        print(f'mudou de {estadoOld} para {estado}')
        if estado == 'disponivel':
            notificar = '1'
            querry_string = f"UPDATE produtos_nike SET estado = '{estado}', preco = '{preco}', notificar = '{notificar}', imagem_link = '{imagemTenis}', nome = '{nome}' WHERE url_tenis = '{urlTenis}'; "
            cursor = connection.cursor()
            try:
              cursor.execute(querry_string)
            except Exception as erro:
              print(erro)
            connection.commit()
            
        else:
            querry_string = f"UPDATE produtos_nike SET estado = '{estado}', preco = '{preco}', imagem_link = '{imagemTenis}', nome = '{nome}'  WHERE url_tenis = '{urlTenis}'; "
            cursor = connection.cursor()
            try:
              cursor.execute(querry_string)
            except Exception as erro:
              print(erro)
            connection.commit()     
                 
    ##fazer o track do preco
    compararPreco(preco, precoOld)

    ##encerrar thread
    sys.exit()

def iniciarThreding():     #### essa função recebe todos os url_tenis no array data
    querry_string = 'SELECT url_tenis FROM produtos_nike;' 
    cursor = connection.cursor()
    cursor.execute(querry_string)   
    data = cursor.fetchall()

    #data = ['https://www.nike.com.br/nike-x-stussy-1-16-210-283919']

    for urlTenis in data:
      a = str(urlTenis).replace("',)", "")
      urlTenis = (str(a).replace("('", ""))
      verific = 'sim'
      processThread = threading.Thread(target=receber_info_tenis, args=(urlTenis, verific)) # parameters and functions have to be passed separately
      processThread.start() # start the thread




while True: 
    fornecerInfoBanco()
    time.sleep(10)
    iniciarThreding()