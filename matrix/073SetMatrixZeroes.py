def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    modifies a given matrix in place, so each row and column where a zero is originally found, will turn to zeroes as well

     Keyword arguments:
    matrix, a list of lists of m x n size
    """
    #Initialize the zeroes list, with two empty sets, one for the rows and one for the columns found to have zeroes
    zeroes=[set(),set()]
    #iterate once over the whole matrix, and save the row and column of the zeroes found in the variable zeroes
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0: 
                zeroes[0].add(i)
                zeroes[1].add(j)
    #iterate a second time over the matrix, replacing the its values with zero if they match the row or column values un the variable zeroes
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in zeroes[0] or j in zeroes[1]:
                matrix[i][j]=0
