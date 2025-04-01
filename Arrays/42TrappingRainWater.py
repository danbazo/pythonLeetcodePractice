def trap(height):
        #We initialize the variables we will use
        waterSum=0
        maxHeight=[]
        maxHeightIndex=[]
        up=True
        height.append(0)
       
        #We start our first loop, to determine the local maximums in the height array
        for i in range(len(height)-1):
            if up:
                if height[i]>height[i+1]:
                    maxHeight.append(height[i])
                    maxHeightIndex.append(i)
                    up=False
            else:
                if height[i]<height[i+1]:
                    up=True
       
        #if no loca maxiumums were found, return 0, as there will be no "valleys" for the water to deposit
        if not maxHeight:
            return 0
       
        #We start our second loop, this time on the array we created for the Maximums, to eliminate the ones between greater ones, as the water will be over those
        currentHighest=maxHeight[-1]
        for j in reversed(range(len(maxHeight)-1)):
            if maxHeight[j]<=currentHighest:
                while maxHeight[j]>maxHeight[j+1]:
                    del maxHeight[j+1]
                    del maxHeightIndex[j+1]
            else:
                while currentHighest>maxHeight[j+1]:
                    del maxHeight[j+1]
                    del maxHeightIndex[j+1]
                currentHighest=maxHeight[j]
        #We initialize th variables for out last loop, to calculate the water deposited, using the maximums array we crated, and the index array as well
        prevIndex=0
        nextIndex=maxHeightIndex[0]
        prevLevel=0
        nextLevel=maxHeight[0]
        for k in range(1,len(maxHeight)):
            prevIndex=nextIndex
            nextIndex=maxHeightIndex[k]
            prevLevel=nextLevel
            nextLevel=maxHeight[k]
            level=min(prevLevel,nextLevel)
            for h in range(prevIndex+1,nextIndex):
                diff=level-height[h]
                if diff>0:
                    waterSum+=(diff)
        return waterSum
