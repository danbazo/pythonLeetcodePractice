def exist(board, word):
      
      directions=[(0,1),(0,-1),(1,0),(-1,0)]
      n=len(board)
      m=len(board[0])
      def helper(row,column,wordPoss):
          
          if board[row][column]==word[wordPoss]:
              if wordPoss==len(word)-1: return True
              board[row][column]='#'
              for direction in directions:
                  newRow=row+direction[0]
                  newColumn=column+direction[1]
                  if 0<=newRow<n and 0<=newColumn<m:
                      if helper(newRow,newColumn,wordPoss+1): return True
              board[row][column]=word[wordPoss]
          return False
      for i in range(n):
          for j in range(m):
              if helper(i,j,0): return True
      return False
