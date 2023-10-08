coins = list(map(int, input().split()))
v = int(input())
mm = [None] * (v+1)

def mincoin(v):
    global coins, mm
    if mm[v] == None:
        if v == 0:
            mm[v] = 0
        else:
            minc = 100000000
            for c in coins:
                if c <= v:
                    mc = 1 + mm[v - c]
                    minc = min(minc, mc)
            mm[v] = minc
        return mm[v]
    else:
        return mm[v]
        
for change in range(v+1):
    mincoin(change)
print(mm)
print(mm[change])


# mm = [None] * (v+1)
# for i in range(v):
#     minc = [0] * 
#     if i == 0:
#         mm[i] = 0
#     else:
#         for c in range(len(coins)):
#             if coins[c] >= i:
#                 minc[i] += coins[c]
#         mm[i] = min(minc)

# print(mm)
