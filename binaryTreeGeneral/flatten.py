# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def flatten(self, root: Optional[TreeNode]) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    
    preList=[]
    def helper(node):
        if not node: return None
        preList.append(node)
        helper(node.left)
        helper(node.right)
    helper(root)
    for i in range(len(preList)-1):
        preList[i].right=preList[i+1]
        preList[i].left=None
