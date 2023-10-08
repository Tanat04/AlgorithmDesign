def mincoin(coins, amount):
    # Base case: if the amount is 0, no coins are needed
    if amount <= 0:
        return 0

    # Initialize the minimum number of coins required to a large value
    min_coins = float('inf')

    # Try using each coin denomination
    # print('Full coin list', coins, '\n\n')
    for coin in coins:
        # If the current coin is less than or equal to the amount, recursively calculate the minimum number of coins for the remaining amount
        # print('coin and amount: ', coin, amount)
        if amount >= coin:
            # print(coins, amount-coin)
            num_coins = mincoin(coins, amount - coin)
            # Update the minimum number of coins if necessary
            min_coins = min(min_coins, num_coins + 1)
            # print('mincoins:', min_coins)

    return min_coins


# Read the input
coins = list(map(int, input().split()))
amount = int(input())

# Call the mincoin function and print the result
result = mincoin(coins, amount)
print(result)

# # Bonus Version
# import sys
# import time
# sys.setrecursionlimit(10000)
# CoinChoice = list(map(int,input().split()))
# k = int(input())
# count = 0
# def mincoin(v):
#     global count
#     count += 1
#     if v <= 0:
#         return 0

#     minX = sys.maxsize
#     for c in CoinChoice:
#         if c <= v:
#             minX = min(minX, 1 + mincoin(v-c))

#     return minX

# st = time.process_time()
# print(mincoin(k))
# print(count)
# et = time.process_time()
# print(f"Running Time: {et-st}")
