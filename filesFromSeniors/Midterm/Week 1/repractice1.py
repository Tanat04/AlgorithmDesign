import time


#Function Sum for Accumulated technique
# def Sum(x, i, j):
#     if i == 0:
#         return x[i]
#     else:
#         return x[i] - x[j]


numList = list(map(int, input().split()))

start = time.process_time()

maxValue = 0

#Straightforward solution
# for i in range(len(numList)):
#     for j in range(i, len(numList)):
#         if Sum(numList, i, j) > maxValue:
#             maxValue = Sum(numList, i, j)


#Accumulation technique
# for e in range(1, len(numList)):
#     numList[e] = numList[e] + numList[e-1]

# for i in range(len(numList)-1):
#     for j in range(0, i):
#         if Sum(numList, i, j) > maxValue:
#             maxValue = Sum(numList, i, j)


#Kadane's Algorithm
currentValue = 0
if numList[0] > maxValue:
    maxValue = numList[0]
else:
    maxValue = 0
for i in range(1, len(numList)):
    currentValue = max(numList[i], numList[i] + currentValue)
    if currentValue > maxValue:
        maxValue = currentValue
    

print(maxValue)

finish = time.process_time()
print("running time =", finish-start)