price_list = list(map(int, input().split()))

maxVal = 0
price_sum = 0

for i in range(len(price_list)):
    price_sum = max(price_sum + price_list[i], 0)
    if price_sum > maxVal:
        maxVal = price_sum


print(maxVal)
