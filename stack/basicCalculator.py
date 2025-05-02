def calculate(s):
        """
        returns an integer value of the result of the calculations in the string s

        Keyword arguments:
        s a string of a valid expresion of a calculation, expressed in numbers, spaces, '+' and '-' signs and parentheses
        """
        #Create a dictionary opts to convert the string operators into functions
        ops={'+':lambda x,y:x+y,
        '-': lambda x,y:x-y}
        
        #Initialize the number variable, to add digits of numbers found
        num=''
        #Initialize the sign as positive, to keep track of the last operator found
        sign='+'
        #Initialize the stack, where the operations are being handled, and parenthesis are kept track of
        stack=[0]
        #Iterate over the string s
        for character in s:
                #If the character is a number, we add it to the current num string
                if character.isdigit():
                        num+=character
                #If its an empty space, we skip the loop
                elif character==' ':continue
                #Else, it will be an operator or parentheses
                else:
                        #If we have a number num, we add it to the lastest value in the stack with the current sign and reset num
                        if num:
                            stack[-1]=ops[sign](stack[-1],int(num))
                            num=''
                        #If the character is an operator, we update the sign
                        if character in ops:
                            sign=character
                        #Else, if its an opening bracket, we append the current sign to the stack and a cero, initilizing a new calculation inside a bracket, and reset the sign as '+'
                        elif character=='(':
                            
                            stack.append(sign)
                            stack.append(0)
                            sign='+'
                        #Else, the character will be a closing bracket, in which case the last number of the stack (the sum inside the brackets) will be added using the operator in the stack to the previous number
                        #This handles nested brackets correctly
                        else:
                            
                            y=stack.pop()
                            operation=stack.pop()
                            stack[-1]=ops[operation](stack[-1],y)
        #In the end, if there are still a number left not added, its done so
        if num: stack[-1]+=int(sign+num)
        #Return the only left number in the stack
        return stack[0]

#Example test
if __name__ == "__main__":
   print('Basic Calculator test. s = "(1+(4+5+2)-3)+(6+8)"')
   print('Returns: ', calculate("(1+(4+5+2)-3)+(6+8)"))
