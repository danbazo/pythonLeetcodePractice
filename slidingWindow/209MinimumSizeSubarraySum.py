def minSubArrayLen(target, nums):
        minLength=0
        
        front=0
        currentSum=nums[0]
        totalLength=len(nums)
        for i in range(totalLength):
            while currentSum<target:
                if front==totalLength-1: 
                    return minLength
                    
                front+=1
                currentSum+=nums[front]
                
            
            if minLength:
                minLength=min(minLength,front-i+1)
            else:
                minLength=front-i+1
          
            currentSum-=nums[i]

        return minLength
