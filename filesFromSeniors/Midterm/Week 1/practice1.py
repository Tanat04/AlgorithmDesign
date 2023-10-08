import time

# Straightforward Solution

# def Sum(x, i, j):
#     s = 0
#     for k in range(i, j + 1):
#         s += x[k]
#     return s

# Accumulation Technique

def Sum(x, i, j):
    if i == 0:
        return x[i]
    else:
        return x[i] - x[j]

numList = list(map(int, input().split()))
for l in range(1, len(numList)):
    numList[l] = numList[l] + numList[l-1]

start = time.process_time()

maxValue = 0
for i in range(len(numList)-1):
    for j in range(i):
        if Sum(numList, i, j) > maxValue:
            maxValue = Sum(numList, i, j)


finish = time.process_time()
print("running time =", finish - start)

print(maxValue)