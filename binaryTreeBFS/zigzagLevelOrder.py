def zigzagLevelOrder(root):
        levels=[]
        if not root: return levels
        currentLevel=[root]
        right=True
        while currentLevel:
            nextLevel=[]
            levelValues=[]
            for i in range(len(currentLevel)):
                j= i if right else -i-1
                levelValues.append(currentLevel[j].val)
                if currentLevel[i].left: nextLevel.append(currentLevel[i].left)
                if currentLevel[i].right: nextLevel.append(currentLevel[i].right)
            right=not right
            currentLevel=nextLevel
            levels.append(levelValues)

        return levels
