import time

start_time = time.process_time()

numbers = [5, 6, 7, 8, 9, 10]

prices = []

for i in range(1, len(numbers)):
    prices.append(numbers[i] - numbers[i - 1])

print(prices)


def kadane_algorithm(numbers):
    max_sum = 0  # or do = numbers[0]
    current_sum = 0  # or do = numbers[0]
    for num in range(0, len(numbers)):
        current_sum = max(numbers[num], current_sum + numbers[num])
        max_sum = max(max_sum, current_sum)

    return max(max_sum, 0)


end_time = time.process_time()
mx = kadane_algorithm(prices)
print(mx)
