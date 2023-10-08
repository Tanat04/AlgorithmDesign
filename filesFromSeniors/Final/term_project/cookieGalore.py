import collections
import time

N, M = map(int, input().split())
grid = []
moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]


st = time.process_time()
for _ in range(N):
    grid.append([1 if x == "C" else 0 for x in input()])

visited = [[False] * M for _ in range(N)]
visited[0][0] = True

# memoization
dp = [[float('inf')] * M for _ in range(N)]
dp[0][0] = grid[0][0]

class State:
    def __init__(self, r, c, v):
        self.row = r
        self.column = c
        self.value = v
    def __lt__(self, other):
        return self.value < other.value

def isSafe(r, c):
    global visited
    return 0 <= r < N and 0 <= c < M and not visited[r][c]

queue = collections.deque()
queue.append(State(0, 0, grid[0][0]))

while queue:
    s = queue.popleft()
    row, column, value = s.row, s.column, s.value
    if value == dp[row][column]:
        # for loop adjacent moves
        for nRow, nColumn in moves:
            nRow += row
            nColumn += column
            # if the move is valid and new value is less than in memo
            if isSafe(nRow, nColumn) and value + grid[nRow][nColumn] < dp[nRow][nColumn]:
                visited[nRow][nColumn] = True
                dp[nRow][nColumn] = value + grid[nRow][nColumn]
                if grid[nRow][nColumn] == 1:
                    queue.append(State(nRow, nColumn, dp[nRow][nColumn]))
                else:
                    queue.appendleft(State(nRow, nColumn, dp[nRow][nColumn]))

et = time.process_time()

print(et-st)