k = 0  # Declare the global variable 'k' outside the function


def generate_combinations(n, k_input):
    global k  # Declare 'k' as a global variable to access it within the function
    k = k_input  # Assign the input value of 'k' to the global variable

    x = [0] * n  # Initialize a list of length n to store the combination
    count = 0  # Variable to keep track of the number of combinations

    def comb(i):
        nonlocal count  # Use the nonlocal keyword to modify the count variable

        if i == n:  # Base case: combination is complete
            if x.count(1) == k:  # Check if the combination has exactly 'k' 1's
                print(*x)  # Print the combination
                count += 1
            return

        x[i] = 0  # Assign the ith item as 0 (not selected)
        comb(i + 1)  # Recursive call with the next index

        x[i] = 1  # Assign the ith item as 1 (selected)
        comb(i + 1)  # Recursive call with the next index

    comb(0)  # Start with the first index of the combination

    print("Number of combinations with exactly", k, "1's:", count)
    print("Expected number of combinations:", factorial(
        n) // (factorial(n - k) * factorial(k)))

# Helper function to calculate factorial


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Test the function
generate_combinations(3, 2)
