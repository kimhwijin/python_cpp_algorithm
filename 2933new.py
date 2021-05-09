#dfs 로 클러스터찾기
'''
2933번
제출
맞은 사람
숏코딩
재채점
채점 현황
내 제출
강의
질문 검색
미네랄 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	6680	1776	1108	24.176%
문제
창영과 상근은 한 동굴을 놓고 소유권을 주장하고 있다. 
두 사람은 막대기를 서로에게 던지는 방법을 이용해 누구의 소유인지를 결정하기로 했다. 
싸움은 동굴에서 벌어진다. 동굴에는 미네랄이 저장되어 있으며, 던진 막대기가 미네랄을 파괴할 수도 있다.

동굴은 R행 C열로 나타낼 수 있으며, R×C칸으로 이루어져 있다. 
각 칸은 비어있거나 미네랄을 포함하고 있으며, 네 방향 중 하나로 인접한 미네랄이 포함된 두 칸은 같은 클러스터이다.

창영은 동굴의 왼쪽에 서있고, 상근은 오른쪽에 서있다. 
두 사람은 턴을 번갈아가며 막대기를 던진다. 막대를 던지기 전에 던질 높이를 정해야 한다. 
막대는 땅과 수평을 이루며 날아간다.

막대가 날아가다가 미네랄을 만나면, 그 칸에 있는 미네랄은 모두 파괴되고 막대는 그 자리에서 이동을 멈춘다.

미네랄이 파괴된 이후에 남은 클러스터가 분리될 수도 있다. 
새롭게 생성된 클러스터가 떠 있는 경우에는 중력에 의해서 바닥으로 떨어지게 된다. 
떨어지는 동안 클러스터의 모양은 변하지 않는다. 클러스터는 다른 클러스터나 땅을 만나기 전까지 게속해서 떨어진다. 
클러스터는 다른 클러스터 위에 떨어질 수 있고, 그 이후에는 합쳐지게 된다.

동굴에 있는 미네랄의 모양과 두 사람이 던진 막대의 높이가 주어진다. 
모든 막대를 던지고 난 이후에 미네랄 모양을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 동굴의 크기 R과 C가 주어진다. (1 ≤ R,C ≤ 100)

다음 R개 줄에는 C개의 문자가 주어지며, '.'는 빈 칸, 'x'는 미네랄을 나타낸다.

다음 줄에는 막대를 던진 횟수 N이 주어진다. (1 ≤ N ≤ 100)

마지막 줄에는 막대를 던진 높이가 주어지며, 공백으로 구분되어져 있다. 모든 높이는 1과 R사이이며, 높이 1은 행렬의 가장 바닥, R은 가장 위를 의미한다. 
첫 번째 막대는 왼쪽에서 오른쪽으로 던졌으며, 두 번째는 오른쪽에서 왼쪽으로, 이와 같은 식으로 번갈아가며 던진다.

공중에 떠 있는 미네랄 클러스터는 없으며, 두 개 또는 그 이상의 클러스터가 동시에 떨어지는 경우도 없다. 
클러스터가 떨어질 때, 그 클러스터 각 열의 맨 아래 부분 중 하나가 바닥 또는 미네랄 위로 떨어지는 입력만 주어진다.

출력
입력 형식과 같은 형식으로 미네랄 모양을 출력한다.

예제 입력 1 
8 8
........
........
...x.xx.
...xxx..
..xxx...
..x.xxx.
..x...x.
.xxx..x.
5
6 6 4 3 1

예제 출력 1 
........
........
........
........
.....x..
..xxxx..
..xxx.x.
..xxxxx.

'''
import sys
sys.setrecursionlimit(10**6)

r , c = map(int,input().split())
donggool = [' ' for _ in range(r)]
for i in reversed(range(r)):
    donggool[i] = str(input())

visited = [[False] * c for _ in range(r)]

flag = [False]

stick_cnt = int(input())
stick = list(map(int,input().split()))
move = [(1,0),(-1,0),(0,1),(0,-1)]

from collections import deque
queue = deque()

def putString(y,x,s):
    donggool[y] = donggool[y][:x] + s +  donggool[y][x + 1:]

def dfs(y,x):
    if y == 0: #바닥에 닿음
        flag[0] = True
        return

    for dx , dy in move:
        ny = y + dy
        nx = x + dx
        if nx < 0 or nx >= c or ny < 0 or ny >= r:
            continue
        if donggool[ny][nx] == '.' or visited[ny][nx] == True:
            continue
        visited[ny][nx] = True
        queue.append((ny,nx))
        dfs(ny,nx)
    


for st in range(stick_cnt):
    y = stick[st] - 1
    x = -1
    if st % 2 == 0:
        for i in range(c):
            if donggool[y][i] == 'x':
                x = i
                break
    else:
        for i in reversed(range(c)):
            if donggool[y][i] == 'x':
                x = i
                break
    if x == -1:
        continue
    putString(y,x,'.')
    #donggool[y][x] = '.'

    for delta_x , delta_y in move:
        nextY = y + delta_y
        nextX = x + delta_x
        if nextY < 0 or nextY >= r or nextX < 0 or nextX >= c:
            continue
        if donggool[nextY][nextX] == '.':
            continue

        queue = deque()
        visited = [[False] * c for _ in range(r)]
        visited[nextY][nextX] = True
        flag[0] = False

        queue.append((nextY,nextX))
        dfs(nextY,nextX)
        if flag[0] == True:
            continue
        while(1):
            down = True
            for i in range(len(queue)):
                putString(queue[i][0],queue[i][1],'.')
                #donggool[queue[i][0]][queue[i][1]] = '.'
            for i in range(len(queue)):
                ndy = queue[i][0] - 1
                ndx = queue[i][1]
                if ndy < 0 or donggool[ndy][ndx] == 'x':
                    down = False
                    break
            
            for i in range(len(queue)):
                if down == True:
                    queue[i] = (queue[i][0] - 1, queue[i][1])
                putString(queue[i][0],queue[i][1],'x')
                #donggool[queue[i][0]][queue[i][1]] = 'x'
            if down == False:
                break

for row in reversed(range(r)):
    print(donggool[row])