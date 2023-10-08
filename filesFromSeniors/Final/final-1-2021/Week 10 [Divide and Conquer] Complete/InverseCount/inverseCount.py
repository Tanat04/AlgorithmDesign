def merge(A, p, q, r):
    B = []
    i = p
    j = q+1
    inverseCount = 0

    while i <= q and j <= r:
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            inverseCount += (q-i + 1)
            B.append(A[j])
            j += 1
    A[p:r+1] = B + A[i:q+1] + A[j:r+1]

    return inverseCount

def mergesort(A, p, r):
    inverseCount = 0

    if p < r:
        q = (p+r)//2
        inverseCount += mergesort(A, p,q)
        inverseCount += mergesort(A, q+1,r)
        inverseCount += merge(A, p, q, r)
    return inverseCount


t = int(input())
testCase = [[] for i in range(t)]
ansList = []
space = input()
for tnum in range(t):
    nCase = int(input())
    for num in range(nCase+1):
        number = input()
        if len(number) > 0:
            testCase[tnum].append(int(number))
        else:
            break
    
    n = len(testCase[tnum])
    Total = mergesort(testCase[tnum], 0, len(testCase[tnum])-1)
    ansList.append(Total)

for ans in ansList:
    print(ans)

