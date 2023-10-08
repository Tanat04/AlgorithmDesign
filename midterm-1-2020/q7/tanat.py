import time
data = list(map(int, input().split()))
n = len(data)
memo = [None for _ in range(n)]


def LongestIncreasingSubsequence(i):
    if i == 0:
        return 1

    if memo[i] != None:
        return memo[i]

    maxSeq = 1
    for j in range(i):
        if data[i] > data[j]:
            maxSeq = max(maxSeq, 1 + LongestIncreasingSubsequence(j))

    memo[i] = maxSeq
    return maxSeq


# Dynamic Programming
max_val = 0
for i in range(n):
    max_val = max(max_val, LongestIncreasingSubsequence(i))
print(max_val)

# #Heres how its works
# import time
# data = list(map(int, input().split()))
# n = len(data)
# memo = [None for _ in range(n)]


# def LongestIncreasingSubsequence(i):
#     if i == 0:
#         return [data[0]]

#     if memo[i] is not None:
#         return memo[i]

#     maxSeq = [data[i]]
#     for j in range(i):
#         if data[i] > data[j]:
#             seq = LongestIncreasingSubsequence(j) + [data[i]]
#             if len(seq) > len(maxSeq):
#                 maxSeq = seq

#     memo[i] = maxSeq
#     return maxSeq


# # Dynamic Programming
# max_seq = []
# for i in range(n):
#     seq = LongestIncreasingSubsequence(i)
#     if len(seq) > len(max_seq):
#         max_seq = seq

# print("Longest Increasing Subsequence:", max_seq)
