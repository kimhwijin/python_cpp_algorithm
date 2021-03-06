pc, n, h = map(int,input().split())

pclist = [[] for _ in range(pc + 1)]

for _ in range(n):
    i , value = map(int,input().split())
    pclist[i].append(value)
for i in range(1,pc+1):
    pclist[i].sort()

resultlist = [0 for _ in range(h+ 1)]

print(pclist)
for i in range(1, pc+1):
    price = 0
    for hour in pclist[i]:
        if hour > h:
            break
        resultlist[hour] = hour
    for hour in pclist[i]:
        if hour > h:
            break
        for hour1 in pclist[i][pclist[i].index(hour)+1:]:
            if hour + hour1 > h:
                break
            resultlist[hour + hour1] = (hour + hour1) * 1000
    res = 0
    for result in resultlist:
        if result > res:
            res = result
    print(i,res)
