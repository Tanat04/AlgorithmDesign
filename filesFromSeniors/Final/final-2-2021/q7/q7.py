class obj:
    def __init__(self, w, v):
        self.w = w
        self.v = v
        self.r = v/w


x = input().split()
N = int(x[1])
M = int(x[0])
item = []

for i in range(N):
    item.append(obj(*map(int, input().split())))

maxV = 0
count = 0


def Bound(i, sumW, sumV):
    global item, N, M

    RightWeight = 0
    SV = 0
    propotion = 1
    j = i + 1

    # proportion == 1 means the item[t] can be put into the knapsack physically
    # M-sumW-RightWeight > 0 means there is still space in the knapsack

    # t < N means there are still items to be considered
    while j < N and propotion == 1:
        # if the item[t] can be put into the knapsack physically then propotion is 1
        # otherwise propotion is the proportion of the item[t] that can be put into the knapsack

        propotion = min(M - sumW - RightWeight, item[j].w) / item[j].w
        RightWeight += propotion * item[j].w
        SV += propotion * item[j].v
        j += 1

    return SV + sumV


def dfs(i, sumW, sumV):
    global maxV, item, N, M, count

    count += 1
    if i == N:
        maxV = max(maxV, sumV)  # update maxV
    else:
        # only consider if it is possible to put item[h] into the knapsack
        if sumW + item[i].w <= M:
            dfs(i+1, sumW+item[i].w, sumV+item[i].v)

        # Bound is the maximum possible value of the knapsack illegally
        # If you cheat and still cannot get a better solution, then there is no need to consider the rest of the items
        if Bound(i, sumW, sumV) > maxV:  # only consider if it is possible to get a better solution
            dfs(i+1, sumW, sumV)


item.sort(key=lambda x: x.r, reverse=True)
dfs(0, 0, 0)
print(maxV)

# # Read input
# initial_investment, num_stocks = map(int, input().split())

# stock_info = []
# for _ in range(num_stocks):
#     current_price, one_year_profit = map(int, input().split())
#     stock_info.append((one_year_profit, current_price))

# # Sort stocks by profit-to-price ratio in descending order
# stock_info.sort(key=lambda x: x[0] / x[1], reverse=True)

# max_total_profit = 0
# remaining_budget = initial_investment

# for profit, price in stock_info:
#     if remaining_budget >= price:
#         max_total_profit += profit
#         remaining_budget -= price
#     else:
#         max_total_profit += (remaining_budget / price) * profit
#         break

# print(int(max_total_profit))
