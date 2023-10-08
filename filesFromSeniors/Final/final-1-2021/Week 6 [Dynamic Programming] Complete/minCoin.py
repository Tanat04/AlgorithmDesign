coins = list(map(int, input().split()))
v = int(input())
mm = [None] * (v+1)

def mincoin(v):
    global coins, mm
    if mm[v] == None:
        if v == 0:
            mm[v] = 0
        else:
            minc = 10000000
            for c in coins:
                if c <= v:
                    mc = 1 + mm[v-c]
                    minc = min(minc, mc)
            mm[v] = minc

for change in range(v+1):
    mincoin(change)
print(mm[change])
print(mm)