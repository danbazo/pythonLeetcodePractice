# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

  def reverseKGroup(head, k):
      
      fakeHead=ListNode(0,head)
      currentNode=fakeHead
      broken=False
      while currentNode:
          
          nodeMap={}
          
          tempNode=currentNode
          for i in range(k+1):
              tempNode=tempNode.next
              nodeMap[i]=tempNode
                              
              if i<k and not tempNode: 
                  broken=True
                  break
          if broken: break
          nodeMap[0].next=nodeMap[k]
          for i in range(1,k):
              nodeMap[i].next=nodeMap[i-1]
          currentNode.next=nodeMap[k-1]
          currentNode=nodeMap[0]
      
      
      
      return fakeHead.next
