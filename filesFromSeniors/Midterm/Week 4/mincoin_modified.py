coins = list(map(int, input().split()))
v = int(input())
count = 0
lst= [None] * (v+1)

def mincoin(v):
    global coins, count, lst
    count += 1
    if lst[v] == None:
        if v == 0:
            lst[v] = 0
        else:
            minc = 1000000
            for c in coins:
                if c <= v:
                    mc = 1 + mincoin(v - c)
                    minc = min(minc, mc)
            lst[v] = minc
        return lst[v]
    else:
        return lst[v]
    
print(mincoin(v))
print(count)