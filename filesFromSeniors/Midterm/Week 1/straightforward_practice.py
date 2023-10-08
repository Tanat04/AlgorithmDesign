import time

def Sum(x, i, j):
    s = 0
    for k in range(i, j + 1):
        s += x[k]
    return s

start = time.process_time()

numList = list(map(int, input().split()))
maxValue = 0
for i in range(len(numList)-1):
    for j in range(i, len(numList)):
        if Sum(numList, i, j) > maxValue:
            maxValue = Sum(numList, i, j)


finish = time.process_time()
print("running time =", finish - start)

print(maxValue)
