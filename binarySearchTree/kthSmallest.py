 def kthSmallest(root, k):
        found=False
        smallest=[]
        def helper(root,k,found):
            if found or not root:
                return found
            found=helper(root.left,k,found)
            smallest.append(root.val)
            if len(smallest)==k:
                found=True
            if not found:
                found=helper(root.right,k,found)
            return found
        
        helper(root,k,found)
        return smallest[k-1]
