 def averageOfLevels(root)]:
        currentLevel=[root]
        average=[]
        while currentLevel:
            nextLevel=[]
            levelSum=0
            levelCount=0
            for node in currentLevel:
                levelSum+=node.val
                levelCount+=1
                if node.left:nextLevel.append(node.left)
                if node.right: nextLevel.append(node.right)
            currentLevel=nextLevel
            average.append(levelSum/levelCount)
        return average
