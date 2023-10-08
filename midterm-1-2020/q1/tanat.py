import time

start_time = time.process_time()

numbers = list(map(int, input().split()))


def kadane_algorithm(numbers):
    max_sum = 0
    current_sum = 0

    for num in range(0, len(numbers)):
        current_sum = max(numbers[num], current_sum + numbers[num])
        max_sum = max(max_sum, current_sum)

    return max(max_sum, 0)


end_time = time.process_time()
mx = kadane_algorithm(numbers)
print(mx)
