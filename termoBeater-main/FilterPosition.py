def filterPosition(wordList, letter, position):
  matchWords = []
  for word in wordList:
    if word[position-1] == letter:
      if not word in matchWords:
        matchWords.append(word)
    
  return matchWords

def filterNotInPosition(wordList, letter, position):
  matchWords = []

  for word in wordList:
    if word[position-1] != letter:
      if not word in matchWords:
        matchWords.append(word)

  return matchWords
# print(matchWords)