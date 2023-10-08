W = int(input())
k = int(input())

sack_size = [] * k
prices = [] * k

for i in range(k):
    s, p = list(map(int, input().split()))
    sack_size.append(s)
    prices.append(p)

memo = [-1] * (W+1)
maxs = 0
s = 0

for w in range(W+1):
    if w == 0:
        memo[w] = 0
    else:
        for i in range(len(sack_size)):
            if w - sack_size[i] >= 0:
                s = memo[w-sack_size[i]] + prices[i]
                maxs = max(s, maxs)
        memo[w] = maxs

print(memo[-1])
