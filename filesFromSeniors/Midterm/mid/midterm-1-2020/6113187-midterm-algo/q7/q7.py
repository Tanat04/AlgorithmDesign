import sys
sys.setrecursionlimit(10000)

seq = list(map(int,input().split()))
seq += [-1]
mm = [[-1] * (len(seq)+1) for i in range(len(seq)+1)]

def increase(i,p):
    if i == len(seq)-1:
        return 0
    if mm[i][p] != -1:
        return mm[i][p]
    a = increase(i+1,p)
    b = 0
    if seq[p] < seq[i]:
        b = increase(i+1, i) + 1
    maxs = max(a,b)
    mm[i][p] = maxs
    return maxs

print(increase(0,-1))
