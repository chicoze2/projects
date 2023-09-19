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

maxthreads = 65
sema = threading.Semaphore(value=maxthreads)
threads = list()


######################
ipDoBanco = ''
usuarioBanco = ''
senhaBanco = ''# parametros para a conexao 
database = ''   # com o banco de dados

connection = mysql.connector.connect(host=ipDoBanco,
                             user=usuarioBanco,
                             passwd=senhaBanco,
                             database=database)
###############################################

def logErro(erro):
    print(erro)

def fornecerUrlBancoArtwalk():
    try:
        urls = ['https://www.artwalk.com.br/buscapagina?fq=specificationFilter_16%3aT%C3%AAnis&fq=specificationFilter_15%3aJordan&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=2',
    'https://www.artwalk.com.br/buscapagina?fq=specificationFilter_16%3aT%C3%AAnis&fq=specificationFilter_15%3aJordan&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=3',
    'https://www.artwalk.com.br/buscapagina?fq=specificationFilter_16%3aT%C3%AAnis&fq=specificationFilter_15%3aJordan&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=4',
    'https://www.artwalk.com.br/buscapagina?fq=specificationFilter_16%3aT%C3%AAnis&fq=specificationFilter_15%3aJordan&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=5',
    'https://www.artwalk.com.br/buscapagina?fq=specificationFilter_16%3aT%C3%AAnis&fq=specificationFilter_15%3aJordan&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=6',
    'https://www.artwalk.com.br/buscapagina?fq=specificationFilter_16%3aT%C3%AAnis&fq=specificationFilter_17%3aNMD&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=1',
    'https://www.artwalk.com.br/buscapagina?fq=specificationFilter_16%3aT%C3%AAnis&fq=specificationFilter_17%3aNMD&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=2',
    'https://www.artwalk.com.br/buscapagina?fq=specificationFilter_16%3aT%C3%AAnis&fq=specificationFilter_17%3aNMD&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=3',
    'https://www.artwalk.com.br/buscapagina?fq=specificationFilter_16%3aT%C3%AAnis&fq=specificationFilter_17%3aNMD&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=4',
    'https://www.artwalk.com.br/buscapagina?ft=air+force&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=2', 
    'https://www.artwalk.com.br/buscapagina?ft=air+force&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=3', 
    'https://www.artwalk.com.br/buscapagina?ft=air+force&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=4',
    'https://www.artwalk.com.br/buscapagina?ft=air+force&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=5',
    'https://www.artwalk.com.br/buscapagina?fq=specificationFilter_16%3aT%c3%aanis&fq=specificationFilter_15%3aLebron+James&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=1',
    'https://www.artwalk.com.br/buscapagina?fq=specificationFilter_16%3aT%c3%aanis&fq=specificationFilter_15%3aLebron+James&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=2',
    'https://www.artwalk.com.br/buscapagina?fq=specificationFilter_16%3aT%c3%aanis&fq=specificationFilter_15%3aLebron+James&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=3',
    'https://www.artwalk.com.br/T%C3%AAnis/Kobe%20Bryant?PS=24&map=specificationFilter_16,specificationFilter_15&O=OrderByTopSaleDESC',
    'https://www.artwalk.com.br/buscapagina?fq=C%3a%2f1000022%2f&ft=Air+Max&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=2',
    'https://www.artwalk.com.br/buscapagina?fq=C%3a%2f1000022%2f&ft=Air+Max&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=3',
    'https://www.artwalk.com.br/buscapagina?fq=C%3a%2f1000022%2f&ft=Air+Max&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=4',
    'https://www.artwalk.com.br/buscapagina?fq=C%3a%2f1000022%2f&ft=Air+Max&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=5',
    'https://www.artwalk.com.br/buscapagina?fq=C%3a%2f1000022%2f&ft=Air+Max&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=6',
    'https://www.artwalk.com.br/buscapagina?fq=C%3a%2f1000022%2f&ft=Air+Max&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=7',
    'https://www.artwalk.com.br/buscapagina?fq=C%3a%2f1000022%2f&ft=Air+Max&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=8',
    'https://www.artwalk.com.br/buscapagina?fq=C%3a%2f1000022%2f&ft=Air+Max&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=9',
    'https://www.artwalk.com.br/buscapagina?fq=C%3a%2f1000022%2f&ft=Air+Max&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=10',
    'https://www.artwalk.com.br/buscapagina?fq=C%3a%2f1000022%2f&ft=Air+Max&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=11',
    'https://www.artwalk.com.br/buscapagina?fq=C%3a%2f1000022%2f&ft=Air+Max&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=12',
    'https://www.artwalk.com.br/buscapagina?fq=C%3a%2f1000022%2f&ft=Air+Max&O=OrderByReleaseDateDESC&PS=24&sl=19206a08-963f-4d97-b912-0523d722f9f5&cc=1&sm=0&PageNumber=13']
    except Exception as erro:
      logErro(erro)

    for url in urls:
        print('ARTWALK')
        page = requests.get(url, timeout=(20, 27))
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find("div", class_='QD prateleira row qd-xs n1colunas')
        for produtos in results:

            ############################################
            ######## RECEBER url  DE CADA TENIS ########    
            ############################################  

            #print('---------------------------')
            #print(produtos)
            divEspecifica = produtos.find('div', class_='col-xs-22 col-xs-offset-1')
            urlTenis = divEspecifica.find_all('a')[0]['href']
            querry_string = f"INSERT INTO produtos_artwalk (url_tenis) VALUES ('{urlTenis}');"
            try:
              cursor = connection.cursor()
              cursor.execute(querry_string)
            except Exception as erro:
              print(erro)
            connection.commit()


