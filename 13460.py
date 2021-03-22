n , m = map(int,input().split())
if n * m <= 12:
    result = -1
    exit(0)

graph = []
for _ in range(n):
    graph.append(list(input()))

red = []
blue = []
goal = []   
for nn in range(n):
    for mm in range(m):
        if graph[nn][mm] == 'R':
            red = [nn,mm]
        elif graph[nn][mm] == 'B':
            blue = [nn,mm]
        elif graph[nn][mm] == 'O':
            goal = [nn,mm]



def checkdir(ppos):
    redpos = []
    pos = ppos
    #up
    if graph[ppos[0] - 1][ppos[1]] != '#':
        nn = ppos[0]
        mm = ppos[1]
        rb = 0
        while True:
            if graph[nn - 1][mm] == '#':
                break
            elif graph[nn - 1][mm] == 'R' or graph[nn -1][mm] == 'B':
                rb = 1
            elif graph[nn -1][mm] == 'O':
                nn = -1
                mm = -1
                rb = 0
                break
            nn -= 1
        pos = [nn + rb,mm]

    redpos.append(pos)
    pos = ppos
    #left
    if graph[ppos[0]][ppos[1] - 1] != '#':
        nn = ppos[0]
        mm = ppos[1]
        rb = 0
        while True:
            if graph[nn][mm - 1] == '#':
                break
            elif graph[nn][mm - 1] == 'R' or graph[nn][mm - 1] == 'B':
                rb = 1
            elif graph[nn][mm - 1] == 'O':
                nn = -1
                mm = -1
                rb = 0
                break
            mm -= 1
        pos = [nn,mm + rb]
    redpos.append(pos)    
    pos = ppos 

    #down
    if graph[ppos[0] + 1][ppos[1]] != '#':
        nn = ppos[0]
        mm = ppos[1]
        rb = 0
        while True:
            if graph[nn + 1][mm] == '#':
                    break
            elif graph[nn + 1][mm] == 'R' or graph[nn + 1][mm] == 'B' :
                rb = -1  
            elif graph[nn + 1][mm] == 'O':
                nn = -1
                mm = -1
                rb = 0
                break
            nn += 1
        pos = [nn + rb,mm]
    redpos.append(pos) 

    pos = red
    #right
    if graph[ppos[0]][ppos[1] + 1] != '#':
        nn = ppos[0]
        mm = ppos[1]
        rb = 0
        while True:
            if graph[nn][mm + 1] == '#':
                break
            elif graph[nn][mm + 1] == 'R' or graph[nn][mm + 1] == 'B' :
                rb = -1  
            elif graph[nn][mm + 1] == 'O':
                nn = -1
                mm = -1
                rb = 0
                break
            mm += 1
        pos = [nn,mm + rb]

    redpos.append(pos) 
    return redpos

def checkvisited(key):
    for skey in visited:
        if skey == key:
            return visited[skey]
    return -1





cnt = 0
visited = {}


cur = [red,blue]
nextt = []
nextt.append(checkdir(red))
nextt.append(checkdir(blue))
key = str(red[0]) + str(red[1]) + str(blue[0]) + str(blue[1])
from collections import deque
visited = {key:cnt}
stackdir  = deque()
stackdir.append(cur)
result = -1

while stackdir:

    graph[red[0]][red[1]] = '.'
    graph[blue[0]][blue[1]] = '.'
    cur = stackdir.popleft()
    red = cur[0]
    blue = cur[1]
    graph[red[0]][red[1]] = 'R'
    graph[blue[0]][blue[1]] = 'B'
    nextt = []
    nextt.append(checkdir(red))
    nextt.append(checkdir(blue))

    for nredpos,nbluepos in zip(nextt[0] , nextt[1]):
        if nbluepos == [-1,-1]:
            continue
        elif nredpos == [-1,-1]:
            if result == -1 or result > checkvisited(curkey) + 1:
                result = checkvisited(curkey) + 1
                continue

        key = str(nredpos[0]) + str(nredpos[1]) + str(nbluepos[0]) + str(nbluepos[1])
        curkey = str(cur[0][0]) + str(cur[0][1]) + str(cur[1][0]) + str(cur[1][1])
        if key != curkey:

            curcnt = checkvisited(curkey)
            cnt = checkvisited(key)
            if cnt == -1:
                stackdir.append([nredpos,nbluepos])
                visited[key] = curcnt + 1
            elif cnt > curcnt + 1:
                stackdir.append([nredpos,nbluepos])
                visited[key] = curcnt + 1
        

if result > 10:
    result = -1
print(result)
    

    


