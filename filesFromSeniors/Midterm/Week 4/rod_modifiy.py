prices = list(map(int, input().split()))
lengthOfRod = len(prices)
# calls = [0] * (lengthOfRod + 1)
count = 0
lst = [-10] * (lengthOfRod + 1)

def maxRev(l):
    global prices, count, calls, lst
    maxR = -10
    if lst[l] > 0:
        return lst[l]
    elif l == 0:
        maxR = 0
    else:
        for i in range(1, l+1):
            mr = prices[i-1] + maxRev(l-i)
            maxR = max(mr,maxR)
            # count += 1
        # calls[l] += 1
        lst[l] = maxR
    return maxR

print(maxRev(lengthOfRod))
# print(calls)
# print(count)