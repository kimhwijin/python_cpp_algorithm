#보류
coocnt = int(input())
coolist = list(map(int,input().split()))
goocnt = int(input())
goolist = list(map(int,input().split()))

from itertools import cominations

cnt = ['N' for _ in range(40001)]
for i in range(coocnt):
    cnt[coolist[i]] = 'Y'

for i in range(1,coocnt + 1):
    combi = list(combinations(coolist,i))
    for tu in combi:
        for weight in tu:
            for weight1 in weight:
                if len(weight) == 1:
                    cnt[weight1] = 'Y'
    for j in range(i+1,coocnt):
        cnt[coolist[j] + coolist[i]] = 'Y'
        cnt[coolist[j] - coolist[i]] = 'Y'





for i in range(goocnt):
    print(cnt[goolist[i]],end=' ')