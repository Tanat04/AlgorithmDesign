n = int(input())
nums = list(map(int, input().split()))

one = 0
cumSum = 0
flip = 0

for i in range(n):
    if nums[i] == 1:
        one += 1
for i in range(n):

    if nums[i] == 0:
        cumSum += 1
    else:
        cumSum -= 1

    flip = max(flip, cumSum)

    if cumSum < 0:
        cumSum = 0
if one == n:
    print(n - 1)
else:
    print(one + flip)
