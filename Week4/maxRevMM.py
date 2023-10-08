import sys
sys.setrecursionlimit(10000)

p = list(map(int, input().split()))
L = len(p)
call = [0] * (L + 1)
mm = [None]*(L+1)

p.insert(0, 0)
count = 0


def maxRev(l):
    global p, L
    global count, call

    if mm[l] == None:
        call[l] += 1
        count += 1

        if l == 0:
            mm[l] = 0
        else:
            mm[l] = -1
            for i in range(1, l+1):
                mm[l] = max(mm[l], p[i] + maxRev(l-i))
    return mm[l]


print(maxRev(L))
print("Total Visits: ", count)
print("Calls: ", call)


# # Bonus code
# import sys
# import time

# sys.setrecursionlimit(10000)
# Price = list(map(int, input().split()))
# l = len(Price)
# count = 0
# calls = [0 for _ in range(l+1)]
# MaximumRevenue = [None for _ in range(l + 1)]
# MaximumRevenue[0] = 0
# def RodCut(l):
#     global MaximumRevenue, calls, count
#     if MaximumRevenue[l] == None:
#         calls[l] += 1
#         count += 1

#         maxRev = -1
#         for i in range(1, l + 1):
#             maxRev = max(maxRev, Price[i-1] + RodCut(l-i))

#         MaximumRevenue[l] = maxRev


#     return MaximumRevenue[l]


# st = time.process_time()
# print(RodCut(l))
# print(count)
# print(calls)
# et = time.process_time()
# print(f"Running Time: {et - st}")
