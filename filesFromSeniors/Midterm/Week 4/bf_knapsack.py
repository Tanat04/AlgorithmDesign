import sys
sys.setrecursionlimit(10000)
N, M = list(map(int, input().split()))
weights = list(map(int, input().split()))
values = list(map(int, input().split()))

x = [None] * N
v = []
def comb(i):
    global x
    global v
    if i == N:
        sv = sw = 0
        for j in range(N):
            sw += x[j]*weights[j]
            sv += x[j]*values[j]
        if sw <= M:
            return sv
        else:
            return -1
    else:
        x[i] = 0
        skip = comb(i+1)
        x[i] = 1
        take = comb(i+1)
        return max(skip, take)
print(comb(0))