def receber_info_tenis_artwalk(urlTenis, verific):  ## essa função recebe como parametro o urlTenis e tem como obejtivo receber os parametros (preco, estado, nome)
  try:
    sema.acquire()
   # print("start %s" % (urlTenis,))

    a = str(urlTenis).replace("',)", "")
    urlTenis = (str(a).replace("('", ""))
    print("start %s" % (urlTenis,))
    connection = mysql.connector.connect(host=ipDoBanco,
                                 user=usuarioBanco,
                                 passwd=senhaBanco,
                                 database=database)
    page = requests.get(urlTenis) 
    file = BeautifulSoup(page.text, features="html.parser") 
    ######## RECEBER INFO DE CADA TENIS ########   
    #estado
    #nome
    #preco
    #imagem
    ##requerir estado antigo
    querry_string = f"SELECT estado FROM produtos_artwalk WHERE url_tenis = '{urlTenis}';" 
    cursor = connection.cursor()
    cursor.execute(querry_string)   
    data = cursor.fetchone()
    
    try:
      detalhes = file.find('p', class_='descricao-preco')
      preco2 = file.find('em', class_='valor-por price-best-price')
      preco = detalhes.find('strong', class_='skuPrice').text
      #preco = preco2.text
      #preco = detalhes.text

    except Exception as erro:                                        
      print(erro)         
      preco = 'nao sabe'                                             

    estadoOld = (str(data[0]))

    if detalhes:                                                        
      estado = 'disponivel'
    
    else:
      estado = 'esgotado'
    
    imagemTenis = file.find('img', class_='sku-rich-image-main')['src']
    nome = file.find('h1', class_='product-name').text
    print(f'Resumo do tenis; {nome}  --  {estado}  -- {urlTenis} -- {preco}')



    #fazer compração
    if estado == estadoOld:
        print('nao mudo')
        querry_string = f"UPDATE produtos_artwalk SET estado = '{estado}', preco = '{preco}', imagem_link = '{imagemTenis}', nome = '{nome}' WHERE url_tenis = '{urlTenis}'; "
        cursor = connection.cursor()
    else:
       
        if estado == 'disponivel':
            notificar = '1'
            querry_string = f"UPDATE produtos_artwalk SET estado = '{estado}', preco = '{preco}', notificar = '{notificar}', imagem_link = '{imagemTenis}', nome = '{nome}' WHERE url_tenis = '{urlTenis}'; "
            cursor = connection.cursor()
            try:
              cursor.execute(querry_string)
            except Exception as erro:
              print(erro)
            connection.commit()
        else:
            querry_string = f'UPDATE produtos_artwalk SET estado = "{estado}", preco = "{preco}", imagem_link = "{imagemTenis}", nome = "{nome}"  WHERE url_tenis = "{urlTenis}"; '
            cursor = connection.cursor()
            try:
              cursor.execute(querry_string)
            except Exception as erro:
              print(erro)
    connection.commit()          
    ##atualizar banco
  except Exception as erro:
    logErro(erro)
    #sys.exit()
  page = '.'
  file = '.'
  sema.release()


def iniciarThradingArtwalk():
    querry_string = 'SELECT url_tenis FROM `boo-monitor`.`produtos_artwalk` ORDER BY `estado` ASC, `notificar` ASC LIMIT 1000;' 
    cursor = connection.cursor()
    cursor.execute(querry_string)   
    data = cursor.fetchall()

    connectionA = mysql.connector.connect(host=ipDoBanco,
                                 user=usuarioBanco,
                                 passwd=senhaBanco,
                                 database=database)

    for urlTenis in data:
      a = str(urlTenis).replace("',)", "")
      urlTenis = (str(a).replace("('", ""))
      verific = 'sim'

      thread = threading.Thread(target=receber_info_tenis_artwalk, args=(urlTenis, verific))
      threads.append(thread)
      thread.start()


#receber_Info_tenis_artwalk('https://www.artwalk.com.br/tenis-sky-jordan-1-ps-infantil-bq719-7-101/p','sim', 'none')

#iniciarThradingArtwalk()

while True: 
    fornecerUrlBancoArtwalk()
    #time.sleep(10)
    iniciarThradingArtwalk()
    print(threading.active_count())
















