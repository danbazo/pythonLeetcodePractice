def evalRPN(tokens):
   """
   returns an integer value of the evliated arithmetic expression in a Reverse Polish Notation given by tokens
   
   Keyword arguments:
   tokens a list of strings that represents an arithmetic expression in a Reverse Polish Notation.
   """
   #Initialize the stack list
   stack=[]
   #Create a dictionary opts to convert the string operators into functions
   ops={'+':lambda x, y: x+y,
      '/':lambda x, y: int(x/y), #Its requested that division operation truncates toward zero.
      '-':lambda x,y:x-y,
      '*':lambda x,y:x*y}
   #Iterate over the list tokens
   for element in tokens:
      #Any time an operator is found, said operation is applied to the last two items in the stack, and the result is appended at the end
      if element in ops:
         second=stack.pop()
         first=stack.pop()
   
         stack.append(ops[element](first,second))
   
      #If a number is found, its appended at the end of the stack as an integer
      else:
         stack.append(int(element))
   #The last remaining element of the stack is returned
   return stack[0]
#Example test
if __name__ == "__main__":
   print('Evaluate Reverse Polish Notation test. tokens = ["2","1","+","3","*"]')
   print('Returns: ', evalRPN(["2","1","+","3","*"]))
