def Sum(x, i, j):
    s = 0
    for k in range(i, j+1):
        s += x[k]
    return s


numList = list(map(int, input().split()))
print(numList)
Sum(numList, len(numList), len(numList)-1)