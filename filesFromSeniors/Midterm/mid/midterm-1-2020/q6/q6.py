gifts = list(map(int,input().split()))
Sum = sum(gifts)
half = Sum//2
mm = [[-1] * (half) for i in range(len(gifts))]

def split(i,v):
    if v == half:
        return v
    if v > half:
        if v-gifts[i-1] > half:
            return -float('inf')
        return v-gifts[i-1]
    if i == len(gifts):
        return -float('inf')
    if mm[i][v] != -1:
        return mm[i][v]
    mins = max(split(i+1,v+gifts[i]), split(i+1,v))
    mm[i][v] = mins
    return mins


first = split(0,0)
second = Sum - first
print(second-first)


