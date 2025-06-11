
# Definition for a Node.
class Node:
    def __init__(self, val = 0, left = None, right = None, next = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root):
    if not root: return root
    levelDummy=Node(None)
    levelPointer=levelDummy
    currentNode=root
    while currentNode:
        while currentNode:
            if currentNode.left:
                levelPointer.next=currentNode.left
                levelPointer=levelPointer.next
            if currentNode.right:
                levelPointer.next=currentNode.right
                levelPointer=levelPointer.next
            currentNode=currentNode.next
        currentNode=levelDummy.next
        levelDummy=Node(None)
        levelPointer=levelDummy
    return root
