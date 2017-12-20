#https://www.hackerrank.com/challenges/30-2d-arrays/problem

def hourglass(matrix, n):
    result = -45 #Min value of an element is -9, so min sum of an hourglass is -45
    for i in range(n-2):
        for j in range(n-2):
            sum = int(matrix[i][j]) + int(matrix[i][j+1]) + int(matrix[i][j+2]) + int(matrix[i+1][j+1]) + int(matrix[i+2][j]) + int(matrix[i+2][j+1]) + int(matrix[i+2][j+2])
            if sum > result:
                result = sum
    return result

# matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
matrix = []
for i in range(6):
    a = input().strip().split(' ')
    matrix.append(a)
n = 6

print (hourglass(matrix, n))
