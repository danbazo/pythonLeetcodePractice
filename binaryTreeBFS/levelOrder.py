def levelOrder(root):
        levels=[]
        if not root: return levels
        currentLevel=[root]
        while currentLevel:
            nextLevel=[]
            levelValues=[]
            for node in currentLevel:
                levelValues.append(node.val)
                if node.left: nextLevel.append(node.left)
                if node.right: nextLevel.append(node.right)
            currentLevel=nextLevel
            levels.append(levelValues)

        return levels
