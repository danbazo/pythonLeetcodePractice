# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

def rotateRight( head, k):
    if not head: return None
    if not k: return head
    nodeMap={}
    i=0
    currentNode=head
    while currentNode:
        nodeMap[i]=currentNode
        currentNode=currentNode.next
        i+=1
    length=len(nodeMap)
    kNew=k%length
    if not kNew: return head

    nodeMap[length-kNew-1].next=None
    newHead=nodeMap[length-kNew]
    nodeMap[length-1].next=head
    return newHead
