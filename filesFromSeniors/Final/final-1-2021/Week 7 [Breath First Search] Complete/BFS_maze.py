M, N = map(int, input().split())
sr, sc = map(int, input().split())
dr, dc = map(int, input().split())

maze = []
for r in range(M):
    x = list(map(int, input().split()))
    for c in range(N):
        x[c] *= -1
    maze.append(x)

class state:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.step = 0


def goal(s):
    if s.r == dr and s.c == dc:
        return True
    else:
        return False


def valid(r, c):
    if 0 <= r < M and 0 <= c < N:
        if maze[r][c] != -1:
            return True
    return False


adj = [(-1, 0), (1, 0), (0, -1), (0, 1)]
import copy


def successor_state(s):
    succ = []
    for d in adj:
        r = s.r + d[0]
        c = s.c + d[1]
        if valid(r, c):
            u = copy.deepcopy(s)
            u.r = r
            u.c = c
            u.step += 1
            succ.append(u)
    return succ


s = state(sr, sc)
Q = []
while not goal(s):
    succ = successor_state(s)
    for x in succ:
        Q.append(x)
    s = Q[0]
    del Q[0]

print(s.step)
