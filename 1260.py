def dfs(x):

    stack.append(x)
    visited[x] = True
    print(x, end=' ')
    for aline in line:
        if aline[0] == x:
            if visited[aline[1]] == False:
                dfs(aline[1])
        elif aline[1] == x:
            if visited[aline[0]] == False:
                dfs(aline[0])

from collections import deque

def bfs(start):
    queue = deque([start])

    while queue:
        nn = queue.popleft()
        print(nn, end=' ')
        visited[nn] = True
        for aline in line:
            if aline[0] == nn:
                if visited[aline[1]] == False:
                    visited[aline[1]] = True
                    queue.append(aline[1])
            elif aline[1] == nn:
                if visited[aline[0]] == False:
                    visited[aline[0]] = True
                    queue.append(aline[0])




n , m , v = map(int,input().split())

stack = []
line = []
for _ in range(m):
    line.append(list(map(int,input().split())))

for a in range(m):
    if line[a][0] > line[a][1]:
        temp = line[a][0]
        line[a][0] = line[a][1]
        line[a][1] = temp

line.sort()
visited = [False for _ in range(n + 1)]
dfs(v)
print("")
visited = [False for _ in range(n + 1)]
bfs(v)