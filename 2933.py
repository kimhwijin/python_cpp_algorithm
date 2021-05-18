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



====================
........
........
........
........
.....x..
..xxxx..
..xxx.x.
..xxxxx.

'''
r , c = map(int,input().split())
donggool = [' ' for _ in range(r)]
for i in reversed(range(r)):
    donggool[i] = str(input())

stick_cnt = int(input())
stick = list(map(int,input().split()))

def check_blow(height):
    a = []
    for i in range(c):

        if donggool[height][i] == donggool[height-1][i]:
            if donggool[height][i] == '.':
                a.append(0)
            else:
                a.append(-1)
        else:
            if donggool[height][i] == 'x' and donggool[height - 1][i] == '.':
                a.append(1)
            else:
                a.append(0)
    return a

def break_min(height,dir):
    if dir == 'l':
        ls = range(c)
    else:
        ls = reversed(range(c))

    for i in ls:
        if donggool[height][i] == 'x':
            donggool[height] = donggool[height][:i] + '.' + donggool[height][i+1:]
            return

def first_collapse_block(check,height):
    start = -1
    end = -1
    i = 0
    first1 = False
    end1 = False
    if height == 0:
        return False
    while (i < c):
        if check[i] == 1 and start == -1:
            if i == 0:
                first1 = True
            elif check[start - 1] == 0:
                first1 = True
            start = i

            if first1 == True: #왼쪽 연결 x
                
                while(check[i] == 1):
                    i += 1
                    if i == c:
                        end1 = True
                        break
                    elif check[i] == 0:
                        end1 = True
                        break
                if end1 == True: #오른쪽연걸 x
                    end = i
                    donggool[height-1] = donggool[height-1][:start] + donggool[height][start:end] + donggool[height-1][end:]
                    a = '.' * (end - start)
                    donggool[height] = donggool[height][:start] + a + donggool[height][end:]
                    height -= 1
                    while(height > 0):
                        if collapse_block(height,start,end) == False:
                            break
                        height -= 1
                    return True
        i += 1
    return False

def collapse_block(height,start,end):
    a = '.' * (end - start)
    if donggool[height-1][start:end] == a:
        donggool[height-1] = donggool[height-1][:start] + donggool[height][start:end] + donggool[height-1][end:]
        donggool[height] = donggool[height][:start] + a + donggool[height][end:]
        return True
    return False


for s in range(stick_cnt):
    _height = stick[s] - 1
    if s % 2 == 0:
        break_min(_height,'l')
    else:
        break_min(_height,'r')

    if _height != 0: #부순층 collapse
        rel_value = check_blow(_height)
        first_collapse_block(rel_value, _height)
    _height += 1
    while(_height < r):
        rel_value = check_blow(_height)
        if first_collapse_block(rel_value, _height) == False:
            break
        _height += 1 
    print(1123123)
    for row in reversed(range(r)):
        print(donggool[row])
for row in reversed(range(r)):
    print(donggool[row])
