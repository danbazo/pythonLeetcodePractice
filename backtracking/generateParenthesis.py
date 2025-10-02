def generateParenthesis(n):
    combinations=[]
    
    def helper(opened,closed,pattern):
        if len(pattern)==2*n:
            combinations.append(pattern)
            return
        if opened<n:
            helper(opened+1,closed,pattern+"(")
        if closed<opened:
            helper(opened,closed+1,pattern+")")

    helper(0,0,"")
    return combinations
