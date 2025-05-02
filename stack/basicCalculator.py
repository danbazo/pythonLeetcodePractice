def calculate(s):
        ops={'+':lambda x,y:x+y,
        '-': lambda x,y:x-y}
        i=0
        def helper(s,i):
            total=0
            num=0
            operation='+'
            
            while i<len(s):
                if s[i].isdigit():
                    num=num*10+int(s[i])
                
                else:
                    if num:
                        total=ops[operation](total,num)
                        num=0
                    if s[i]==' ':
                        pass
                    elif s[i]=='(':
                        toSum,iIncreased=helper(s,i+1)
                        total=ops[operation](total,toSum)
                        i=iIncreased
                    elif s[i]==')':
                        
                        return total,i
                    else:
                        operation=s[i]
                        
                i+=1
            if num:
                total=ops[operation](total,num)
            return total,i
        return helper(s,i)[0]
