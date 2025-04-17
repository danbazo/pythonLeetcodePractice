def summaryRanges(nums):
    ranges=[]
    if not nums:
      return ranges
    start=nums[0]
    i=0
    while i<len(nums)-1:
      if nums[i+1]!=nums[i]+1:
        if start==nums[i]:
          ranges.append(str(start))
        else:
          ranges.append(str(start)+'->'+str(nums[i]))
        start=nums[i+1]

      i+=1
    if start==nums[-1]:
      ranges.append(str(start))
    else:
      ranges.append(str(start)+'->'+str(nums[-1]))
            
    return ranges
