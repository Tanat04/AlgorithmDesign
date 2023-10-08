N, M = list(map(int, input().split()))
weights = list(map(int, input().split()))
values = list(map(int, input().split()))

memo = [[-1] * (M+1) for i in range(N+1)]

def knapsack(i, c):
    global memo

    if memo[i][c] == -1:
        if i == N:
            memo[i][c] = 0
        else:
            skip = knapsack(i+1, c)
            if c - weights[i] >= 0:
                take = value[i] + knapsack(i+1, c - weights[i])
            else:
                take = -1
            memo[i][c] = max(skip,take)
    return memo[i][c]

print(knapsack(0,M))
