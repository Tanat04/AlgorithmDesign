g = int(input("Input the number of generations:"))

M = [0] * (g+1)
F = [0] * (g+1)
M[0] = 1

for i in range(g):
    M[i+1] = F[i]
    F[i+1] = M[i] + F[i]

print(M[g]+F[g])
