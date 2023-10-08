coins = list(map(int, input().split()))
v = int(input())
count = 0

def mincoin(v):
    global coins, count
    count += 1
    if v == 0:
        return 0
    else:
        minc = 1000000
        for c in coins:
            if c <= v:
                mc = 1 + mincoin(v - c)
                minc = min(minc, mc)
        return minc
                
print(mincoin(v))
print(count)