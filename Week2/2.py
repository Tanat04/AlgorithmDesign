def generate_combinations(n):
    x = [0] * n  # Initialize a list of length n to store the combination
    count = 0  # Variable to keep track of the number of combinations

    def comb(i):
        nonlocal count  # Use the nonlocal keyword to modify the count variable

        if i == n:
            print(*x)
            count += 1
            return

        x[i] = 0
        comb(i + 1)

        x[i] = 1
        comb(i + 1)

    comb(0)  # Start with the first index of the combination

    print("Total combinations:", count)
    print("Expected total combinations:", 2 ** n)


# Test the function
generate_combinations(3)
