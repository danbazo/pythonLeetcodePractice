def isAnagram(s, t):
  """
  Returns a boolean indicating s and t are anagrams of eachother.

  Keyword arguments:
  s a string of valid ascii character
  t a string of valid ascii character
  """
  #If length are different, s and t cannot be anagrams
  if len(s)!=len(t): return False
  #create a doctionary of character frequency of s
  letterCount={}
  for letter in s:
    if letter in letterCount:
      letterCount[letter]+=1
    else:
      letterCount[letter]=1
  #check if all characters in t are in the frequency map, and if there is enough amount of them
  for character in t:
    if character in letterCount and letterCount[character]>0:
      letterCount[character]-=1
    else:
      return False
  return True
