#Rotating a 2-D matrix clockwise

from copy import deepcopy

def rotate_matrix(matrix, n):
    result = deepcopy(matrix)
    for i in range(n):
        for j in range(n-1, -1, -1):
            result[i][n-j-1] = matrix[j][i]
    return result

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
n = 4

print (matrix)
print (rotate_matrix(matrix, n))
