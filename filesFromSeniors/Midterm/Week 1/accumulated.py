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

max_value = -99999

for i in range(1, len(nList)):
    nList[i] = nList[i] + nList[i-1]

for i in range(len(nList)-1, -1, -1):
    for j in range(0, i):
        if Sum(nList, i, j) > max_value:
            max_value = Sum(nList, i, j)

end_time = time.process_time()
running_time = end_time - start_time
print(max_value)
print(running_time)
