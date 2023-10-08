import sys
sys.setrecursionlimit(10001)

FLAT = 0
UPPER2 = 1
LOWER2 = 2

L = int(input())
mm = [[-1]*(3) for i in range(L+1)]


def nWays(d, s):
    if mm[d][s] == -1:
        if d == L:
            if s == FLAT:
                mm[d][s] = 1
            else:
                mm[d][s] = 0
        else:
            counter = 0
            if s == FLAT:
                counter += nWays(d+1, UPPER2)
                # Actually, this is symmetric to UPPER2
                counter += nWays(d+1, LOWER2)
                if d < L-1:
                    counter += nWays(d+2, FLAT)
            else:  # s is either UPPER2 or LOWER2
                counter += nWays(d+1, FLAT)
                if d < L-1:
                    counter += nWays(d+2, s)
            mm[d][s] = counter
    return mm[d][s]


print(nWays(0, FLAT))
