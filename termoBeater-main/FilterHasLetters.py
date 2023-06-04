def filterHasLetters(wordList, hasLetters):
  hasWords = []

  for word in wordList: 
    for letter in hasLetters:
      if letter in word:
        if not word in hasWords:
          hasWords.append(word)

  return hasWords
  # print(hasWords)

