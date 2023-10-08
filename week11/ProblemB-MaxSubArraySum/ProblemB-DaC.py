# Divide and Conquer for maximum contiguous subarray
x = list(map(int, input().split()))
n = len(x)


def maxCrossingSum(x, left, middle, right):
    sum = 0
    leftSum = -1
    for i in range(middle, left - 1, -1):
        sum += x[i]
        if sum > leftSum:
            leftSum = sum

    sum = 0
    rightSum = -1
    for i in range(middle + 1, right + 1):
        sum += x[i]
        if sum > rightSum:
            rightSum = sum

    return leftSum + rightSum


def maxSubArraySum(x, left, right):
    if left == right:
        return x[left]

    middle = (left + right) // 2

    return max(maxSubArraySum(x, left, middle),
               maxSubArraySum(x, middle + 1, right),
               maxCrossingSum(x, left, middle, right))


print(maxSubArraySum(x, 0, n - 1))

'''While the Divide and Conquer approach is a valid way to solve the maximum subarray sum 
problem and has a time complexity of O(n log n), it's not as efficient as Kadane's algorithm 
for this specific problem. Here's why Kadane's algorithm is better:

Simplicity: Kadane's algorithm is simpler and more intuitive to implement.
Efficiency: Kadane's algorithm has a linear time complexity of O(n), while the Divide and 
Conquer approach has a higher time complexity of O(n log n).
Space: Kadane's algorithm uses a constant amount of space, whereas the Divide and Conquer 
approach uses additional space for recursive calls.
In practice, Kadane's algorithm is the preferred choice for solving the maximum subarray 
sum problem because of its efficiency and simplicity. The Divide and Conquer approach may 
be more suitable for solving other types of problems where the Divide and Conquer paradigm 
is a better fit.'''
