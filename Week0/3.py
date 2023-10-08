import time

start_time = time.process_time()


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False


def find_product_k(K, numbers):
    numbers.sort()  # Sort the numbers in ascending order

    for i in range(len(numbers)):
        num1 = numbers[i]

        if num1 != 0 and K % num1 == 0:
            complement = K // num1
            if binary_search(numbers, complement):
                print(num1, complement)
                return True

    return False


# Example usage:
K = int(input())  # Read the targeted product K from input or any other source
# Read the list of numbers from input or any other source
numbers = list(map(int, input().split()))

result = find_product_k(K, numbers)
print(result)


end_time = time.process_time()
running_time = end_time - start_time

print("Running time: ", running_time)
