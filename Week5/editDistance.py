import sys
sys.setrecursionlimit(10000)

a = input()
b = input()

memo = [[-1] * (len(b)+1) for i in range(len(a)+1)]
# for i in range(len(a)+1):
#     for j in range(len(b)+1):
#         print(memo[i][j], end=" ")
#     print()


def editDistance(i, j):
    global memo
    # print(i, j)
    # print(memo[i][j])
    if memo[i][j] == -1:

        if i == len(a) or j == len(b):
            return len(a) - i + len(b) - j

        if a[i] == b[j]:
            return editDistance(i + 1, j + 1)
        memo[i][j] = 1 + min(
            editDistance(i, j+1),
            editDistance(i+1, j),
            editDistance(i+1, j+1)
        )
    return memo[i][j]


print(editDistance(0, 0))
