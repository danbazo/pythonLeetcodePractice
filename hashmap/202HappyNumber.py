def isHappy(n):
  """
  returns a boolean indicating if integer n is a happy number.

  Keyword arguments:
  n an integer
  """
  
  #Initilize a set to keep track of numbers checked and detecting a loop
  cycled=set()
  #Loop untill we reach our answer or we detect a cycle
  while n not in cycled:
    #Add the current number to our cycle set
    cycled.add(n)
    #Initilize the sum of squares
    squareSum=0
    #loop through the digits of n
    while n:
      squareSum+=(n%10)**2
      n=n//10
    #If the solution is found, return true
    if squareSum==1: return True
    #Else, use the sum of squares we calculated as the new n
    else:
      n=squareSum
  #if the loop is exited for detecting a cycle, return False
  return False
