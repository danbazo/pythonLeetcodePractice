def countNodes(root):
        
        def helper(node,leftDepth,rightDepth):
            if not leftDepth:
                leftNode=node
                leftDepth=0
                while leftNode:
                    leftDepth+=1
                    leftNode=leftNode.left
            if not rightDepth:
                rightNode=node
                rightDepth=0
                while rightNode:
                    rightDepth+=1
                    rightNode=rightNode.right
            if leftDepth==rightDepth:
                return (2**leftDepth)-1
            return 1+helper(node.left,leftDepth-1,None)+helper(node.right,None,rightDepth-1)
        
        return helper(root,None,None)
