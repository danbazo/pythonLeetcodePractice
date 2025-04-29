def findMinArrowShots(points):
  """
  returns an integer value of the minimum arrows neede to busrts vallons represented in points

  Keyword arguments:
  points a list of the ends and starts locations of the ballons, horizantally
  """
  #In case of an empty list, return 0
  if not points:
    return 0
  #Sort the list      
  points.sort()
  #Initialize the count and the upper value to keep track of where a ballon can be popped
  arrowCount=1
  upper=points[0][1]
  #iterate over the list points, minus the first item
  for i in range(1,len(points)):
    if points[i][0]<=upper: #if the next ballon is overlaps, the upper value is updated to the minimum between the current one and the balloon
      upper=min(upper,points[i][1])
    else: #else, we add one arrow and update the upper value
      arrowCount+=1
      upper=points[i][1]
  
     
  return arrowCount

if __name__ == "__main__":
  print('Minimum Number of Arrows to Burst Balloons test. points = [[1,2],[2,3],[3,4],[4,5]]')
  print('Returns: ', findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
