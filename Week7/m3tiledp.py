import sys
sys.setrecursionlimit(10001)

FLAT = 0
UPPER2 = 1
LOWER2 = 2

L = int(input())

mm = [[-1] * 3 for _ in range(L + 1)]

mm[L][FLAT] = 1

for d in range(L-1, -1, -1):
    for s in [FLAT, UPPER2, LOWER2]:
        counter = 0
        if s == FLAT:
            counter += mm[d+1][UPPER2]
            # Actually, this is symmetric to UPPER2
            counter += mm[d+1][LOWER2]
            if d < L-1:
                counter += mm[d+2][FLAT]
        else:  # s is either UPPER2 or LOWER2
            counter += mm[d+1][FLAT]
            if d < L-1:
                counter += mm[d+2][s]

        mm[d][s] = counter

result = mm[0][FLAT]
print(result)
