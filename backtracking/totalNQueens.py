def totalNQueens(n):
      columns=set()
      upDiag=set()
      downDiag=set()

      def helper(row):
          if row==n:
              return 1
          queenCount=0
          for column in range(n):
              if column not in columns and row+column not in upDiag and row-column not in downDiag:
                  columns.add(column)
                  upDiag.add(row+column)
                  downDiag.add(row-column)
                  queenCount+=helper(row+1)
                  columns.remove(column)
                  upDiag.remove(row+column)
                  downDiag.remove(row-column)
          return queenCount

      return helper(0)
