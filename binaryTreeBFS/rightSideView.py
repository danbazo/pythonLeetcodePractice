def rightSideView(root):

        def helper(root,level,viewed):
            if not root: return viewed
            if level>=len(viewed):
                viewed.append(root.val)
            viewed=helper(root.right,level+1,viewed)
            viewed=helper(root.left,level+1,viewed)
            return viewed
        return helper(root,0,[])
