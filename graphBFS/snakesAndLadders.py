def snakesAndLadders(self, board: List[List[int]]) -> int:
        n=len(board)
        totalPoss=n**2
        current=[1]
        jumps=0
        visited=set()
        def coordinates(poss,n):
            k=(poss-1)//n
            r=(poss-1)%n
            row=n-1-k
            column=r if k%2==0 else n-1-r
            
            return (row,column)

        while current:
            newCurrent=[]
            jumps+=1
            for cell in current:
                if cell in visited: continue
                visited.add(cell)
                if cell>=totalPoss-6: return jumps
                for nextCell in range(cell+1,cell+7):
                    row,column=coordinates(nextCell,n)
                    if board[row][column]==-1:
                        newCurrent.append(nextCell)
                    else:
                        nextJump=board[row][column]
                        if nextJump==totalPoss: return jumps
                        newCurrent.append(nextJump)
            current=newCurrent
            

        return -1
