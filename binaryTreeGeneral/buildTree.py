# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    
    
    inorderMap={}
    for index in range(len(inorder)):
        inorderMap[inorder[index]]=index
    
    currentIndex=[0]
    

    def buildNode(down,up):
        if up==down:return None
        if currentIndex[0]==len(inorder):return None
        nodeVal=preorder[currentIndex[0]]
        currentIndex[0]+=1
        
        node=TreeNode(nodeVal)
        node.left=buildNode(down,inorderMap[nodeVal])
        node.right=buildNode(inorderMap[nodeVal]+1,up)
        return node
    
    return buildNode(0,len(inorder))


