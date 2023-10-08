import sys
sys.setrecursionlimit(10000)
# N = no. of item | M = max weight
N, M = map(int, input().split())
wList = list(map(int, input().split()))
vList = list(map(int, input().split()))

mm = [[-1]*(M+1) for i in range(N+1)]

def maxVal(i,C):
    if mm[i][C] == -1:
        # if the knapsack is has N items or it reaches maximum weight
        if i == N or C == 0:
            mm[i][C] = 0
        else:
            #skip = last item with same weight
            skip = mm[i+1][C]
            take = 0
            if wList[i] <= C:
                take = vList[i] + mm[i+1][C-wList[i]]
            mm[i][C] = max(skip,take)
    return mm[i][C]

for i in range(N,-1,-1):
    for C in range(M+1):
        maxVal(i, C)
print(mm[0][M])
print(mm)