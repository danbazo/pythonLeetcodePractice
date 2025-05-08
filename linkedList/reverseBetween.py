# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseBetween(head, left, right):
        if right==left:
            return head
        span=right+left
        i=1
        mappedList={}
        currentNode=head
        while currentNode:
            if left<=i<=right+1:
                mappedList[i]=currentNode
            currentNode=currentNode.next
            i+=1
        if 1 in mappedList:
            head=mappedList[right]
        
        currentNode=head
        i=1
        while currentNode:
            if left-1<=i<=right-1:
                currentNode.next=mappedList[span-i-1]
            elif i==right:
                if i+1 in mappedList:
                    currentNode.next=mappedList[i+1]
                else: currentNode.next=None
            currentNode=currentNode.next
            i+=1
        
        return head
