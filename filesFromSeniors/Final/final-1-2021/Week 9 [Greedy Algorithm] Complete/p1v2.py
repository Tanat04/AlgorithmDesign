n = int(input())
a = []
for i in range(n):
    a.append(tuple(map(int, input().split())))


def getkey(x):
    return x[1]

a.sort(key=getkey)

count = 0
busy = -1
for act in a:
    if act[0] > busy:
        count += 1
        busy = act[1]
        print(busy)

print(count)
