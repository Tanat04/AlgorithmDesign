prices = list(map(int, input().split()))
lengthOfRod = len(prices)
count = 0

def maxRev(l):
    global count
    global calls
    if l == 0:
        return 0
    else:
        calls[l] += 1
        maxR = 0
        for i in range(1, l+1):
            mr = prices[i-1] + maxRev(l-i)
            maxR = max(mr,maxR)
            count += 1
        return maxR

print(maxRev(lengthOfRod))
print(count)