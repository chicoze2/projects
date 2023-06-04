import os
from FilterNotLetters import *
from FilterHasLetters import *
from FilterPosition import *

hasLetters = []
notLetters = []

wordList = open("database/fiveLettersOnly.txt", "r", encoding="utf-8").readlines()

while True:
  os.system('cls')
  options = input("""Digite a operação desejada:
1 - Letra que CONTÉM na palavra
2 - Letra que NÃO CONTÉM na palavra
3 - Filtrar letra por POSIÇÃO
4 - Filtrar letra por NEGATIVA de posição
5 - Mostrar possibilidades
9 - Reiniciar
0 - Sair
---> """)


  match int(options):
    case 1: #letra que CONTÉM
      os.system('cls')
      inputLetra = input("Digite a letra: ")
      hasLetters.append(inputLetra)

    case 2: #letra que nao contem
      os.system('cls')
      inputLetra = input("Digite a letra: ")
      notLetters.append(inputLetra)


    case 3: # filtrar por posição 
      os.system('cls')
      
      
      letter = input("Digite a letra: ")
      position = int(input("Digite a posição em que ela aparece: "))

      wordList = filterPosition(wordList,letter, position)

    case 4: ## negativa de posição
      os.system('cls')

      letter = input("Digite a letra: ")
      position = int(input("Digite a posição em que ela NÃO aparece: "))

      wordList = filterNotInPosition(wordList,letter, position)
      hasLetters.append(letter)
      wordList = filterHasLetters(wordList, hasLetters)

    case 5: # mostrar possibilidades
      os.system('cls')
      if notLetters != []:
        wordList = filterNotLetters(wordList, notLetters)
        notLetters == []

      if hasLetters != []:
        wordList = filterHasLetters(wordList, hasLetters)
        hasLetters = []
      

      count = 0
      for word in wordList:
        count += 1

      opt = input(f"Você deseja ver as {count} opções? (s/n) ")
      if opt == "s":
        print(*wordList, sep = '-> ')
        input("Pressione qualquer tecla para retornar")


    case 9:
      os.system('cls')
      hasLetters = []
      notLetters = []
      wordList = open("database/fiveLettersOnly.txt", "r", encoding="utf-8").readlines()

    case other:
      break
      
  

  