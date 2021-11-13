'''
2213번
제출
맞힌 사람
숏코딩
재채점 결과
채점 현황
내 제출
강의
질문 검색
트리의 독립집합 스페셜 저지
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	3610	1747	1318	49.142%
문제
그래프 G(V, E)에서 정점의 부분 집합 S에 속한 모든 정점쌍이 서로 인접하지 않으면 (정점쌍을 잇는 간선이 없으면) S를 독립 집합(independent set)이라고 한다. 
독립 집합의 크기는 정점에 가중치가 주어져 있지 않을 경우는 독립 집합에 속한 정점의 수를 말하고, 정점에 가중치가 주어져 있으면 독립 집합에 속한 정점의 가중치의 합으로 정의한다. 
독립 집합이 공집합일 때 그 크기는 0이라고 하자. 크기가 최대인 독립 집합을 최대 독립 집합이라고 한다.

문제는 일반적인 그래프가 아니라 트리(연결되어 있고 사이클이 없는 그래프)와 각 정점의 가중치가 양의 정수로 주어져 있을 때, 최대 독립 집합을 구하는 것이다.

입력
첫째 줄에 트리의 정점의 수 n이 주어진다. n은 10,000이하인 양의 정수이다. 1부터 n사이의 정수가 트리의 정점이라고 가정한다. 
둘째 줄에는 n개의 정수 w1, w2, ..., wn이 주어지는데, wi는 정점 i의 가중치이다(1 ≤ i ≤ n). 셋째 줄부터 마지막 줄까지는 간선의 리스트가 주어지는데, 한 줄에 하나의 간선을 나타낸다. 
간선은 정점의 쌍으로 주어진다. 입력되는 정수들 사이에는 빈 칸이 하나 있다. 가중치들의 값은 10,000을 넘지 않는 자연수이다.

출력
첫째 줄에 최대 독립집합의 크기를 출력한다. 둘째 줄에는 최대 독립집합에 속하는 정점을 오름차순으로 출력한다. 최대 독립 집합이 하나 이상일 경우에는 하나만 출력하면 된다.

예제 입력 1 
7
10 30 40 10 20 20 70
1 2
2 3
4 3
4 5
6 2
6 7
예제 출력 1 
140
1 3 5 7
'''
'''
파라미터 설명
n : 트리 노드의 수
edge : 희소 행렬로 edge[i] -> 노드 i 와 연결된 노드의 리스트
weight : 엣지의 가중치 행렬, weight[i] -> 입력된 i 번째 edge의 가중치
path : 최대 가중치를 얻기 위해 지나온 노드
dp : 최대 가중치의 값
dp[i][0] : i번째 노드 자신을 포함한 서브트리 전체의 독립집합 가중치 최대
dp[i][1] : i번째 노드 자신을 제외한 서브트리 전체의 독립집합 가중치 최대

목표 : 트리 처음부터 마지막 노드까지 가중치 최대
방식 : 
- 1번 노트부터 탐색을 시작해서 dfs방식으로 재귀적으로 리프노드까지 도달한다.
- 리프노드에서는 자신을 포함하지 않으면 0, 포함하면 자신의 가중치를 가진다. (초기에 지정해둔 상태)
- 리프노드가 아닌곳에서는 자신과 자식으로 연결된 노드들의 재귀적으로 최대 가중치를 찾아 dp에 지정해둔 상태에서
- 현재 노드를 포함한 경우와 아닌경우를 나누어서 자식 노드들의 dp를 더해가면서 최대값을 저장한다.
- 각 경우에 맞춰서 경로를 추가해준다.
- 이런 방식으로 최상단 1번 노드까지 도달한 후, 최대 가중치 값과 그에맞는 정렬된 경로를 반환한다.

'''


#python 2213.py --test 일 테스트 케이스 수행
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--test', dest='accumulate', action='store_const',
                    const=True, default=False)

args = parser.parse_args()
test = args.accumulate

def print_test_case(n, weight, input_edge):

    print("n : ", n)
    print("weights: ", *weight[1:])
    print("edges : ")
    for a, b in input_edge:
        print(a, b)
    print()


def tree_dfs(start):
    #노드 방문완료
    visit[start] = True

    for node in edge[start]:
        if not visit[node]:
            tree_dfs(node)
            #현재 노드 포함일 때, 자식 노드를 포함하지 않은 가중치 최대값을 더함
            dp[start][0] += dp[node][1]
            #이전 경로를 덧붙여줌
            path[start][0] += path[node][1]

            #현재 노드를 포함하지 않으면, 자식 노드의 포함여부는 상관 없음, 최대값을 찾아 더함
            dp[start][1] += max(dp[node][0], dp[node][1])
            #최대값에 맞는 경로를 더해줌
            path[start][1] += path[node][1] if dp[node][0] < dp[node][1] else path[node][0]

#데이터 입력
if not test:
    import sys
    input = sys.stdin.readline
    n = int(input())
    weight = [0] + list(map(int, input().split()))
    edge = [[] for _ in range(n + 1)]
    dp = [[weight[i], 0] for i in range(n + 1)]
    visit = [False for _ in range(n + 1)]
    path = [[[i], []] for i in range(n + 1)]

    for i in range(n - 1):
        a, b = map(int, input().split())
        edge[a].append(b)
        edge[b].append(a)
    
    edge[0].append(1)
    tree_dfs(0)
    print(dp[0][1])
    path[0][1].sort()
    print(*path[0][1])

#테스트 케이스 수행
else:
    import random
    random.seed(42)

    iter_n = [random.randrange(7, 90) for _ in range(5)]
    iter_weight = []
    iter_edge = []
    for i in iter_n:
        iter_weight.append([0] + [random.randrange(1,6) for _ in range(i)])
        temp_edges = []
        for j in range(i-1):
            while True:
                a = j
                b = random.randrange(1, i+1)
                if a != b:
                    if not [a,b] in temp_edges:
                        temp_edges.append([a,b])
                        break
        iter_edge.append(temp_edges)
    

    for i, [n, weight, input_edge] in enumerate(zip(iter_n, iter_weight, iter_edge)):
        print();print("test",i+1, "-"*30)
        print_test_case(n, weight, input_edge)
        edge = [[] for _ in range(n + 1)]
        dp = [[weight[i], 0] for i in range(n + 1)]
        visit = [False for _ in range(n + 1)]
        path = [[[i], []] for i in range(n + 1)]
        for a, b in input_edge:
            edge[a].append(b)
            edge[b].append(a)

        edge[0].append(1)
        tree_dfs(0)
        print(dp[0][1])
        path[0][1].sort()
        print(*path[0][1])


