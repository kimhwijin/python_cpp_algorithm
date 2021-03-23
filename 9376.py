'''

9376번
제출
맞은 사람
숏코딩
재채점
채점 현황
내 제출
강의
질문 검색
탈옥 출처다국어분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	5939	730	517	24.584%
문제
상근이는 감옥에서 죄수 두 명을 탈옥시켜야 한다. 이 감옥은 1층짜리 건물이고, 상근이는 방금 평면도를 얻었다.

평면도에는 모든 벽과 문이 나타나있고, 탈옥시켜야 하는 죄수의 위치도 나타나 있다. 감옥은 무인 감옥으로 죄수 두 명이 감옥에 있는 유일한 사람이다.

문은 중앙 제어실에서만 열 수 있다. 상근이는 특별한 기술을 이용해 제어실을 통하지 않고 문을 열려고 한다. 하지만, 문을 열려면 시간이 매우 많이 걸린다. 두 죄수를 탈옥시키기 위해서 열어야 하는 문의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스의 수는 100개를 넘지 않는다.

첫째 줄에는 평면도의 높이 h와 너비 w가 주어진다. (2 ≤ h, w ≤ 100) 다음 h개 줄에는 감옥의 평면도 정보가 주어지며, 빈 공간은 '.', 지나갈 수 없는 벽은 '*', 문은 '#', 죄수의 위치는 '$'이다.

상근이는 감옥 밖을 자유롭게 이동할 수 있고, 평면도에 표시된 죄수의 수는 항상 두 명이다. 각 죄수와 감옥의 바깥을 연결하는 경로가 항상 존재하는 경우만 입력으로 주어진다.

출력
각 테스트 케이스마다 두 죄수를 탈옥시키기 위해서 열어야 하는 문의 최솟값을 출력한다.

예제 입력 1 
3
5 9
****#****
*..#.#..*
****.****
*$#.#.#$*
*********
5 11
*#*********
*$*...*...*
*$*.*.*.*.*
*...*...*.*
*********.*
9 9
*#**#**#*
*#**#**#*
*#**#**#*
*#**.**#*
*#*#.#*#*
*$##*##$*
*#*****#*
*.#.#.#.*
*********
예제 출력 1 
4
0
9
'''
import sys
t = int(sys.stdin.readline())

move = [[1,0],[0,-1],[-1,0],[0,1]]
def dfs(data,visited,outdoor,row,col):
    ploc = []
    pcnt = 0
    print("ouutdoor : ", outdoor)
    print("data : ", data)
    while outdoor:
        stack = []
        stack.append(outdoor.pop())
        while stack:
            y, x = stack.pop()
            for i in range(4):
                ny = y + move[i][0]
                nx = x + move[i][1]
                if ny >= row-1 or ny == 0 or nx >= col-1 or nx == 0:
                    continue
                if data[ny][nx] == '*':
                    continue
                if data[ny][nx] == '#': 
                    if visited[ny][nx] > visited[y][x] + 1:
                        visited[ny][nx] = visited[y][x] + 1
                        stack.append((ny,nx))
                elif data[ny][nx] == '.': 
                    if visited[ny][nx] > visited[y][x]:
                        visited[ny][nx] = visited[y][x]
                        stack.append((ny,nx))
                elif data[ny][nx] == '$':
                    if visited[ny][nx] == 12345678:
                        pcnt += 1
                        ploc.append((ny,nx))
                    if visited[ny][nx] > visited[y][x]:
                        visited[ny][nx] = visited[y][x]
                        stack.append((ny,nx))
    print("visited : ")
    for row1 in visited:
        print(row1)
        

            
for _ in range(t):
    data = []
    visited = []
    outdoor = []
    row,col = map(int,sys.stdin.readline().split())
    for r in range(row):
        data.append(str(sys.stdin.readline().strip()))
        visited.append([12345678] * col)
    for c in range(col):
        if data[0][c] == '#':
            outdoor.append((0,c))
            visited[0][c] = 1
        elif data[0][c] == '.':
            outdoor.append((0,c))
        elif data[row-1][c] == '#':
            outdoor.append((row-1,c))
            visited[row-1][c] = 1
        elif data[row-1][c] == '.':
            outdoor.append((row-1,c))

    for r in range(1,row-1):
        if data[r][0] == '#':
            visited[r][0] = 1
            outdoor.append((r,0))
        elif data[r][0] == '.':
            outdoor.append((r,0))
        elif data[r][col-1] == '#':
            visited[r][col-1] = 1
            outdoor.append((r,col-1))
        elif data[r][col-1] == '.':
            outdoor.append((r,col-1))
    
    dfs(data,visited,outdoor,row,col)

