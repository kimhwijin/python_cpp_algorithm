cnt = int(input())
nlist = []
for _ in range(cnt):
    nlist.append(int(input()))

n = [[] for _ in range(65)]
n[2] = [10,9,8,7,6,5,4,3,2,1]
for i in range(3,65):
    n[i] = []
    for j in range(10):
        sum = 0
        for a in n[i - 1][j:]:
            sum += a
        n[i].append(sum)


for c in range(cnt):
    result = 0
    if nlist[c] == 1:
        print(0)
        continue
    for j in n[nlist[c]]:
        result += j
    print(result)
