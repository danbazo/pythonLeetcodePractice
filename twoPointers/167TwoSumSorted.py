def twoSum(numbers, target):
        if target<numbers[-1]:
            for i in range(len(numbers)-1):
                for j in range(i+1,len(numbers)):
                    if numbers[i]+numbers[j]==target:
                        return [i+1,j+1]
                    elif numbers[i]+numbers[j]>target:
                        break
        else:
            for i in range(len(numbers)-1,0,-1):
                for j in range(i-1,-1,-1):
                    if numbers[i]+numbers[j]==target:
                        return [j+1,i+1]
                    elif numbers[i]+numbers[j]<target:
                        break
