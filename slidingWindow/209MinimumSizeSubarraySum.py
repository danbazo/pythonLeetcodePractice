def minSubArrayLen(target, nums):
        """
        Returns an integer denoting the smallest length that a subsequence of nums sum up to or more than target. If no subsequence is found, returns 0.

        Keyword arguments:
        targer an integer
        nums an list of positive integers
        """
        #we initialize our variables
        #minLength to zero, as it will be the value returned if no solution is found
        minLength=0
        #front to 0, as it will be the fron pointer of our sliding window
        front=0
        #currentSUm to the first element of the array, as its where we are starting
        currentSum=nums[0]
        totalLength=len(nums)
        #we will iterate over the whole nums array
        for i in range(totalLength):
        #while we dont reach our target, we will keep adding elements to the right, increasing the window   
            while currentSum<target:
                #if we reach the end of the array on the right, and our current sum is no bigger than the target, we will finish our function
                if front==totalLength-1: 
                    return minLength
                front+=1
                currentSum+=nums[front]
                
            #we will update minLength with the smallest length of subsequence that sum up to or over our target value
            if minLength:
                minLength=min(minLength,front-i+1)
            else:
                minLength=front-i+1
        
            currentSum-=nums[i]

        return minLength
