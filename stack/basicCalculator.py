def calculate(s):
        stack=[]
        operation=[]
        def suma(x,y):
            return x+y
        def subs(x,y):
            return x-y
        ops={'+':suma,
        '-': subs}
        opened=False
        numStart=-1
        numStarted=False
        for i in range(len(s)):
            if s[i].isdigit():
                if numStarted==False:
                    numStart=i
                    numStarted=True   

            else:
                if numStarted:
                    numStarted=False
                    if opened or not operation:
                        stack.append(int(s[numStart:i]))
                        opened=False
                    else:
                       
                        stack.append(operation.pop()(stack.pop(),int(s[numStart:i])))


                if s[i]==' ':
                    if numStarted:
                        numStarted=False
                        stack.append(int(s[numStart:i]))
                
                elif s[i]=='(':
                    opened=True
                elif s[i]==')':
                    if len(stack)==1:
                        continue
                    second=stack.pop()
                    first=stack.pop()
                    stack.append(operation.pop()(first,second))
                    
                else:
                    if opened or not stack:
                        stack.append(0)
                        opened=False

                    
                    operation.append(ops[s[i]])
        if numStarted:

            if opened or not operation:
                stack.append(int(s[numStart:]))
                opened=False
            else:
                stack.append(operation.pop()(stack.pop(),int(s[numStart:])))
        
        return stack[0]
