def containsNearbyDuplicate(nums, k):
  #Initialize the dictionary to keep track of numbers and indexes
  numsDict={}
  #Loop through the nums list
  for i in range(len(nums)):
    #Check if number has been seen, if so, check if its close enough to current number. If one of these conditions is not met, add/replace the index of the number
    if (nums[i] not in numsDict) or i- numsDict[nums[i]]>k:
      numsDict[nums[i]]=i
    #Return true otherwise
    else:
      return True
  #return false if through the loop no answer was found
  return False
                
