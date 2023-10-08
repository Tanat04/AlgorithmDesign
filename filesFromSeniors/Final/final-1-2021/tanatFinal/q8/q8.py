import itertools


def calculate_min_sum_of_ratings(n, ratings):
    min_sum = float('inf')
    for pairing in itertools.permutations(range(n)):
        sum_ratings = sum(ratings[i][pairing[i]] for i in range(n))
        min_sum = min(min_sum, sum_ratings)

    return min_sum


# Input
n = int(input())
ratings = [list(map(int, input().split())) for _ in range(n)]

# Calculate and print the minimum possible sum of ratings
result = calculate_min_sum_of_ratings(n, ratings)
print(result)
