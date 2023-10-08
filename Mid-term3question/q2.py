p = list(map(int,input().split()))
p.append(0)
m = 0
max = 0

for i in range(len(p)-1):
    m += p[i] - p[i+1]
    if m < 0:
        if m < max:
            max = m
    else:
        m = 0
        
print(-max)
