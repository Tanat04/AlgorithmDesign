N, M = map(int, input().split(' '))
w = list(map(int, input().split()))
v = list(map(int, input().split()))

# Create a memoization table initialized with -1
memo = [[-1 for _ in range(M+1)] for _ in range(N+1)]
print(memo)


def maxVal(i, C):
    # Check if the result for the current index and remaining capacity is already computed
    if memo[i][C] != -1:
        return memo[i][C]

    if i == N:
        return 0
    else:
        skip = maxVal(i + 1, C)
        if w[i] <= C:
            take = v[i] + maxVal(i + 1, C - w[i])
        else:
            take = -1

        # Store the computed result in memoization table
        memo[i][C] = max(skip, take)

    return memo[i][C]


print(maxVal(0, M))
