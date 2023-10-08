prices = list(map(int,input().split()))

Max = 0
sum = 0

for i in range(len(prices)):
    sum = max(sum+prices[i],0)
    if sum > Max:
        Max = sum

print(Max)