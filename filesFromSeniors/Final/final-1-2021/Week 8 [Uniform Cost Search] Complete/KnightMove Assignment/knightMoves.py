from sys import stdin

moveRow = [2, 1, -1, -2, -2, -1, 1, 2]
moveColumn = [1, 2, 2, 1, -1, -2, -2, -1]

class knightClass():
    def __init__(self, column, row, step):
        self.column = column
        self.row = row
        self.step = step

def charToInt(c):
    return ord(c) - ord('a') + 1

def isInside(column, row):
    return column >= 1 and column <= 8 and row >= 1 and row <= 8


def knightMoveBFS(sColumn, sRow, dColumn, dRow):
    Q = [knightClass(sColumn, sRow, 0)]

    while Q != []:
        knight = Q.pop(0)
        if knight.column == dColumn and knight.row == dRow:
            return knight.step
        for r in range(8):
            nextColumn = knight.column + moveColumn[r]
            nextRow = knight.row + moveRow[r]
            if isInside(nextColumn, nextRow):
                Q.append(knightClass(nextColumn, nextRow, knight.step + 1))

for line in stdin:
    s, d = line.split()
    sColumn = charToInt(s[0])
    sRow = int(s[1])

    dColumn = charToInt(d[0])
    dRow = int(d[1])
    
    print('To get from {0} to {1} takes {2} knight moves.'.format(s, d, knightMoveBFS(sColumn, sRow, dColumn, dRow)))

