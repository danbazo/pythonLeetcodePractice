def twoSum(nums, target):
  indexes=[i for i in range(len(nums))]

  sortedNums, sortedIndexes = zip(*sorted(zip(nums,indexes)))
  start=0
  end=len(nums)-1
  while True:
    if sortedNums[start]+sortedNums[end]==target:
        return [sortedIndexes[start],sortedIndexes[end]]
    elif sortedNums[start]+sortedNums[end]>target:
        end-=1
    else: start+=1
