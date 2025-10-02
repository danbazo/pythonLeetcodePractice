def ladderLength(beginWord, endWord, wordList):

  if endWord not in wordList: return 0
  wordLength=len(beginWord)
  wordPatterns={}
  checkedPattern=set()
  endPattern=set()
  changeCount=1
  for word in wordList:
      isEnd=word==endWord
      for i in range(wordLength):
          pattern=word[:i]+"*"+word[i+1:]
          if isEnd: endPattern.add(pattern)
          if pattern in wordPatterns:
              wordPatterns[pattern].append(word)
          else:
              wordPatterns[pattern]=[word]
  currentWords=[beginWord]
  while currentWords:
      nextWords=[]
      changeCount+=1
      for checkingWord in currentWords:
          
          for j in range(wordLength):
              currentPattern=checkingWord[:j]+"*"+checkingWord[j+1:]
              if currentPattern in endPattern: return changeCount
              if currentPattern in checkedPattern: continue
              checkedPattern.add(currentPattern)
              if currentPattern in wordPatterns:
                  nextWords.extend(wordPatterns[currentPattern])
      currentWords=nextWords            
  return 0
