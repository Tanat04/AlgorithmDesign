import copy
n = int(input())

'''
self.a is a list of length n, initialized with -1. It will store the row number for each queen in each column.
self.b is an integer initialized to 0, representing the current column where a queen is being placed.
'''


class state():
    def __init__(self, n):
        self.a = [-1]*n
        self.b = 0

# The conflict function checks if there is a conflict between two queens placed at columns i and j.


def conflict(Q, i, j):
    if Q[i] == Q[j] or abs(Q[i] - Q[j]) == abs(i-j):
        return True
    else:
        return False

# The goal function checks if the current state v has placed all n queens on the board.


def goal(v):
    if v.b == n:
        return True
    else:
        return False

# The valid function checks if the current state v has a valid placement for the queen being placed in the current column.


def valid(v):
    for j in range(v.b):
        if conflict(v.a, j, v.b):
            return False
    return True

# The successor function generates all valid successor states from the current state v.


def successor(v):
    succ = []
    for row in range(n):
        w = copy.deepcopy(v)
        w.a[w.b] = row
        if valid(w):
            w.b += 1
            succ.append(w)
    return succ


def printqueens(Q):
    n = len(Q)
    board = [['.']*n for i in range(n)]
    for j in range(n):
        board[Q[j]][j] = 'Q'
    for i in range(n):
        for j in range(n):
            print(board[i][j], end='')
        print()


s = state(n)
u = []
while not goal(s):
    for x in successor(s):
        u.append(x)
    s = u[0]
    del u[0]

print(s.a)
printqueens(s.a)

'''
import time
N = int(input())
Q = [None for _ in range(N)]
def printqueens(Q):
    n = len(Q)
    board = [['.']*n for i in range(n)]
    for j in range(n):
        board[Q[j]][j] = 'Q'
    for i in range(n):
        for j in range(n):
            print(board[i][j], end='')
        print()

def conflict(Q, i, j):
    #Check Horizontal and Diagonal
    return Q[i] == Q[j] or abs(Q[i]-Q[j]) == abs(i-j)

class state():
    def __init__(self, Q):
        self.Q = Q
        self.g = 0  # Current Modifying Column Index
        self.parent = None


def stateEqual(s1, s2):
    return s1.Q == s2.Q


def successor(s):
    if s.g == N:  # If Board is Full, There is no successor
        return []

    succ = []
    for j in range(N):
        newQ = s.Q.copy()
        newQ[s.g] = j

        x = state(newQ)

        no_conflict = True
        for k in range(s.g):
            if conflict(x.Q, k, s.g):
                no_conflict = False
                break

        if no_conflict:
            x.g = s.g + 1
            x.parent = s
            succ.append(x)

    return succ


def is_goal(s):
    return sum([1 for i in range(N) if s.Q[i]==None]) == 0

def BreadthFirstSearch(s):
    Q = [s]
    Reached = set()
    Reached.add(tuple(s.Q))
    while Q:
        node = Q[0]
        del Q[0]
        if is_goal(node):
            return node.g
        for suc in successor(node):
            if tuple(suc.Q) not in Reached:
                Reached.add(tuple(suc.Q))
                Q.append(suc)
def BreadthFirstSearch(s):
    global count
    Q = [s]
    Reached = set()
    Reached.add(s)
    solution = []
    while Q:
        node = Q[0]
        del Q[0]

        if is_goal(node):
            exist = False
            for s1 in solution:
                if stateEqual(s1, node):
                    exist = True
                    break
            if not exist:
                print(f"Solution #{len(solution)+1}")
                printqueens(node.Q)
                solution.append(node)

        for suc in successor(node):
            SInReached = False
            for d in Reached:
                if stateEqual(d, suc):
                    SInReached = True
                    break

            if not SInReached:
                Reached.add(suc)
                Q.append(suc)


s = state(Q)
BreadthFirstSearch(s)
'''
