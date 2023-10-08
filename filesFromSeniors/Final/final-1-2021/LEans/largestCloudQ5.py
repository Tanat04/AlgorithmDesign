# Voraruethai Chancharung 6210109
# Question 5: Largest Cloud

row, column = list(map(int, input().split()))
pic = []

for i in range(row):
    inp = list(map(int, input().split()))
    pic.append(inp)

masterPic = pic.copy()

def cloud(r, c):
    global pic, row, column

    if r < 0 :
        return 0
    if r > row-1:
        return 0
    if c < 0:
        return 0
    if c > column-1:
        return 0

    if pic[r][c] == 0:
        return 0
    else:
        pic[r][c] = 0
        return 1 + cloud(r, c-1) + cloud(r, c+1) + cloud(r-1, c) + cloud(r+1, c)

result = []
for i in range(row):
    for j in range(column):
        pic = masterPic.copy()
        result.append(cloud(i,j))

print(max(result))