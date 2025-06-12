# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def sumNumbers(root):
    
    def helper(node,partSum):
        if not node: 
            
            return 0
        
        partSum=partSum*10+node.val
        
        if not node.left and not node.right:
            return partSum
    
        else:   
            return helper(node.left,partSum)+helper(node.right,partSum)
        
    return helper(root,0)
   
  
