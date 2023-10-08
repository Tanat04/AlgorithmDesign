tiles = list(map(int,input().split()))
length = int(input())
mm = [-1] * (length+1)

def cover(l):
    if l == 0:
        return 0
    if mm[l] != -1:
        return mm[l]
    s = 0
    mins = float('inf')
    for i in range(len(tiles)):
        if l-tiles[i] >= 0:
            s = cover(l-tiles[i]) + 1
            mins = min(mins,s)
    mm[l] = mins
    return mins


print(cover(length))
