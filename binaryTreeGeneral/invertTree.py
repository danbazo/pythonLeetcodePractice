# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root: return root
    currentLevel=[root]
    while currentLevel:
        nextLevel=[]
        for node in currentLevel:
            node.left, node.right = node.right, node.left
            if node.left: nextLevel.append(node.left)
            if node.right: nextLevel.append(node.right)
        currentLevel=nextLevel
    return root
