def summaryRanges(nums):
    """
    returns a list of strings indicating the start and end of each range within nums.
    
    Keyword arguments:
    nums a list of integers, unique and sorted
  
    """
    #Initialize the list ranges, which will be the returned object
    ranges=[]
    #if nums is empty, an empty list will be returned
    if not nums:
      return ranges
    #Initialize the first value of the starting number of the ranges
    start=nums[0]
    
    #Loop once though the whole nums list, save the last number
    for i in range(len(nums)-1):
        #If the next number is not the current one plus one, finish the range and append its string into ranges
      if nums[i+1]!=nums[i]+1:
        if start==nums[i]:
          ranges.append(str(start))
        else:
          ranges.append(f"{start}->{nums[i]}")
        start=nums[i+1]

    #Finish the last range
    if start==nums[-1]:
      ranges.append(str(start))
    else:
      ranges.append(str(start)+'->'+str(nums[-1]))
            
    return ranges


if __name__ == "__main__":
    print('Summary Ranges test: nums=[0,2,3,4,6,8,9]')
    print('Returns:',summaryRanges([0,2,3,4,6,8,9]))
