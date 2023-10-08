M, N = list(map(int, input().split()))
cloud = []

for i in range(M):
    x = list(map(int, input().split()))
    cloud.append(x)

def valid(r, c):
    if r >= 0 and r <= M-1 and c >= 0 and c <= N-1:
        return True
    return False

def maxC(r, c):
    global cloud, M, N

    if not valid(r, c):
        return 0
    if cloud[r][c] == 0:
        return 0
    else:
        cloud[r][c] = 0
        return 1 + maxC(r, c-1) + maxC(r, c+1) + maxC(r-1, c) + maxC(r+1, c)

result = []
for i in range(M):
    for j in range(N):
        result.append(maxC(i,j))

print(max(result))
