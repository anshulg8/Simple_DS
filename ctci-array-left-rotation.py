# Solution to Arrays: Left Rotation
# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

def array_left_rotation(a, n, k):
    k %= n
    return a[k:] + a[:k]

n, k = map(int, input().strip().split(' '))
a = map(int, input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print (' '.join(map(str,answer)))
