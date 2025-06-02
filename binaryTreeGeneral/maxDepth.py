# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth=0
        currentLevel=[root]
        while currentLevel:
            depth+=1
            nextLevel=[]
            for node in currentLevel:
                if node.left: nextLevel.append(node.left)
                if node.right: nextLevel.append(node.right)
            currentLevel=nextLevel
        return depth
