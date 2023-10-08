import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
wList = []
vList = []
for i in range(N):
    v, w = list(map(int, input().split()))
    wList.append(w)
    vList.append(v)

mm = [[-1]*(M+1) for i in range(N+1)]

def maxVal(i,C):
    if mm[i][C] == -1:
        if i == N or C == 0:
            mm[i][C] = 0
        else:
            skip = mm[i+1][C]   # skip item i
            take = 0
            if wList[i] <= C:
                take = vList[i] + mm[i+1][C-wList[i]]  # take item i
            mm[i][C] = max(skip,take)
    return mm[i][C]

for i in range(N,-1,-1):
    for C in range(M+1):
        maxVal(i, C)
print(mm[0][M])