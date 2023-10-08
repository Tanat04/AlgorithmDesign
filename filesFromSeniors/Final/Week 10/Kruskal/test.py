
class activity():
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

def isOverlapped(a1, a2):
    return a1.finish >= a2.start

n = int(input())
aList = []
for i in range(n):
    s, t = map(int, input().split())
    aList.append(activity(s, t))

sortedByFinish = sorted(aList, key=lambda activity: activity.finish)

count = 0
keepList = []
current = sortedByFinish[0]
keepList.append(current)

for i in sortedByFinish[1:]:
    if not isOverlapped(current, i):
        keepList.append(i)
        current = i
    #else:
        #print("conflict")

for act in keepList:
    count += 1
    #print(act.start, act.finish)

print(count)

#kruskal algorithm, pick the edge that doesn't cause conflict(edge cause cycle). Any element must not be in both sets. 
# 1 3
# 1 8
# 2 5
# 4 7
# 5 9
# 8 10
# 9 11
# 11 14
# 13 16
