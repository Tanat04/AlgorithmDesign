import sys
sys.setrecursionlimit(10000)

n = int(input())

x = [None] * n

def comb(i):
    global x
    if i == n:
        print(x)
    else:
        x[i] = 0
        comb(i+1)
        x[i] = 1
        comb(i+1)
comb(0)
