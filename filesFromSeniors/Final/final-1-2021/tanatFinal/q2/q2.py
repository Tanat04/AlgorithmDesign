import time
import sys
sys.setrecursionlimit(10000)

n = int(input())
M = []
for i in range(n):
    x = list(map(int, input().split()))
    x = [a if a >= 0 else 1000000 for a in x]
    M.append(x)


def minM(i, j, k):
    if i >= 0 and j >= 0 and k >= 0:
        if j > 0:
            minM(i, j-1, k)
        if i > 0:
            minM(i-1, j, k)
        if k > 0:
            minM(i, j, k-1)
        x = M[i][k] + M[k][j]
        M[i][j] = min(M[i][j], x)


st = time.process_time()
for k in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        for i in range(n-1, -1, -1):
            M[i][j] = min(M[i][j], M[i][k] + M[k][j])
# minM(n-1,n-1,n-1)
et = time.process_time()
print(et-st)

for i in range(n):
    for j in range(n-1):
        print(M[i][j], end=' ')
    print(M[i][n-1])
