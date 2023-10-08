# Voraruethai Chancharung 6210109
# Question 4: Typing jobs


n, t, r = list(map(int, input().split()))
sat = list(map(int, input().split()))
sun = list(map(int, input().split()))

over = 0
remain = 0

for i in range(len(sat)):
    numPaper = sat[i] + sun[i]
    numPaper -= t
    if numPaper >= 1:
        over += numPaper
    else:
        remain += abs(numPaper)

result = abs(over - remain)*r
print(result)