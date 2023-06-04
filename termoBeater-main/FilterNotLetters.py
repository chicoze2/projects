def filterNotLetters(wordList, notLetters):
  notWords = []

  for word in wordList: 
    for letter in notLetters:
      if letter in word:
        if not word in notWords:
          notWords.append(word)


  for nWord in notWords:
    if nWord in wordList:
      wordList.remove(nWord)

  return wordList

# print(filterNotLetters(wordList, notLetters)) debug function