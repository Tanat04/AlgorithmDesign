import time

k = int(input())
lt = list(map(int, input().split()))
val = []

start_time = time.process_time()
for i in range(0, len(lt)):
    for j in range(i + 1, len(lt)):
        if lt[i] * lt[j] == k:
            val.append(lt[j])
            val.append(lt[i])
            break

end_time = time.process_time()
running_time = end_time - start_time

print(val)
if len(val) > 0:
    print(k, val[1] * val[0])

print("Running time: ", running_time)
