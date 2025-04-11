def rotate(matrix):
        """
        Rotates in place a given matrix by 90 degress clockwise

        keyword arguments
        matrix a list of list of size n x n
        """
        #use the variable n as the lenth of te matrix
        n=len(matrix)

        #iterate the layers of the matrix, from the outside to the inside. it will be n//2 layers
        for j in range(n//2):
            #in each layer, rotate at a time the 4 symetrical elements between them
            for i in range(n-2*j-1):
                matrix[j][i+j],matrix[i+j][n-1-j],matrix[n-1-j][n-1-i-j],matrix[n-1-i-j][j]=\
                matrix[n-1-i-j][j],matrix[j][i+j],matrix[i+j][n-1-j],matrix[n-1-j][n-1-i-j]
