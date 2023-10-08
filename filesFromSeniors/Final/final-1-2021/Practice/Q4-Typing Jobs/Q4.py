N, P, E = map(int, input().split())
l = []
for i in range(2):
    l.append(list(map(int, input().split())))
l[0].sort()
l[1].sort(reverse=True)
total = 0
for i in range(N):
    result = l[0][i] + l[1][i]
    if result > P:
        extra = (result - P) * E
        total += extra
print(total)