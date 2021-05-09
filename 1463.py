n = int(input())

cnt = [0 for i in range(n + 1)]
if n < 4:
    if n == 1:
        print(0)
    else:
        print(1)
    exit(0)
cnt[1] = 0
cnt[2] = 1
cnt[3] = 1

for i in range(4, n+1):
    minval = i
    if i % 3 == 0:
        if minval > cnt[int(i/3)] + 1:
            minval = cnt[int(i/3)] + 1
    if i % 2 == 0:
        if minval > cnt[int(i/2)] + 1:
            minval = cnt[int(i/2)] + 1
    if cnt[i-1] + 1 < minval:
        minval = cnt[i-1] + 1
    if cnt[i-2] + 2 < minval:
        minval = cnt[i-2] + 2
    cnt[i] = minval

print(cnt[n])