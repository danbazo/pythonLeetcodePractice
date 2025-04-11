def spiralOrder(matrix):
        """
        returns a list the values inside matrix in spiral order, going clockwise

        Keyword arguments:
        matrix a list of lists of integers, all list are the same size, creating a m x n matrix
        
        """
  #Initialize the answer list
        solution=[]
  #define a helper function. This funtions goes all arround the matrix in clockwise order, adding items to solution, and removing them from matrix, leaving an smaller one in the end
        def helper(matrix,solution):
            for element in matrix[0]:
                solution.append(element)

            del matrix[0]
            for i in range(len(matrix)):
                if matrix[i]:
                    solution.append(matrix[i].pop())
                
            if matrix:
                for element in reversed(matrix[-1]):
                    solution.append(element)
                del matrix[-1]

            for j in reversed(range(len(matrix))):
                if matrix[j]:
                    solution.append(matrix[j].pop(0))
                else:
                    del matrix[j]
    #run the helper function on matrix until we remove all items from it            
        while matrix:
            helper(matrix,solution)
        
        return solution
