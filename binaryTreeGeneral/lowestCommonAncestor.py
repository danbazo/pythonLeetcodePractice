def lowestCommonAncestor(root, p, q):
        

        def helper(root,p,q):

            if not root:
                return 0
            if root==p or root==q:
                found=1
            else: found=0
            left=helper(root.left,p,q)
            if left==2:
                return 2
            else:
                found+=left
            if found==2:
                common[0]=root
                return 2
            right=helper(root.right,p,q)
            if right==2:
                return 2
            else:
                found+=right
            if found==2:
                common[0]=root
                return 2
            return found
        common=[None]
        helper(root,p,q)
        return common[0]
