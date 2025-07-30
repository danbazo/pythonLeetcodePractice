def cloneGraph(node):
        if not node: return None
        first=Node(node.val)
        nodeDict={first.val:first}

        def cloner(node,newNode):
            for neighbor in node.neighbors:
            
                if neighbor.val in nodeDict:
                    newNode.neighbors.append(nodeDict[neighbor.val])
                    
                else:
                    newNeighbor=Node(neighbor.val)
                    newNode.neighbors.append(newNeighbor)
                    nodeDict[newNeighbor.val]=newNeighbor
                    cloner(neighbor,newNeighbor)
        cloner(node,first)
        return first
