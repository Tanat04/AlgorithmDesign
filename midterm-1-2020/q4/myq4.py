n = int(input())
nList = [None] * (n+1)

def fibo_recur(n):
    for i in range(n+1):
        if i == 0 or i == 1:
            nList[i] = i + 1
        else:
            nList[i] = nList[i-1] + nList[i-2]
    return nList[-1]

print(fibo_recur(n))