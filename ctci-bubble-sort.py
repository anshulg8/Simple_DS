# Sorting: Bubble Sort
# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

count = 0
for i in range(len(a)):
    for j in range(len(a)-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            count += 1

print ("Array is sorted in {} swaps.".format(count))
print ("First Element: {}".format(a[0]))
print ("Last Element: {}".format(a[-1]))
