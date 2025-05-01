class MinStack:
    """
    MinStack supports stack operations with constant-time retrieval of the minimum element.

    Methods:
    - push(val): Pushes the element onto the stack.
    - pop(): Removes the element on top of the stack.
    - top(): Gets the top element.
    - getMin(): Retrieves the minimum element in the stack.

    """
  def __init__(self):
    # Initialize main stack to store values
    self.stack=[]
    # Initialize min stack to keep track of minimums.
    # Start with 'infinity' to handle edge cases easily.
    self.stackMin=[float('inf')]
      
  
  def push(self, val):
    # Push value to main stack
    self.stack.append(val)
    # Push the smaller value between current and previous min to min stack
    if val<self.stackMin[-1]:
      self.stackMin.append(val)
    else:
      self.stackMin.append(self.stackMin[-1])

  def pop(self):
    # Pop from both stacks to maintain alignment  
    self.stack.pop()
    self.stackMin.pop()
  
  def top(self):
     # Return the top of the main stack
    return self.stack[-1]
  
  def getMin(self):
    # Return the current minimum from the min stack
    return self.stackMin[-1]
