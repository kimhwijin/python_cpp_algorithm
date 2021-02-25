n = int(input())
data = []
for i in range(n):
    data.append(tuple(map(int,input().split())))

adata = sorted(data)
print(adata)
maxcnt = 0
for i in reversed(range(n)):
    cnt = 0
    next = 0

    index = n - i - 1
    end = n - 1
    next = adata[n - i -1][1]
    cnt += 1

    while(next > adata[n - 1][1]):
        flag = False
        start = index
        end = n - 1
        while start < end:
            mid = (start + end) // 2
            if adata[mid][0] == next:
                index = mid
                flag = True
            elif adata[mid][0] < next:
                start = mid + 1
            else:
                end = mid -1
        if flag == False:
            if adata[mid][0] > next:
                index = mid - 1
            elif adata[mid][0] < next:
                index = mid + 1
        next = adata[index][1]
        cnt += 1

    if maxcnt < cnt:
        maxcnt = cnt

print(maxcnt)




