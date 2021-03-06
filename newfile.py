skill = list(input().split())

n = int(input())

link = {}
for _ in range(n):
    first ,end = map(str,input().split())
    if not link.get(first):
        link[first] = [end]
    else:
        link[first].append(end)

link_value = link.values()
for key in link:
    printstr = ''

    for link_val in link_value:
        if key in link_value:
            continue
    printstr = key
    while True:
        print(1)
    for valuelist in link[key]:

        for value in valuelist:
            if not link.get(value):

print(link)