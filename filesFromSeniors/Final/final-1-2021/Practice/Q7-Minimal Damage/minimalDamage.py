import copy
from simplePriorityQueue import Simple_Priority_Queue

class state:
    def __init__(self, x, damage):
        self.x = x
        self.damage = damage

def goal(s):
    return len(s.x) <= 3

def mycomp(x, y):
    return sum(x.x) < sum(y.x)

origin = list(map(int, input().split()))
s = state(origin, 0)
pq = Simple_Priority_Queue(mycomp)
while not goal(s):
    for i in range(1, len(s.x)-1):
        l = copy.deepcopy(s)
        del l.x[i-1:i+2]
        l.damage += sum(l.x)
        pq.enqueue(l)
    s = pq.dequeue()
print(s.damage)


