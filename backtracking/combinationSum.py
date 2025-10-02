def combinationSum(candidates, target):
    combinations=[]
    currentComb=[]
    
    def helper(currentSum,position):
        if currentSum==target:
            combinations.append(currentComb.copy())
        elif currentSum<target:
            for i in range(position,len(candidates)):
                currentComb.append(candidates[i])
                helper(currentSum+candidates[i],i)
                currentComb.pop()
    helper(0,0)
    return combinations
                
