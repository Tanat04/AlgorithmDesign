import sys
sys.setrecursionlimit(10000)

# Given test case
C = int(input())
k = int(input())
sacks = []
for _ in range(k):
    sacks.append(tuple(map(int, input().split())))
MaximumValue = [[None for _ in range(C+1)] for _ in range(k+1)]


def maxVal(i, C):
    if i >= len(sacks) or C == 0:
        return 0

    if MaximumValue[i][C] != None:
        return MaximumValue[i][C]

    notChoose = maxVal(i + 1, C)
    Choose = 0
    for weight, price in sacks:
        if weight <= C:
            TempChoose = price + maxVal(i, C-weight)
            if TempChoose > Choose:
                Choose = TempChoose

    MaximumValue[i][C] = max(Choose, notChoose)
    return MaximumValue[i][C]


for i in range(k+1, -1, -1):
    for c in range(C+1):
        maxVal(i, c)
print(MaximumValue[0][C])
