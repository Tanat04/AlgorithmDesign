N,K,S = list(map(int,input().split()))
position = [S]
score = [0]

for i in range(N):
   p,s = list(map(int,input().split()))
   position.append(p)
   score.append(s)

def Quicksilver(N,K,S,position,score):
    hs = [0 for a in range(N+1)]
    for i in range(1,N+1):
        for j in range(i-1, -1, -1):
           if j == 0 or hs[j] != 0:
              if abs(position[i] - position[j]) <= K:
                 hs [i] = max(hs[i], score[i] + hs[j])
    return max(hs)

print(Quicksilver(N,K,S,position,score))
