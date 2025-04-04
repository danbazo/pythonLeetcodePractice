def maxArea(height):
  """
  Returns the maximum water area the a pair of heights from height can hold

  Keyword arguments:
  height: a list of heights. Any pair of heights form a "container"
  """
  currentMax=0
  upper=len(height)-1
  lower=0
  while not upper==lower:
    currentMax=max(currentMax,min(height[upper],height[lower])*(upper-lower))
    if height[upper]>height[lower]:
      lower+=1
    else: upper-=1
  return currentMax
