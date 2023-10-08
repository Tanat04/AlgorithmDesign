def Sum(x, i, j):
    s = 0
    for k in range(i, j+1):
        s += x[k]
    return s

import time
start = time.process_time()

numList = list(map(int, input().split()))
total = 0
for i in range(1, len(numList)):
    result = numList[i-1] + numList[i]
    numList[i] = result

for i in range(len(numList)):
    for j in range(i, len(numList)):
        sumAll = Sum(numList, i, j)
        if sumAll > total:
            total = sumAll
        
print(total)

finish = time.process_time()
print("running time =", finish-start)
