def merge(A, p, q, r):
    global Total
    B = []
    i = p
    j = q+1
    while i <= q and j <= r:
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            Total += len(A[i:q+1])
            B.append(A[j])
            j += 1
    A[p:r+1] = B + A[i:q+1] + A[j:r+1]

def mergesort(A, p, r):
    # complete the body of this function
    if p < r:
        q = (p+r)//2
        mergesort(A, p,q)
        mergesort(A, q+1,r)
        merge(A, p, q, r)



a = list(map(int, input().split()))
n = len(a)
count = 0
Total = 0
'''
# bruteforce

for i in range(n-1):
    for j in range(i+1, n):
        if a[j] < a[i]:
            count +=1
'''
mergesort(a, 0, len(a)-1)
print(Total)
