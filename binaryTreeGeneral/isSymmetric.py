# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    if not root: return True

    leftLevel=[root.left] if root.left else []
    rightLevel=[root.right] if root.right else []
    
    
    while leftLevel and rightLevel:
        leftLength=len(leftLevel)
        if leftLength!=len(rightLevel): return False
        nextLeft=[]
        nextRight=[]
        for index in range(leftLength):
            leftNode=leftLevel[index]
            rightNode=rightLevel[-index-1]
            if not leftNode:
                if not rightNode: continue
                else: return False
            if not rightNode: return False
            

            if leftNode.val!=rightNode.val: return False
            nextLeft.append(leftNode.left)
            nextLeft.append(leftNode.right)
            nextRight.insert(0,rightNode.right)
            nextRight.insert(0,rightNode.left)
        leftLevel=nextLeft
        rightLevel=nextRight
    if leftLevel or rightLevel: return False
    return True
