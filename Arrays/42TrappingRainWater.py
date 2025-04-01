def trap(height):
        waterSum=0
        maxHeight=[]
        maxHeightIndex=[]
        up=True
        height.append(0)
        for i in range(len(height)-1):
            if up:
                if height[i]>height[i+1]:
                    maxHeight.append(height[i])
                    maxHeightIndex.append(i)
                    up=False
            else:
                if height[i]<height[i+1]:
                    up=True
        if not maxHeight:
            return 0
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
