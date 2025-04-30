def isValid(s):
  """
  returns a boolean indicating if the string s has valid parentheses, oening and closing corrently

  Keyword arguments:
  s a string of only parentheses characters
  """
  #Initialize the list of opening parentheses
  parenthCount=[]
  #Create a dictionary matchin opening and closing parentheses
  parenthMatch={')':'(','}':'{',']':'['}
  #Iterate over the string s
  for character in s:
    if character in parenthMatch: #If a closing parentheses ist found
      #Check if the last opening parentheses matches it, if not, returns False
      if not parenthCount or parenthCount[-1]!=parenthMatch[character]:
        return False
      #If it matches, remove the opening parentheses from the list, having succesfully closed it
      else: parenthCount.pop()
    #if its an opning parentheses, its added to end of the list
    else: parenthCount.append(character)
  #If there are still unclosed parentheses, return False
  if parenthCount: return False
  return True

#Example test
if __name__ == "__main__":
  print('Valid Parentheses test. s = ([])')
  print('Returns: ', isValid('([])'))
