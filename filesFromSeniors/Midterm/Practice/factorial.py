n = int(input())
result = n
if n == 0:
    print("1")
else:
    for i in range(1, n):
        result *= i
    print(result)