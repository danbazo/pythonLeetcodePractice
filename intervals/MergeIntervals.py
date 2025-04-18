def merge(intervals):
  """
  returns a list of the intervals merged, so that each overlaped intervals is combined.

  Keyword arguments:
  intervals a list of lists of intervals
  """
  #Initialize the answer list
  mergedInter=[]
  #Check for empty lists and return and empty one as well
  if not intervals:
    return mergedInter
  #Sort the given list
  intervals.sort()
  #Initialize the values start and end, wich will be the values to for the answer list mergedInter
  start, end =intervals[0]
  
  #iterate once over the list, checking if our current end is greater than the start of the following interval, and smaller than the end of it
  for i in range(1,len(intervals)):
    if end>=intervals[i][0]:
      if end<intervals[i][1]:
        end=intervals[i][1]
    #Else we will append our interval into merged Inter and start a new one    
    else:
      mergedInter.append([start,end])
      start, end=intervals[i]
  #Merge the remaining interval outside of the loop        
  mergedInter.append([start,end])

  return mergedInter


__name__ == "__main__":
  print('Merge Intervals test. intervals=[[1,3],[2,6],[8,10],[15,18]]')
  print(merge('Returns: '[[1,3],[2,6],[8,10],[15,18]]))
