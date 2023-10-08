actS = [1, 2, 4, 1, 5, 8, 9, 11, 13]
actF = [3, 5, 7, 8, 9, 10, 11, 14, 16]
durations = []
activities = []


class Activity:
    def __init__(self, n, s, f):
        self.number = n
        self.start = s
        self.finish = f


# for i in range(len(actS)):
# activities.append(Activity(i + 1, actS[i], actF[i]))

for i in range(len(activities)):
    durations.append(activities[i].finish - activities[i].finish)

# duration sort
# print(sorted(durations))

# start sort
# print(sorted(actS))


def hasConflict(a, b):
    return a.finish >= b.start


def maxActivities(arr):
    actArr = [arr[0]]
    newIndex = 0
    for i in range(len(arr)-1):
        if not hasConflict(arr[newIndex], arr[i + 1]):
            actArr.append(arr[i + 1])
            newIndex = i + 1

    return actArr


n = int(input())

for i in range(n):
    sf = list(map(int, input().split()))
    activities.append(Activity(i + 1, sf[0], sf[1]))

activities = sorted(activities, key=lambda activity: activity.finish)

ans = maxActivities(activities)
for i in range(len(ans)):
    print(ans[i].number, ans[i].start, ans[i].finish)

print(len(ans))