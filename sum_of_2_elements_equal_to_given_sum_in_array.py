# Given an array A[] and a number x, check for pair in A[] with sum as x

# Requires list to be sorted
def abc(arr, count):
    i = 0
    j = len(arr)-1
    while(i<j):
        s = int(arr[i]) + int(arr[j])
        if s == count:
            return True
        elif s < count:
            i += 1
        elif s > count:
            j -= 1
    return False

# Doesn't require list to be sorted
def abcd(arr, count):
    comp = []
    for i in range(len(arr)-1):
        if arr[i] in comp:
            return True
        else:
            comp.append(count - arr[i])
    return False

array = list(map(int, input().strip().split()))
result = int(input())

print (abc(array, result))
print (abcd(array, result))
