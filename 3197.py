
'''
백조의 호수 출처다국어분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	10885	2259	1285	18.905%
문제
두 마리의 백조가 호수에서 살고 있었다. 그렇지만 두 마리는 호수를 덮고 있는 빙판으로 만나지 못한다.

호수는 행이 R개, 열이 C개인 직사각형 모양이다. 어떤 칸은 얼음으로 덮여있다.

호수는 차례로 녹는데, 매일 물 공간과 접촉한 모든 빙판 공간은 녹는다. 두 개의 공간이 접촉하려면 가로나 세로로 닿아 있는 것만 (대각선은 고려하지 않는다) 생각한다.

아래에는 세 가지 예가 있다.

...XXXXXX..XX.XXX ....XXXX.......XX .....XX.......... 
....XXXXXXXXX.XXX .....XXXX..X..... ......X.......... 
...XXXXXXXXXXXX.. ....XXX..XXXX.... .....X.....X..... 
..XXXXX..XXXXXX.. ...XXX....XXXX... ....X......XX.... 
.XXXXXX..XXXXXX.. ..XXXX....XXXX... ...XX......XX.... 
XXXXXXX...XXXX... ..XXXX.....XX.... ....X............ 
..XXXXX...XXX.... ....XX.....X..... ................. 
....XXXXX.XXX.... .....XX....X..... ................. 
      처음               첫째 날             둘째 날
백조는 오직 물 공간에서 세로나 가로로만(대각선은 제외한다) 움직일 수 있다.

며칠이 지나야 백조들이 만날 수 있는 지 계산하는 프로그램을 작성하시오.

입력
입력의 첫째 줄에는 R과 C가 주어진다. 단, 1 ≤ R, C ≤ 1500.

다음 R개의 줄에는 각각 길이 C의 문자열이 하나씩 주어진다. '.'은 물 공간, 'X'는 빙판 공간, 'L'은 백조가 있는 공간으로 나타낸다.

출력
첫째 줄에 문제에서 주어진 걸리는 날을 출력한다.

예제 입력 1 
8 17
...XXXXXX..XX.XXX
....XXXXXXXXX.XXX
...XXXXXXXXXXXX..
..XXXXX.LXXXXXX..
.XXXXXX..XXXXXX..
XXXXXXX...XXXX...
..XXXXX...XXX....
....XXXXX.XXXL...
예제 출력 1 
2
'''

import sys
r, c = map(int, sys.stdin.readline().split())
data = []

for _ in range(r):
    data.append(list(str(sys.stdin.readline().strip())))


from collections import deque
dirc = [(-1,0),(0,-1),(1,0),(0,1)] #up left down right
    
queue = deque()
water = deque()
for pos_r in range(r):
    for pos_c in range(c):
        if data[pos_r][pos_c] == 'L':
            queue.append((pos_r, pos_c))
            water.append((pos_r, pos_c))
        elif data[pos_r][pos_c] == '.':
            water.append((pos_r, pos_c))

daycnt = 1
endpos = queue.pop()
'''
temp = deque()
    while water:
        x, y = water.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C:
                if lake[nx][ny] == 'X':
                    lake[nx][ny] = '.'
                    temp.append((nx, ny))
    return temp
'''
while True:
    if True:
        nextday_water = deque()
        while water:
            pos_r,pos_c = water.popleft()
            for dir_r, dir_c in dirc:
                if 0 <= pos_r + dir_r < r and 0 <= pos_c + dir_c < c:
                    if data[pos_r + dir_r][pos_c + dir_c] == 'X':
                        data[pos_r + dir_r][pos_c + dir_c] = '.'
                        nextday_water.append((pos_r + dir_r, pos_c + dir_c))
        water = nextday_water

    if True:
        nextday = deque()
        while queue:
            pos_r , pos_c = queue.popleft()

            if data[pos_r][pos_c] != 'L':
                data[pos_r][pos_c] = 'C'
            for dir_r , dir_c in dirc:
                if 0 <= pos_r + dir_r < r and 0 <= pos_c + dir_c < c:
                    if endpos[0] == pos_r + dir_r and endpos[1] == pos_c + dir_c:
                        queue = 0
                        break
                    if data[pos_r + dir_r][pos_c + dir_c] == '.':
                        #계속 탐색
                        queue.append((pos_r + dir_r,pos_c + dir_c))
                        #탐색한 부분 처리
                        data[pos_r + dir_r][pos_c + dir_c] = 'C'
                    elif data[pos_r + dir_r][pos_c + dir_c] == 'X':
                        #다음날 탐색 큐
                        nextday.append((pos_r + dir_r,pos_c + dir_c))
        queue = nextday
        
    if queue == 0:
        print(daycnt)
        break

    queue = nextday
    daycnt += 1
    
