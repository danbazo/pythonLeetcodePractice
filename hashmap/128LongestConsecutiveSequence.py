def longestConsecutive(nums):
    numsDict={}
    longest=0
    for element in nums:
        if element in numsDict:
        continue
        numsDict[element]=[element,element]
        upper=element
        lower=element
        if element+1 in numsDict:
            upper=numsDict[element+1][1]

        if element-1 in numsDict:
            lower=numsDict[element-1][0]
        longest=max(upper-lower+1,longest)
        
        numsDict[lower]=[lower,upper]
        numsDict[upper]=[lower,upper]
    
    
    
    return longest
