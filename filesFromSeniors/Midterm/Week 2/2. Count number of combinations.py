import sys
sys.setrecursionlimit(10000)

n = int(input())
k = int(input())
x = [None] * n
s = 0
count = 0

def comb(i):
    global x,s,k,count
    if i == n:
        print(x)
        if x.count(1) == k:
            count += 1
        return 1
    else:
        x[i] = 0
        s = comb(i+1)
        x[i] = 1
        s += comb(i+1)
        x[i] = 2
        s += comb(i+1)
        return s
comb(0)

print(s)
print(count)
