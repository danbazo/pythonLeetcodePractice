def longestConsecutive(nums):
    numsDict={}
    longest=0
    for element in nums:
      if element in numsDict:
        continue
      numsDict[element]=[element,element]
     
                
      if element+1 in numsDict:
        numsDict[numsDict[element][0]]=[numsDict[element][0],numsDict[element+1][1]]
        numsDict[numsDict[element+1][1]]=[numsDict[element][0],numsDict[element+1][1]]
        longest=max(numsDict[element+1][1]-numsDict[element][0]+1,longest)
      
      if element-1 in numsDict:
        numsDict[numsDict[element-1][0]]=[numsDict[element-1][0],numsDict[element][1]]
        numsDict[numsDict[element][1]]=[numsDict[element-1][0],numsDict[element][1]]
        longest=max(numsDict[element][1]-numsDict[element-1][0]+1,longest)
  

    return longest
