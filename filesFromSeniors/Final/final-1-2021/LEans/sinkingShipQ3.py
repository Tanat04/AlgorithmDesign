# Voraruethai Chancharung 6210109
# Question 3: Sinking Ship

x = int(input())
y = []

for i in range(x):
    inp = list(map(int, input().split())) 
    y.append(inp)
masterY = y.copy()

total = 0

def findMax(a):
    maxx = []
    for i in a:
        maxx.append(max(i))
    return maxx

def findIndex(a, value):
    maxIndex = []
    for i in range(len(a)):
        if a[i] == value:
            maxIndex.append(i)
    return max(maxIndex)


for i in range(x-1,-1,-1):
    max_each_floor = findMax(masterY)
    maxIndex = findIndex(max_each_floor, max(max_each_floor))
    total += max_each_floor[maxIndex]
    masterY[maxIndex].remove(max(max_each_floor))
    masterY.pop(i)
    # print(masterY)

print(total)



