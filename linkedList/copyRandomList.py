
# Definition for a Node.
class Node:
  def __init__(self, x:, next = None, random= None):
      self.val = int(x)
      self.next = next
      self.random = random
  def printList(self):
    nodes = []
    head=self
    while head:
        random_val = head.random.val if head.random else None
        nodes.append(f"[Val: {head.val}, Random: {random_val}]")
        head = head.next
    print(" -> ".join(nodes))


def copyRandomList(head):
  """
  returns the head of the copied linked list, given that the originally has a next pointer and a random one

  Keyword arguments:
  head the head of a linked list with next and random pointers
  """
  if not head:
    return None
  # Dictionary to map original nodes to their copies
  randomMap={}

  # First pass: create copy nodes and map them
  currentOrig=head
  copiedHead=Node(currentOrig.val)
  currentCopy=copiedHead
  randomMap[currentOrig]=currentCopy
  currentOrig=currentOrig.next
  
  while currentOrig:
    currentCopy.next=Node(currentOrig.val)
    currentCopy=currentCopy.next
    randomMap[currentOrig]=currentCopy
    currentOrig=currentOrig.next
  # Second pass: assign random pointers
  currentOrig=head
  currentCopy=copiedHead
  while currentOrig:
    currentCopy.random=randomMap[currentOrig.random] if currentOrig.random else None
    currentOrig=currentOrig.next
    currentCopy=currentCopy.next
  return copiedHead


