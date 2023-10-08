import time

start_time = time.process_time()

numbers = list(map(int, input().split()))


def Sum(accumulated, i, j):
    print(accumulated, i, j)
    print(accumulated, accumulated[i], accumulated[j])
    if i == 0:
        return accumulated[j]
    print(accumulated[j] - accumulated[i-1])
    return accumulated[j] - accumulated[i-1]


def find_max_subsequence_sum(numbers):
    accumulated = []
    acc = 0

    for num in numbers:
        acc += num
        accumulated.append(acc)

    largest_sum = float('-inf')

    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            subsequence_sum = Sum(accumulated, i, j)
            print(subsequence_sum, largest_sum)
            if subsequence_sum > largest_sum:
                largest_sum = subsequence_sum

    return largest_sum


end_time = time.process_time()
mx = find_max_subsequence_sum(numbers)
print(mx)
running_time = end_time - start_time

print("Running time: ", running_time)
