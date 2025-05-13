# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
    fakeHead=ListNode(None, head)
    firstNode=fakeHead
    currentNode=firstNode
    while currentNode.next:
        if currentNode.next.val<x:
            if currentNode==firstNode:
                firstNode=firstNode.next
                currentNode=firstNode
                
            else:
                
                toMove=currentNode.next
                currentNode.next=currentNode.next.next
                toMove.next=firstNode.next
                firstNode.next=toMove
                firstNode=firstNode.next
                
        else:
            currentNode=currentNode.next
            
    return fakeHead.next
