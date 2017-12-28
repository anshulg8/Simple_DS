# https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem
# Davis' Staircase probelm using recursion and dp

def step_count_recursive(n):
   if n <= 1:
       return n
   elif n == 2:
       return 2
   elif n == 3:
       return 4
   else:
       return(step_count_recursive(n-1) + step_count_recursive(n-2) + step_count_recursive(n-3))

def step_count_dp(n):
    if n <= 2:
        return n
    elif n == 3:
        return 4
    else:
        a,b,c = 1,2,4
        for i in range(4,n+1):
            d = a+b+c
            a = b
            b = c
            c = d
        return d

n = int(input())
for i in range(n):
    s = int(input())
    print (step_count_dp(s))
