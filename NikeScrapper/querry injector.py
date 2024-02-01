import mysql.connector
import json

ipDoBanco = 
usuarioBanco = ''
senhaBanco = 
database = ''

def conectarBanco(querry_string):
    connection = mysql.connector.connect(host=ipDoBanco,
                                         user=usuarioBanco,
                                         passwd=senhaBanco,
                                         database=database)
    cursor = connection.cursor()
    cursor.execute(querry_string)
    connection.commit()

def conectarBancoSelect(querry_string):
    connection = mysql.connector.connect(host=ipDoBanco,
                                         user=usuarioBanco,
                                         passwd=senhaBanco,
                                         database=database)
    cursor = connection.cursor()
    cursor.execute(querry_string)   
    a = cursor.fetchone()

    print(a[0])


operacao = input('''Qual operação você quer realizar?
1 - Atualizar registro (UPDATE ou INSERT)
2 - Ler registro (SELECT)''')



if operacao == '1':
    querry_string = input('envie aqui a querry string: ')
    conectarBanco(querry_string)
    
elif operacao == '2':
    querry_string = input('envie aqui a querry string')
    result = conectarBancoSelect(querry_string)



#### dicionario
                                                #colunas                                                                    #valor pra cada coluna
#INSERT INTO clientes_info (id, server_url, ativação_plano, valor_plano, coluna_teste) VALUES ('457346989353336833', 'google.com', '2021-03-26', '{"ativacao":"25"}', 'testado amem');