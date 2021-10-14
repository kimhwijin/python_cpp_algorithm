'''
17404번
제출
맞은 사람
숏코딩
재채점 결과
채점 현황
내 제출
강의
질문 검색
RGB거리 2
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
0.5 초 (추가 시간 없음)	128 MB	4590	2472	2036	53.948%
문제
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.
입력
첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.

예제 입력 1 
3
26 40 83
49 60 57
13 89 99
예제 출력 1 
110
'''

def sort_cost_arg(i_cost):
    print(i_cost)
    return sorted(range(len(i_cost)), key=lambda k: i_cost[k])

import sys


n = int(sys.stdin.readline())
rgb_cost = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

min_n = [987654321 for _ in range(n+1)]
RED = 0
GREEN = 1
BLUE = 2
color_n = [-1 for _ in range(n+1)]

i = 0
    
min_arg = sort_cost_arg(rgb_cost[i])
print(min_arg)
#color_n[i+1] = min_color
#min_n[i+1] = rgb_cost[i][min_color]

    