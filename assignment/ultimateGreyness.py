from itertools import combinations


def calculate_difference(colors):
    total_vividness = 1
    total_dullness = 0
    for color in colors:
        vividness, dullness = color
        total_vividness *= vividness
        total_dullness += dullness
        # print(abs(total_vividness - total_dullness))
    return abs(total_vividness - total_dullness)


def find_smallest_difference():
    N = int(input())
    min_diff = float('inf')
    colors = []

    for _ in range(N):
        vividness, dullness = map(int, input().split())
        colors.append((vividness, dullness))

    for size in range(1, N + 1):
        for combination in combinations(colors, size):
            # print(combination)
            diff = calculate_difference(combination)
            min_diff = min(min_diff, diff)

    print(min_diff)


find_smallest_difference()
