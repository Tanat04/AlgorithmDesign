import sys

sys.setrecursionlimit(10000)


n = int(input())

x = []


def generating_combination(n):

    global x
    x = [0] * n

    def comb(i):
        print("'i' is:", i)
        print('N is:', n)
        if i == n:
            print(*x)
            return

        for option in [0, 1]:
            print('i and option', i, option)
            print(x)
            x[i] = option
            print(x)
            comb(i + 1)

    comb(0)


generating_combination(n)
