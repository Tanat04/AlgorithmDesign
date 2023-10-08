n = int(input())
k = int(input())
x = [None] * n

# Question 4
def comb(i):
    global x
    global k
    if i == n:
        print(x)
        if x.count(1) == k:
            return 1
        else:
            return 0
    else:
        x[i] = 0
        s = comb(i+1)
        x[i] = 1
        s += comb(i+1)
        return s

# def comb(i):
#     global x
#     global k
#     if i == n:
#         print(x)
#         return 1
#     else:
#         x[i] = 0
#         s = comb(i+1)
#         x[i] = 1
#         s += comb(i+1)
#         x[i] = 2
#         s += comb(i+1)
#         return s
    
comb(0)