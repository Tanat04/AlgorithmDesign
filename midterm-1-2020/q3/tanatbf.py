def mincoin(coins, amount):
    # Base case: if the amount is 0, no coins are needed
    if amount == 0:
        return 0

    # Initialize the minimum number of coins required to a large value
    min_coins = float('inf')

    # Try using each coin denomination
    for coin in coins:
        # If the current coin is less than or equal to the amount, recursively calculate the minimum number of coins for the remaining amount
        if amount >= coin:
            num_coins = mincoin(coins, amount - coin)
            # Update the minimum number of coins if necessary
            min_coins = min(min_coins, num_coins + 1)
    return min_coins


# Read the input
coins = list(map(int, input().split()))
amount = int(input())

# Call the mincoin function and print the result
result = mincoin(coins, amount)
print(result)
