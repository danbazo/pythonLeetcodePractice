# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def maxPathSum(root):


    maxSum=[float('-inf')]
    def helper(node):
        if not node:
            return 0
        
        if not node.left and not node.right:
            maxSum[0]=max(maxSum[0],node.val)
            
            return max(node.val,0)
        left=helper(node.left)
        right=helper(node.right)
        maxSum[0]=max(maxSum[0],left+right+node.val)
        return max(left+node.val,right+node.val,node.val,0)
    helper(root)
    return maxSum[0]
