def trap(height):
        """
        returns an integer value of the sum of water trapped in the elevations given in height
        
        Keyword arguments:
        height a list of integers representing a 2D elevation map
        """
        
        #initialize the variables
        waterSum=0
        maxLeft=0
        maxRight=0
        left=0
        right=len(height)-1
        #Iterate over the height list from left and right using a 2 pointer approach
        while left<right:
            if height[left]<height[right]:
                if height[left]>maxLeft:
                    maxLeft=height[left]
                else:
                    waterSum+=maxLeft-height[left]
                left+=1
            else:
                if height[right]>maxRight:
                    maxRight=height[right]
                else:
                    waterSum+=maxRight-height[right]
                right-=1
        return waterSum
#Example test
if __name__ == "__main__":
   print('Trapping Rain Water Test. height = [0,1,0,2,1,0,1,3,2,1,2,1]')
   print('Returns: ', trap([0,1,0,2,1,0,1,3,2,1,2,1]))
