V, E = map(int, input().split())
edgeList = []
for i in range(E):
    edgeList.append(tuple(map(int, input().split())))

class DisjointSets:
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [0]*n
        
    def findset(self, u):
        if self.p[u] == u:
            return u
        else:
            self.p[u] = self.findset(self.p[u])
            return self.p[u]

    def union(self, u,v):
        a = self.findset(u)
        b = self.findset(v)
        if self.rank[a] < self.rank[b]:
            self.p[a] = b
        else:
            self.p[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1

s = DisjointSets(V)

edgeList.sort(key=lambda edge: edge[2])
A = 0
edgeCount = 0
for u,v,w in edgeList:
    if s.findset(u) != s.findset(v):
        s.union(u, v)
        A += w
        edgeCount += 1

if edgeCount == V-1:
    print(A)
