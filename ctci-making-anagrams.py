# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
#Strings: Making Anagrams

from collections import Counter

def number_needed(a, b):
    counter_a = Counter(a)
    counter_b = Counter(b)
    res = 0
    for k,v in ((counter_a-counter_b)+(counter_b-counter_a)).items():
        res += v
    return res

a = input().strip()
b = input().strip()

print (number_needed(a, b))
