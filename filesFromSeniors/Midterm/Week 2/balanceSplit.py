import time

numList = list(map(int, input().split()))
n = len(numList)
x = [None] * n
sumList = []
leastValue = 100000


def comb(i):
    global x
    if i == n:
        sumList.append(sum(x))
    else:
        x[i] =  0
        comb(i+1)
        x[i] = numList[i]
        comb(i+1)
    
start = time.process_time()

comb(0)

for j in range(0, len(sumList)//2):
    result = abs(sumList[j] - sumList[-j-1])
    if result > 0 and result < leastValue:
        leastValue = result

finish = time.process_time()
print("running time =", finish - start)
print(leastValue)