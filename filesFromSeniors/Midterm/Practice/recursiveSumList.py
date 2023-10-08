def fib(nth):
    if nth == 1:
        return 0
    elif nth == 2:
        return 1
    else:
        return fib(nth - 1) + fib(nth - 2)

print(fib(5))