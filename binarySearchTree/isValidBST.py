def isValidBST(root):
        isBST=True
        def helper(root,isBST):
            
            if root.left:
                smallLeft,bigLeft,isBST=helper(root.left,isBST)
                if not isBST or bigLeft>=root.val: return None, None, False
            
            else:
                smallLeft=root.val
            if root.right:
                smallRight,bigRight,isBST=helper(root.right,isBST)
                if not isBST or smallRight<=root.val: return None, None, False
            else:
                bigRight=root.val
            return smallLeft,bigRight,isBST
        
        return helper(root,isBST)[2]
