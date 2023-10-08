import time

start_time = time.process_time()

numbers = list(map(int, input().split()))


def kadane_algorithm(numbers):
    max_sum = 0  # or do = numbers[0]
    current_sum = 0  # or do = numbers[0]

    print(numbers)
    for num in range(0, len(numbers)):
        print(current_sum, numbers[num], current_sum + numbers[num])
        current_sum = max(numbers[num], current_sum + numbers[num])
        print(current_sum, max_sum)
        max_sum = max(max_sum, current_sum)
        print(max_sum)

    return max(max_sum, 0)


end_time = time.process_time()
mx = kadane_algorithm(numbers)
print(mx)
