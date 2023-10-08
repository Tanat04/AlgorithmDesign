import sys
sys.setrecursionlimit(10001)

c = input().split()
for i in range(len(c)):
    c[i] = int(c[i])

V = int(input())
call = [0] * (V + 1)
mm = [None] * (V + 1)


def mincoin(v):
    global call, mm, c

    if mm[v] == None:
        call[v] += 1

        if v == 0:
            mm[v] = 0
        else:
            minc = float('inf')
            for x in c:
                if x <= v:
                    minc = min(minc, 1 + mincoin(v-x))
            mm[v] = minc

    return mm[v]


for i in range(V+1):
    x = mincoin(i)
print(mm[V])
# print(call)
# print(mm)
