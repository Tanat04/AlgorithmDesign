def balance_split(goods):
    n = len(goods)
    min_diff = float('inf')  # Initialize minimum difference with infinity

    def calculate_difference(combination):
        total_group_1 = 0
        total_group_2 = 0
        for i in range(n):
            if combination[i] == 0:
                total_group_1 += goods[i]
            else:
                total_group_2 += goods[i]
        return abs(total_group_1 - total_group_2)

    def generate_combinations(i, combination):
        nonlocal min_diff

        if i == n:
            diff = calculate_difference(combination)
            min_diff = min(min_diff, diff)
            return

        for option in [0, 1]:
            combination[i] = option
            generate_combinations(i + 1, combination)

    combination = [0] * n
    generate_combinations(0, combination)

    return min_diff


# Test the function
values = list(map(int, input().split()))
minimal_difference = balance_split(values)
print("Minimal difference:", minimal_difference)
