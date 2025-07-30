def solve(board):
        """
        Do not return anything, modify board in-place instead.
        """
        
        m=len(board)
        n=len(board[0])
        def helper(row,column):
            if 0<=row<m and 0<=column<n and board[row][column]=='O':
                board[row][column]='S'
                helper(row-1,column)
                helper(row+1,column)
                helper(row,column+1)
                helper(row,column-1)
            else: return

        for i in range(m):
            helper(i,0)
            helper(i,n-1)

        for j in range(1,n-1):
            helper(0,j)
            helper(m-1,j)
        
        for row in range(m):
            for column in range(n):
                if board[row][column]=='S': board[row][column]='O'
                elif  board[row][column]=='O':board[row][column]='X'
