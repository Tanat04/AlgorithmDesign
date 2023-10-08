from simplePriorityQueue import *

H, T = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(H)]
adj = [1, 0, -1]


class state():
    def __init__(self, h, t):
        self.h = h
        self.t = t
        self.cost = maze[h][t]  # number of steps from start to this state
        self.parent = None


def valid(h, t):
    return 0 <= h < H and 0 <= t < T


def successor(s):
    succ = []
    for y in adj:
        new_t = s.t + y
        if valid(s.h+1, new_t):
            x = state(s.h+1, new_t)
            x.cost = s.cost + maze[x.h][x.t]
            x.parent = s
            succ.append(x)
    return succ


def is_goal(s):
    return s.h == H - 1


def BFS(s):
    global maximum
    Q = Simple_Priority_Queue(lambda x, y: x.cost > y.cost)
    Q.enqueue(s)

    while not Q.empty():
        node = Q.dequeue()
        if is_goal(node):
            maximum = max(maximum, node.cost)

        for suc in successor(node):
            Q.enqueue(suc)

    return True


maximum = -1
for t in range(T):
    BFS(state(0, t))
print(maximum)
