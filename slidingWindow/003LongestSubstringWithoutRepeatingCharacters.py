def lengthOfLongestSubstring(s):
  """
  Returns an Integer indicating the maximun length of a substring o s without repeating characters.

  Keyword arguments:
  s a string
  """     
  
  sSub=''
  maxLength=0
  
  for i in range(len(s)):
      try:
          j=sSub.index(s[i])
          maxLength=max(maxLength,len(sSub))
          sSub=sSub[j+1:]
      except ValueError:
          pass
                          
      sSub+=s[i]
      
  maxLength=max(maxLength,len(sSub))
  return maxLength
