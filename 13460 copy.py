from sys import stdin
from collections import deque

input = stdin.readline
n, m = map(int,input().split())

board = [list(input().strip()) for _ in range(n)]
q = deque()
visited_r = [[0]*m for _ in range(n)]
visited_b = [[0]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def init():
    rx,ry,bx,by = [0]*4
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                rx, ry = i,j
            elif board[i][j] == 'B':
                bx, by = i,j
    q.append((rx,ry,bx,by,1))
    visited_r[rx][ry] = 1
    visited_b[bx][by] = 1

def move(x,y,dx,dy):
    count = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x,y,count

def bfs():
    init()
    while q:
        rx,ry,bx,by,depth = q.popleft()
        if depth > 10:
            break
        for i in range(4): #4방향 돌리기
            nrx, nry, count_r = move(rx, ry, dx[i], dy[i])
            nbx, nby, count_b = move(bx, by, dx[i], dy[i])
            if board[nbx][nby] == 'O':
                continue
            if board[nrx][nry] == 'O':
                return print(depth)
            if nrx == nbx and nry == nby:
                if count_r>count_b:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            if not visited_r[nrx][nry] or not visited_b[nbx][nby]:
                q.append((nrx,nry,nbx,nby,depth+1))
                visited_r[nrx][nry] = 1
                visited_b[nbx][nby] = 1
    return print(-1)

bfs()