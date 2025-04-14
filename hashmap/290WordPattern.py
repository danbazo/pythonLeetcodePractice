def wordPattern(pattern, s):
  """
  Returns a boolean indicating if a string pattern and a string s, find if follow the same pattern.
  
  Keyword arguments:
  s a string of words, separated by a single space
  pattern a string of characters
  """
      #split s into a list of words
      sList=s.split(' ')
      #Initialize mapDict to keep track of each letter in pattern mapped to a word in sList
      mapDict={}
      #If lengths are different, it cannot be mapped
      if len(pattern)!=len(sList): 
          return False
      
      for i in range(len(pattern)):
          if pattern[i] not in mapDict:
              if sList[i] not in mapDict.values():
                  mapDict[pattern[i]]=sList[i] #if a letter in pattern has not been mapped not has its counterpart word in sList, we map them
              else: return False #If the word in sList has been mapped before to another letter, return False
          elif mapDict[pattern[i]]!=sList[i]: return False #If a character in patter has benn mapped to another word in sList, return False
      return True
