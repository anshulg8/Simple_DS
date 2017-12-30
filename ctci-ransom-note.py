# https://www.hackerrank.com/challenges/ctci-ransom-note/problem
# Hash Tables: Ransom Note

# Instead of searching through the entire magazine word list again and again[O(MxN)],
# it's possible to hash each word in the magazine and store a count along with it(word_counts).
# Then, when you want to check if a word is in the magazine, you can check the hash in O(1)
# time for a result of O(N) to construct the hash and O(M) to check all m words, which is a final O(N+M).

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
