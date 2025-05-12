# Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def deleteDuplicates(head):
    duplicated=False
    if not head: return None
    fakeHead=ListNode(None,head)
    prevNode=fakeHead
    currentNode=fakeHead.next

    while currentNode.next:
        if duplicated:
            if currentNode.val==currentNode.next.val:
                currentNode.next=currentNode.next.next
            else:
                prevNode.next=currentNode.next
                currentNode=prevNode.next
                duplicated=False
        else:
            if currentNode.val==currentNode.next.val:
                duplicated=True
                currentNode.next=currentNode.next.next
            else:
                prevNode=currentNode
                currentNode=currentNode.next
    if duplicated:
        prevNode.next=currentNode.next

    return fakeHead.next
