class Node:
    def __init__(self,key, val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None
   

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.usedCap=0
        self.cache={}
        self.firstNode=Node('first',None)
        self.lastNode=Node('last',None)
        self.firstNode.next=self.lastNode
        self.lastNode.prev=self.firstNode
        
    def _remove(self, node):
        prevNode=node.prev
        nextNode=node.next
        prevNode.next=nextNode
        nextNode.prev=prevNode

    def _append(self, node):
        recentNode=self.lastNode.prev
        recentNode.next=node
        node.prev=recentNode
        node.next=self.lastNode
        self.lastNode.prev=node

    def get(self, key: int) -> int:
        if key in self.cache:
            currentNode=self.cache[key]
            
            if currentNode.next!=self.lastNode:
                self._remove(currentNode)
                self._append(currentNode)

            return currentNode.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            currentNode=self.cache[key]
            currentNode.val=value
            
            if currentNode.next!=self.lastNode:
                self._remove(currentNode)
                self._append(currentNode)
  

        else:
            currentNode=Node(key,value)
            self.cache[key]=currentNode
            self._append(currentNode)
            
            if self.usedCap==self.cap:
                delNode=self.firstNode.next
                self._remove(delNode)
                del self.cache[delNode.key]
                

            else:
                self.usedCap+=1
            



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
