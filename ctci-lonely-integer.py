# Bit Manipulation: Lonely Integer
# https://www.hackerrank.com/challenges/ctci-lonely-integer/problem

#!/bin/python3

import sys
from collections import Counter

# Using hashmap
def lonely_integer_a(a):
    for k, v in Counter(a).items():
        if v == 1:
            return k

# Using Arithmetic
def lonely_integer_b(a):
    return sum(list(set(a)))*2 - sum(a)

# Using Bit Manipulation
def lonely_integer_c(a):
    result = 0
    for i in a:
        result = result ^ i
    return result

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer_a(a))
print(lonely_integer_b(a))
print(lonely_integer_c(a))
