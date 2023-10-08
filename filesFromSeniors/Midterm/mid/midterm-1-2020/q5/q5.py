import sys
sys.setrecursionlimit(10000)

weight = int(input())
n = int(input())
sizes = [0] * n
prices = [0] * n
mm = [-1] * (weight+1)

for i in range(n):
    x = list(map(int,input().split()))
    sizes[i] = x[0]
    prices[i] = x[1]

s = 0
maxs = 0
for w in range(weight+1):
    if w == 0:
        mm[w] = 0
    else:
        for i in range(len(sizes)):
            if w-sizes[i] >= 0:
                s = mm[w-sizes[i]] + prices[i]
                maxs = max(maxs,s)
        mm[w] = maxs

print(mm)
