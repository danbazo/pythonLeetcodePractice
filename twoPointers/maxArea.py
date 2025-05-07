def maxArea(height):
  """
  Returns the maximum water area the a pair of heights from height can hold

  Keyword arguments:
  height: a list of heights. Any pair of heights form a "container"
  """
  #Initialize variables
  currentMax=0 #Keep tracks of the max area, to be returned in the end
  upper=len(height)-1 #upper pointer
  lower=0 #Lower pointer
  while not upper==lower: #Iterate until upper equals lower
    #Calculates the max volume measured so far
    currentMax=max(currentMax,min(height[upper],height[lower])*(upper-lower)) 
    #Move the smallest heigt of the pointers
    if height[upper]>height[lower]:
      lower+=1
    else: upper-=1
  return currentMax


#Example test
if __name__ == "__main__":
   print('Container with Most water test. height= [1,8,6,2,5,4,8,3,7]')
   print('Returns: ', maxArea( [1,8,6,2,5,4,8,3,7]))
