import os
import threading

dict = open("database/palavras.txt", "r", encoding="utf-8")
fiveLettersOnly = open("database/fiveLettersOnly.txt", "w", encoding="utf-8")
count = 0

for i in dict.readlines():
  if len(i) == 6:
    if(not "-" in i):
      if(not "." in i):
        # if(not "'"):
        count+=1
        fiveLettersOnly.write(i.lower())
      
print(f"Foram gravadas {str(count)} palavras")