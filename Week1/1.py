import time

start_time = time.process_time()

numbers = list(map(int, input().split()))


def Sum(X, i, j):
    sm = 0
    for k in range(i, j+1):
        sm += X[k]
    return sm


def find_max_subsequence_sum(numbers):
    largest_sum = float('-inf')  # Initialize largest_sum as negative infinity

    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            subsequence_sum = Sum(numbers, i, j)
            if subsequence_sum > largest_sum:
                largest_sum = subsequence_sum
    return largest_sum


end_time = time.process_time()
mx = find_max_subsequence_sum(numbers)
print(mx)
running_time = end_time - start_time

print("Running time: ", running_time)
