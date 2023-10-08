class obj:
    def __init__(self, w, v):
        self.w = w
        self.v = v
        self.r = v/w


x = input().split()
N = int(x[0])
M = int(x[1])
w = input().split()
v = input().split()
item = []
for i in range(N):
    item.append(obj(int(w[i]), int(v[i])))

maxV = 0
count = 0


def dfs(i, sumW, sumV):
    global maxV, item, N, M, count

    count += 1
    if i == N:
        # This part consider even if it exceeds capacity
        maxV = max(maxV, sumV)  # update maxV
    else:

        dfs(i+1, sumW, sumV)  # not take item[i]
        if sumW + item[i].w <= M:
            dfs(i+1, sumW+item[i].w, sumV+item[i].v)  # take item[i]


dfs(0, 0, 0)
print(maxV)
print(count)


'''This code uses a depth-first search (DFS) approach, which explores all possible 
combinations of items. While it guarantees correctness, it can be significantly slower 
than the DP approach for large input sizes because it has an exponential time complexity.

The normal DP solution uses a table to store intermediate results and calculates the
maximum value iteratively in a bottom-up manner. It has a time complexity of O(N*M),
 which is much more efficient for larger instances of the problem.

This code with DFS can be useful for educational purposes or when the input size is 
relatively small. However, for practical applications with larger datasets, the DP 
approach is preferred due to its efficiency.'''
