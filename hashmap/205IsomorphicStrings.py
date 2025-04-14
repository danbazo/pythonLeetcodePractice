def isIsomorphic(s, t):
   """
  Returns a boolean indicating if the strings s and t are isomorphic.

  Keyword arguments:
  s a string of valid ascii character
  t a string of the same length as s
  """
      #Initialize the dictionary of mapped character betwwen s and t
        mappedChar={}
      #iterate over the lenght of the strings
        for i in range(len(s)):
            if s[i] not in mappedChar:
                if t[i] not in mappedChar.values():
                    mappedChar[s[i]]=t[i] #if a character in s has not been mapped not has its counterpart in t, we map them
                else:
                    return False #if the character is s has not been mapped, but the counterpart has, we would map the same character twice
            elif mappedChar[s[i]]!=t[i]:
                return False #if we have mapped the character in s, but the mapped character in t is different from the current t we would be mapping twice
        return True
