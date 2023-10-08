import time

start_time = time.process_time()


def find_product_k(K, numbers):
    # Initialize DAT with False values
    DAT = [False] * (12999709 - (-12999709) + 1)

    for num in numbers:
        if num < 0:
            num = -num + 12999709  # Map negative numbers to positive indices
        DAT[num] = True  # Mark num as True in the DAT

    for num in numbers:
        complement = K // num
        if complement < 0:
            # Map negative complements to positive indices
            complement = -complement + 12999709
        if complement <= 12999709 and K % num == 0 and DAT[complement]:
            print("Number: ", num, complement)
            return True  # K can be formed using two numbers in the list

    return False  # No two numbers can form K


# Example usage:
K = int(input())  # Read the targeted product K from input or any other source
# Read the list of numbers from input or any other source
numbers = list(map(int, input().split()))

result = find_product_k(K, numbers)
print(result)


end_time = time.process_time()
running_time = end_time - start_time

print("Running time: ", running_time)
