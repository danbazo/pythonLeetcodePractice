# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def removeNthFromEnd(head, n):
    
    fakeHead=ListNode(0,head)
    before=fakeHead
    after=fakeHead.next.next
    currentNode=head
    toEnd=0
    while currentNode:
        if toEnd==n:
            before=before.next
            after=after.next
        else:
            toEnd+=1
        currentNode=currentNode.next
    before.next=after
    return fakeHead.next
