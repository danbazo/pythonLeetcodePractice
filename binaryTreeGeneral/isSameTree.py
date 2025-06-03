# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p:
        if not q: return True
        else: return False
    if not q: return False
    pLayer=[p]
    qLayer=[q]
    while pLayer and qLayer:
        pLength=len(pLayer)
        if pLength!=len(qLayer):
            return False
        pLayerNext=[]
        qLayerNext=[]
        for index in range(pLength):
            pNode=pLayer[index]
            qNode=qLayer[index]
            if not pNode:
                if not qNode:
                    continue
                else:
                    return False
            elif not qNode: return False

            if pNode.val!=qNode.val: return False
            pLayerNext.append(pNode.left)
            pLayerNext.append(pNode.right)
            qLayerNext.append(qNode.left)
                qLayerNext.append(qNode.right)
            pLayer=pLayerNext
            qLayer=qLayerNext
        return True
