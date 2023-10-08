import sys


def maxRevenue(length):
    # Base case: if the amount is 0, no coins are needed
    if length == 0:
        return 0

    # Initialize the minimum number of coins required to a large value
    revenue = -9999999

    # Try using each coin denomination
    for i in range(1, length+1):
        max_rev = prices[i-1] + maxRevenue(length-i)
        revenue = max(max_rev, revenue)
    return revenue


# Read the input
prices = list(map(int, input().split()))
length = len(prices)
# print(prices, length)
# Call the mincoin function and print the result
maxRev = maxRevenue(length)
print(maxRev)
