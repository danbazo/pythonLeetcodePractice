def simplifyPath(path):
  """
  returns a string of the simplified version of the absolute path for a Unix-style file system, path

  Keyword arguments:
  path a string, valid absolute path for a Unix-style file system
  """
  #Dividing the given path by /
  pathList=path.split('/')
  #Initializing the stack list
  newPath=[]
  #Iterating over the list of split path
  for element in pathList:
    #If the element is empty (due to consecutives /) or a period (Current directory), we skip this element
    if not element or element=='.': continue
    #If the element are two periods, we go up one directory by removing the last item in newPath, if it exist
    elif element=='..':
      if newPath: newPath.pop()
    #In any other case, the element is added to the newPath list
    else: newPath.append(element)
  #The joined list newPath is returned, with a / at the beggining
  return '/'+'/'.join(newPath)

#Example test
if __name__ == "__main__":
  print('Simplify Path test.  path = "/home/user/Documents/../Pictures"')
  print('Returns: ', simplifyPath('/home/user/Documents/../Pictures'))
