def findWords(board, words):
      m=len(board)
      n=len(board[0])

      wordsTrie={}
      for word in words:
          currentLevel=wordsTrie
          for letter in word:
              if letter not in currentLevel:
                  currentLevel[letter]={'count':0}
                  
              currentLevel=currentLevel[letter]
              currentLevel['count']+=1
          currentLevel['#']=word
      
      foundWords=[]
      def isWord(currentLetter,trieLevel,row, column):
          
          if currentLetter in trieLevel:
              board[row][column]='#'
              nextTrieLevel=trieLevel[currentLetter]
              if nextTrieLevel['count']>0:
                  if '#' in nextTrieLevel: 
                      foundWord=nextTrieLevel['#']
                      foundWords.append(foundWord)
                      removeLevel=wordsTrie
                      for character in foundWord:
                          removeLevel=removeLevel[character]
                          removeLevel['count']-=1
                      del nextTrieLevel['#']
                  
                  for i,j in [(0,1),(0,-1),(1,0),(-1,0)]:
                      nextRow=row +i
                      nextColumn=column + j
                      
                      if 0 <= nextRow < m and 0 <= nextColumn < n and board[nextRow][nextColumn]!='#':
                          nextLetter=board[nextRow][nextColumn]
                          

                          isWord(nextLetter,nextTrieLevel,nextRow,nextColumn)
                       
              board[row][column]=currentLetter

      for row in range(m):
          for column in range(n):

              isWord(board[row][column],wordsTrie,row,column)


        return foundWords
