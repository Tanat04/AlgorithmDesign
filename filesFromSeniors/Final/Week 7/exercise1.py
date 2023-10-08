def printqueens(Q):
    n = len(Q)
    board = [['.']*n for i in range(n)]
    for j in range(n):
        board[Q[j]][j] = 'Q'
    for i in range(n):
        for j in range(n):
            print(board[i][j], end='')
        print()

n = int(input())
pos = [-1]*n

class state:
    def __init__(self, pos, i):
        self.pos = pos
        self.i = i

def goal(s):
    global n

    if s.i == n:
        return True
    else:
        return False

def conflict(Q,i,j):
    if Q[i]==Q[j] or abs(Q[i]-Q[j])==abs(i-j):
        return True
    else:
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
            if conflict(u.pos, j, u.i):
                valid = False
                break
        if valid:
            u.i += 1
            succ.append(u)
    return succ

queue = []
s = state(pos, 0)
while not goal(s):
    succ = successor(s)
    for u in succ:
        queue.append(u)
    s = queue[0]
    del queue[0]
printqueens(s.pos)



