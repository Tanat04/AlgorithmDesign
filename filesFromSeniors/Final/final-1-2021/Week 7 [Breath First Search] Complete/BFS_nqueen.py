import copy

n = int(input())


class State():
    def __init__(self):
        global n

        self.queen = [-1] * n
        self.i = 0


def printqueens(Q):
    n = len(Q)
    board = [['.'] * n for i in range(n)]
    for j in range(n):
        board[Q[j]][j] = 'Q'
    for i in range(n):
        for j in range(n):
            print(board[i][j], end='')
        print()


def conflict(Q, i, j):
    if Q[i] == Q[j] or abs(Q[i] - Q[j]) == abs(i - j):
        return True
    else:
        return False


def successor_state(s):
    succ = []
    for r in range(n):
        u = copy.deepcopy(s)
        u.queen[u.i] = r
        valid = True
        for j in range(u.i):
            if conflict(u.queen, u.i, j):
                valid = False
                break
        if valid:
            u.i += 1
            succ.append(u)
    return succ


def Goal(s):
    global n
    if s.i == n:
        return True
    else:
        return False


Q = []
s = State()
while not Goal(s):
    succ = successor_state(s)
    for x in succ:
        Q.append(x)
    s = Q[0]
    del Q[0]

printqueens(s.queen)
