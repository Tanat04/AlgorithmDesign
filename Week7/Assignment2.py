import sys

sys.setrecursionlimit(10001)

FLAT = 0
UPPER2 = 1
LOWER2 = 2


def read_lengths():
    lengths = []
    while True:
        length = int(input())
        if length == -1:
            break
        lengths.append(length)
    return lengths


def count_ways(d, s, memo, L):
    if memo[d][s] is not None:
        return memo[d][s]

    if d == L:
        return 1 if s == FLAT else 0
    else:
        counter = 0
        if s == FLAT:
            counter += count_ways(d + 1, UPPER2, memo, L)
            counter += count_ways(d + 1, LOWER2, memo, L)
            if d < L - 1:
                counter += count_ways(d + 2, FLAT, memo, L)
        else:
            counter += count_ways(d + 1, FLAT, memo, L)
            if d < L - 1:
                counter += count_ways(d + 2, s, memo, L)

        memo[d][s] = counter
        return memo[d][s]


def solve_one_case(L):
    memo = [[None for _ in range(3)] for _ in range(L + 1)]
    for i in range(L, -1, -1):
        for j in range(3):
            count_ways(i, j, memo, L)

    print(memo[0][FLAT])


def main():
    lengths = read_lengths()
    if lengths:
        for length in lengths:
            if length <= 0:
                print(1)
                continue
            solve_one_case(length)


if __name__ == "__main__":
    main()
