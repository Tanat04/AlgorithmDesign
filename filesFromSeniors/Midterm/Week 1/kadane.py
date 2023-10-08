n = int(input())
numList = []
for j in range(n):
    numList.append(int(input()))

maxCurrent = 0

if numList[0] >= 0:
    maxValue = numList[0] 
else:
    maxValue = 0
    
for i in range(1, len(numList)):
    maxCurrent = max(numList[i]+maxCurrent, numList[i])
    maxValue = max(maxCurrent, maxValue)

print(maxValue)

