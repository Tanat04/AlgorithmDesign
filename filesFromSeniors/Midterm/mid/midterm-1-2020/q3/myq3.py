tiles = list(map(int, input().split()))
l = int(input())
lst= [None] * (l+1)

def minTiles(l):
    global lst
    if lst[l] == None:
        if l == 0:
            lst[l] = 0
        else:
            mint = 1000000
            for t in tiles:
                if t <= l:
                    mt = 1 + minTiles(l - t)
                    mint = min(mint, mt)
            lst[l] = mint
        return lst[l]
    else:
        return lst[l]

print(minTiles(l))