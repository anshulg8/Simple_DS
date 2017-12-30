# https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem
def isBalanced(exp):
    pair = {")":"(","}":"{","]":"["}
    s = []
    if exp.count('(') != exp.count(')'):
        return False
    elif exp.count('{') != exp.count('}'):
        return False
    elif exp.count('[') != exp.count(']'):
        return False

    for i in range(len(exp)):
        if exp[i] in ['(','{','[']:
            s.append(exp[i])
        elif exp[i] in [')','}',']']:
            if len(s)==0:
                return False
            if pair[exp[i]] != s.pop():
                return False

    if len(s) != 0:
        return False

    return True

def main():
    N = int(raw_input())
    for _ in xrange(N):
        s = raw_input()
        if isBalanced(s):
            print "YES"
        else:
            print "NO"

if __name__ == '__main__':
    main()
