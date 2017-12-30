# https://www.hackerrank.com/challenges/ctci-ransom-note/problem
# Hash Tables: Ransom Note

from collections import Counter

def ransom_note(magazine, ransom):
    word_counts = Counter(magazine)
    for word in ransom:
        if word_counts[word] > 0:
            word_counts[word] -= 1
        else:
            return False
    return True

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
