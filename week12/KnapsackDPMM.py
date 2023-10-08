import time
N, C = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))
MaximumValue = [[None for _ in range(C+1)] for _ in range(N+1)]
MaximumValue[N] = [0 for _ in range(C+1)]
count = 0


def maxVal(i, C):
    if MaximumValue[i][C] != None:
        return MaximumValue[i][C]

    notChoose = maxVal(i + 1, C)
    if w[i] <= C:
        Choose = v[i] + maxVal(i+1, C-w[i])
    else:
        Choose = -1

    MaximumValue[i][C] = max(Choose, notChoose)
    return MaximumValue[i][C]


def KnapsackDynamicProgramming():
    for i in range(N-1, -1, -1):
        for j in range(C+1):
            maxVal(i, j)


st = time.process_time()
KnapsackDynamicProgramming()
print(MaximumValue[0][C])
et = time.process_time()
print(f"Running Time: {et-st}")

'''Efficiency: The DP approach has a significantly better time complexity compared to the DFS approach. 
The DFS approach explores all possible combinations of items, which results in an exponential time complexity, 
making it impractical for larger instances of the problem. On the other hand, the DP approach has a time 
complexity of O(N*C), which is much more efficient.

Optimal Substructure: The DP approach takes advantage of the optimal substructure property of the Knapsack 
Problem. It breaks down the problem into smaller subproblems and uses the results of those subproblems to 
solve the larger problem efficiently. This property is leveraged by the DP approach and allows it to find 
the optimal solution without redundantly solving the same subproblems multiple times.'''
