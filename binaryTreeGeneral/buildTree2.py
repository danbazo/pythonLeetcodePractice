# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    inorderMap={}
    for index in range(len(inorder)):
        inorderMap[inorder[index]]=index
    
    currentIndex=[len(inorder)-1]


    def buildNode(down,up):
        if up==down:return None
        if currentIndex[0]==-1:return None
        
        nodeVal=postorder[currentIndex[0]]
        currentIndex[0]-=1
        
        node=TreeNode(nodeVal)
        node.right=buildNode(inorderMap[nodeVal]+1,up)
        node.left=buildNode(down,inorderMap[nodeVal])
        
        return node

    return buildNode(0,len(inorder))
