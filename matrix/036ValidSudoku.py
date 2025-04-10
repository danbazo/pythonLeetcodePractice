def isValidSudoku(board):
      """
        returns a boolean indicating if a partially filled sudoku board is valid or not (Meaning there are no repeating number in its columns, rows or boxes)

        Keyword arguments:
        board a list of lists of strings
        
        """
        #iterate simultaneously over columns, rows and boxes, adding found numbers to a set. If a number is repeated, the Sudoku is not valid
        for i in range(9):
            currentRow=set()
            currentColumn=set()
            CurrentBox=set()
            for j in range(9):
              #iteration over the Rows
                if board[i][j].isnumeric():
                    if board[i][j] in currentRow:
                        
                        return False
                    else: currentRow.add(board[i][j])
              #iteration over the Columns
                if board[j][i].isnumeric():
                    if board[j][i] in currentColumn:
                        
                        return False
                    else: currentColumn.add(board[j][i])
              #iteration over the boxes
                if board[j//3+3*(i//3)][j%3+3*(i%3)].isnumeric():
                    if board[j//3+3*(i//3)][j%3+3*(i%3)] in CurrentBox:
                        
                        return False
                    else: CurrentBox.add(board[j//3+3*(i//3)][j%3+3*(i%3)])
        return True
