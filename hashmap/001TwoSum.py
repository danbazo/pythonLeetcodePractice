def twoSum(nums, target):
  """
  returns a list with the indexes of the two integers in nums that sum up the target value.

  Keyword arguments:
  nums a list of integers
  target an integer
  """
  #Initialize the dictionary where the values and indexes of nums will be stored
  numsDict={}

  #loop though the list nums, storing the values and indexes and comparing if we find the sum of the target value
  for i in range(len(nums)):
    complement=target-nums[i]
    if complement in numsDict:
      return [i,numsDict[complement]]
    else:
      numsDict[nums[i]]=i
