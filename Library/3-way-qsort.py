#20173483 김휘진 4/6 PM 5:14
def Partition(A,l,r):
    if r <= l:
        return
    p = A[l]
    i = l + 1
    j = i
    for k in range(l + 1,r + 1):
        if (A[k] < p):
            t = A[i]
            A[i] = A[k]
            A[k] = t
            i += 1
            j += 1
        elif (A[k] == p):
            t = A[j]
            A[j] = A[k]
            A[k] = t
            j += 1
    t = A[l]
    A[l] = A[i-1]
    A[i-1] = t
    print(l,r,A)
    Partition(A,l,i-2)
    Partition(A,j,r)

def qsort(A,l,r):
    Partition(A,l,r)
    return A

#A = [33,26,28,22,26,38,38,21,23]
A = [3,6,8,2,6,8,8,1,13]
l = 0
r = len(A) - 1
qsort(A,l,r)
