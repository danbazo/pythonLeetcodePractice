def minSubArrayLen(target, nums):
        minLength=0
        end=False
        front=0
        currentSum=nums[0]
        totalLength=len(nums)
        for i in range(totalLength):
            while currentSum<target:
                if front==totalLength-1: 
                    end=True
                    break
                front+=1
                currentSum+=nums[front]
                
            if end: break
            if minLength:
                minLength=min(minLength,front-i+1)
            else:
                minLength=front-i+1
          
            currentSum-=nums[i]

        return minLength
