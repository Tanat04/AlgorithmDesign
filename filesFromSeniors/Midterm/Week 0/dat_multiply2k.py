import time
target = int(input())
numList = list(map(int, input().split()))
# part of the code to measure running time
DAT = [False for i in range((12999709*2)+1)]

start_time = time.process_time()
for a in numList:
    if target % a == 0:
        b = target//a
        if DAT[b + 12999710] == True:
            print(a,b)
            break
        DAT[a + 12999710] = True

end_time = time.process_time()
running_time = end_time - start_time
print(running_time)