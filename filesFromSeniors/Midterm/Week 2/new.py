n = int(input())
x = [None] * n

def comb(i):
    global x
    if i == n:
        print(x)
        return 1
    else:
        x[i] = 0
        s =comb(i+1)
        x[i] = 1
        s += comb(i+1)
        return s

print(comb(0))
