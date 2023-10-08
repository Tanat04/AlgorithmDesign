import sys
sys.setrecursionlimit(10000)

x = list(map(int, input().split()))
num_items = x[0]
max_cap = x[1]
weight = list(map(int, input().split()))
value = list(map(int, input().split()))

count = 0

def knapsack(i, c):
    global count
    count+=1

    if i == num_items:
        return 0
    else:
        skip = knapsack(i+1, c)
        if c - weight[i] >= 0:
            take = value[i] + knapsack(i+1, c- weight[i])
        else:
            take = -1
        return max(skip,take)

print(knapsack(0,max_cap))
print(count)