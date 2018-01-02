# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem#

#!/bin/python3

import sys

def solve(arr, count):
    comp = {}
    for idx, val in enumerate(arr):
        if count - val in comp:
            print ("{} {}".format(comp[count-val]+1, idx+1))
        else:
            comp[val] = idx

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        money = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        solve(arr, money)
