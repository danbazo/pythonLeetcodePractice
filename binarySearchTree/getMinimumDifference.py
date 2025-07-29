def getMinimumDifference(root):

        def helper(root):
            currentDiff=float('inf')
            currentMax=root.val
            currentMin=root.val
            if root.left:
                leftMin,leftMax,leftDiff=helper(root.left)
                currentDiff=min(root.val-leftMax,leftDiff)
                currentMin=leftMin
            if root.right:
                rightMin,rightMax,rightDiff=helper(root.right)
                currentDiff=min(rightMin-root.val,rightDiff,currentDiff)
                currentMax=rightMax
            return currentMin,currentMax,currentDiff
        return helper(root)[2]
