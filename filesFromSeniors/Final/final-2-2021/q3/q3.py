def partition(arr, left, right):
    # Choose the pivot element
    pivot = arr[right]
    i = left - 1

    # Partition the array into elements <= pivot and elements > pivot
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            # Swap elements arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    # Place the pivot element in its correct position
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def kth_order_statistic(arr, left, right, k):
    if left == right:
        # If the array has only one element, return it
        return arr[left]

    # Partition the array and get the pivot index
    pivot_index = partition(arr, left, right)

    if k == pivot_index:
        # If k matches the pivot index, return the kth order statistic
        return arr[pivot_index]
    elif k < pivot_index:
        # If k is less than the pivot index, search in the left subarray
        return kth_order_statistic(arr, left, pivot_index - 1, k)
    else:
        # If k is greater than the pivot index, search in the right subarray
        return kth_order_statistic(arr, pivot_index + 1, right, k)


# Input: Read the array and k
arr = list(map(int, input().split()))
k = int(input())

# Find kth order statistic
result = kth_order_statistic(arr, 0, len(arr) - 1, k - 1)

# Output: Print the kth order statistic
print(result)


# def partition(arr, low, high):
#     pivot = arr[low]
#     i = low
#     for j in range(low+1, high+1):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i], arr[low] = arr[low], arr[i]
#     return i

# def kth_smallest(arr, l, h, k):
#     if l <= h:
#         pivotIndex = partition(arr, l, h)
#         if pivotIndex == k - 1:
#             return arr[pivotIndex]
#         elif pivotIndex > k - 1:
#             return kth_smallest(arr, l, pivotIndex - 1, k)
#         else:
#             return kth_smallest(arr, pivotIndex + 1, h, k)
#     return None

# def main():
#     # Reading input
#     numbers = list(map(int, input().split()))
#     k = int(input())

#     # Finding kth smallest value
#     result = kth_smallest(numbers, 0, len(numbers)-1, k)
#     print(result)

# if __name__ == "__main__":
#     main()
