"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

def connect(self, root: 'Node') -> 'Node':
  if not root: return root
  currentLevel=[root]
  while currentLevel:
      nextLevel=[]
      for index in range(len(currentLevel)):
          node=currentLevel[index]
          if node.left: nextLevel.append(node.left)
          if node.right: nextLevel.append(node.right)
          if index<len(currentLevel)-1:
             node.next=currentLevel[index+1]
      currentLevel=nextLevel
  return root


