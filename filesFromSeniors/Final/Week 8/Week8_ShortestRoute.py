from simplePriorityQueue import Simple_Priority_Queue
from sys import stdin

INF = 1000000000
V = int(input())
adj = [[] for i in range(V)]
for line in stdin:
    x = line.split()
    u = int(x[0])
    v = int(x[1])
    w = int(x[2])
    adj[u].append((v,w))
    adj[v].append((u,w))

class state:
    def __init__(self, city, distance):
        self.city = city
        self.d = distance

def goal(s):
    return s.city == V-1

import copy

def successor(s):
    succ = []
    for u,w in adj[s.city]:
        v = copy.deepcopy(s)
        v.city = u
        v.d = s.d + w #from the source state to the next city state
        succ.append(v)
    return succ

def mycomp(x, y):
    return x.d < y.d #the distance of the adjacent city

# memo
memo = [False] * V

s = state(0,0)
pq = Simple_Priority_Queue(mycomp)
while not goal(s):
    if not memo[s.city]:
        succ = successor(s)
        for x in succ:
            pq.enqueue(x)
        memo[s.city] = True
    s = pq.dequeue()


print(s.d)