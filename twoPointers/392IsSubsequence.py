def isSubsequence(s,t):
"""Returns a boolean indicating if s is a subsequence of t.

  Keyword arguments:
  s a string
  t a string
  """
#if s is bigger than t, it cannot be a subsequence
  if len(s)>len(t):
    return False
      
#we check every element of s in t. If we find a match, we go to the next s character, starting were we left off (using pointer)
#if we finish the run on t without finding a match, we return False
  pointer=0
  for i in range(len(s)):
      match=False
      for j in(range(pointer,len(t))):
          
          if s[i]==t[j]:
              pointer=j+1
              match=True
              break
      if not match: return False
  return True
      
