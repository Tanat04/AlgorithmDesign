import time
k = int(input())
numList = list(map(int, input().split()))

start_time = time.process_time()
# part of the code to measure running time
for i in range(len(numList)):
    for j in range(i+1, len(numList)):
        if numList[i] * numList[j] == k:
            print(numList[i], numList[j])
            break
end_time = time.process_time()
running_time = end_time - start_time
print(running_time)