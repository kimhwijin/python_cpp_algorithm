n,m,e = map(int,input().split())
data = [0 for _ in range(100)]
temp = list(map(int,input().split()))
first = temp[0]
end = temp[len(temp)-1]

for i in temp:
    data[i] = 1

result = 0

if e <= first:
    cnt = 0
    i = 0
    while cnt != m:
        cnt += data[i]
        i += 1
    result = i - e - 1
elif e >= end:
    cnt = 0
    i = e
    while cnt != m:
        cnt += data[i]
        i -= 1
    result = i
next = first
cnt = 0
start = first
partend = next
result = 987654321
while partend < end:
    cnt = 0
    start = partend
    while cnt != m:
        cnt += data[next]
        next += 1
    partend = next - 1
    next = partend
    if start <= e and partend >= e:
        if result > partend - start:
            result = partend - start
    elif start < e:
        if result > e - start:
            result = e - start
    elif partend > e:
        if result > partend - e:
            result = partend - e

print(result)