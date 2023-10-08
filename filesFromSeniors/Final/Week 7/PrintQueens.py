adj = [(0,-1),(0,1),(-1,0),(1,0)]

class state:
    def __init__(self, pos, i):
        self.pos = pos
        self.i = i

def goal(s):
    global n

    if s.i == (dr,dc):
        return True
    else:
        return False

def valid(r,c):
    global steps
    
    if r >= 0 and r < 10 and c >= 0 and c < 10:
        if steps[r][c] == 0:
            return True
    return False

import copy

def successor(s):
    global n

    succ = []
    for r in range(n):
        u = copy.deepcopy(s)
        u.pos[u.i] = r
        valid = True
        for j in range(u.i):
            if valid(u.pos, j, u.i):
                valid = False
                break
        if valid:
            u.i += 1
            succ.append(u)
    return succ

r, w = list(map(int, input().split()))
sr, sc = list(map(int, input().split()))
dr, dc = list(map(int, input().split()))
maze = []
pos = [(0,-1),(0,1),(-1,0),(1,0)]

for row in range(r):
    maze.append(input())

queue = []
s = state(pos, 0)
while not goal(s):
    succ = successor(s)
    for u in succ:
        queue.append(u)
    s = queue[0]
    del queue[0]
