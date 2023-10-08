import time

def Sum(x, i, j):
    s = 0
    if i == 0:
        s = x[i]
    else:
        s = x[i] - x[j]
    return s

nList = list(map(int, input().split()))
start_time = time.process_time()

max_sum = -99999
current_sum = 0

for i in range(len(nList)):
    current_sum = max(current_sum + nList[i], 0)
    if current_sum > max_sum:
        max_sum = current_sum


end_time = time.process_time()
running_time = end_time - start_time
print(max_sum)
print(running_time)
