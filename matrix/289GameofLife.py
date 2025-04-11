def gameOfLife(board):
        """
        Modifies the input board in-place to compute the next state of the Game of Life.

        Keyword arguments:
        board a list of lists composed of 1s or 0s
        """
        m=len(board)
        n=len(board[0])
        
        for i in range(m):
            for j in range(n):
                alive=0
                # Check all 8 neighbors using a 3x3 grid
                for k in range(9):
                    row=i+k//3-1
                    collumn=j+k%3-1
                    if k!=4 and m>row>=0 and n>collumn>=0:
                      # Consider cells marked 1 (alive) and 2 (alive -> dead) as alive
                        if board[row][collumn]>0: alive+=1
                # Apply rules using temporary markers
                if board[i][j]==1:
                    if not (alive==2 or alive==3): board[i][j]=2 #Is alive but will die
                else:
                    if alive==3: board[i][j]=-1 #Is dead but will revive
        #update in-place temporary values to its final state
        for i in range(m):
            for j in range(n):
                if board[i][j]==-1: board[i][j]=1
                elif board[i][j]==2: board[i][j]=0
