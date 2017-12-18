#Rotating a 2-D matrix clockwise

from copy import deepcopy

def rotate_matrix(matrix, n):
    result = deepcopy(matrix)
    for i in range(n):
        for j in range(n-1, -1, -1):
            result[i][j] = matrix[2-j][i]
    return result


matrix = [[1,2,3],[4,5,6],[7,8,9]]
n = 3

# result[0][2] == 1 == matrix[0][0]
# result[0][1] == 4 == matrix[1][0]
# result[0][0] == 7 == matrix[2][0]
# result[1][2] == 2 == matrix[0][1]
# result[1][1] == 5 == matrix[1][1]
# result[1][0] == 8 == matrix[2][1]
# result[2][2] == 3 == matrix[0][2]
# result[2][1] == 5 == matrix[1][2]
# result[2][0] == 9 == matrix[2][2]
# result[i][j] = matrix[2-j][i]

print (matrix)
print (rotate_matrix(matrix, n))
