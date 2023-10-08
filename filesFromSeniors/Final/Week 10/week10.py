import sys 
sys.setrecursionlimit(10000000)

a, x = map(int, input().split())
mod = 2147483647

def expo(a, x):
    if x == 0:
        return 1
    else:
        i = expo(a, x // 2)

        if x % 2 == 0:
            return (i * i) % mod
        else:
            return ((i * i) % mod * a) % mod

print(expo(a, x))