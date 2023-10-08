class obj:
    def __init__(self,w,v):
        self.w = w
        self.v = v
        self.r = v/w



x = input().split()
N = int(x[0])
M = int(x[1])
w = input().split()
v = input().split()

item = []
for i in range(N):
    item.append(obj(int(w[i]),int(v[i])))

def getKey(x):
    return x.r

def Bound(i, C):	# object i -> n-1, capacity = C
    global item, N
    
    sw = 0
    sv = 0
    j = i
    f = 1.0
    while j < N and f == 1.0:
        wj = min(C-sw, item[j].w)
        f = float(wj)/item[j].w
        sw += f*item[j].w
        sv += f*item[j].v
        j += 1
    return sv

maxV = 0
count = 0
item.sort(key=getKey, reverse=True)


def dfs(i, sumW, sumV):
    global maxV, item, N, M,count 

    count += 1
    
    if i == N:
        maxV = max(maxV, sumV)
    else:
        dfs(i+1, sumW, sumV)
        if sumW + item[i].w <= M:
            if Bound(i, M-sumW) :
                dfs(i+1, sumW+item[i].w, sumV+item[i].v)

dfs(0,0,0)
print(maxV)
print(count)
