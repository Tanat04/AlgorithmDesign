import time

def Sum(x, i, j):
    s = 0
    for k in range(i, j+1):
        s += x[k]
    return s

n = list(map(int, input().split()))
start_time = time.process_time()

max_value = -99999

for i in range(len(n)-1):
    for j in range(i, len(n)):
        if Sum(n, i, j) > max_value:
            max_value = Sum(n, i, j)

end_time = time.process_time()
running_time = end_time - start_time
print(max_value)
print(running_time)
