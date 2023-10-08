# version 1
def fibonacci(n):

    result = [1, 1]

    for i in range(len(result), n + 2):
        num = result[i-1] + result[i-2]
        result.append(num)

    print(result[-1])


fibonacci(28)

# version 2

# n = int(input())
# nList = [None] * (n+1)

# def fibo_recur(n):
#     for i in range(n+1):
#         if i == 0 or i == 1:
#             nList[i] = i + 1
#         else:
#             nList[i] = nList[i-1] + nList[i-2]
#     return nList[-1]

# print(fibo_recur(n))

# # orginal fibonacci
# def fibonacci(n):

#     result = [1, 1]

#     for i in range(len(result), n):
#         num = result[i-1] + result[i-2]
#         result.append(num)

#     print(result)


# fibonacci(7)
