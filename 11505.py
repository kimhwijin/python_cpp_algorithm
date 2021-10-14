'''11505번
제출
맞은 사람
숏코딩
재채점 결과
채점 현황
내 제출
강의
질문 검색
구간 곱 구하기
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	11761	4052	2886	32.758%
문제
어떤 N개의 수가 주어져 있다. 그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 곱을 구하려 한다. 만약에 1, 2, 3, 4, 5 라는 수가 있고, 3번째 수를 6으로 바꾸고 2번째부터 5번째까지 곱을 구하라고 한다면 240을 출력하면 되는 것이다. 그리고 그 상태에서 다섯 번째 수를 2로 바꾸고 3번째부터 5번째까지 곱을 구하라고 한다면 48이 될 것이다.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)과 M(1 ≤ M ≤ 10,000), K(1 ≤ K ≤ 10,000) 가 주어진다. M은 수의 변경이 일어나는 횟수이고, K는 구간의 곱을 구하는 횟수이다. 그리고 둘째 줄부터 N+1번째 줄까지 N개의 수가 주어진다. 그리고 N+2번째 줄부터 N+M+K+1 번째 줄까지 세 개의 정수 a,b,c가 주어지는데, a가 1인 경우 b번째 수를 c로 바꾸고 a가 2인 경우에는 b부터 c까지의 곱을 구하여 출력하면 된다.

입력으로 주어지는 모든 수는 0보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

출력
첫째 줄부터 K줄에 걸쳐 구한 구간의 곱을 1,000,000,007로 나눈 나머지를 출력한다.

예제 입력 1 
5 2 2
1
2
3
4
5
1 3 6
2 2 5
1 5 2
2 3 5
예제 출력 1 
240
48
예제 입력 2 
5 2 2
1
2
3
4
5
1 3 0
2 2 5
1 3 6
2 2 5
예제 출력 2 
0
240
'''
import sys
sys.setrecursionlimit(10**5)

def update(node, start, end, idx, val):
    if start > idx or end < idx:
        return
    if start == end:
        tree[node] = val
        return
    
    mid = (start + end) // 2
    update(node*2, start, mid, idx, val)
    update(node*2+1, mid+1, end, idx, val)
    tree[node] = (tree[node*2] * tree[node*2+1]) % MOD


def query(node, start, end, left, right):
    if start > right or left > end:
        return 1

    if left <= start and end <= right:
        return tree[node] 

    mid = (start + end ) // 2

    return (query(node*2, start, mid, left, right) * query(node*2+1, mid+1, end, left, right)) % MOD


import sys, math
MOD = 1000000007
n, m, k = map(int, sys.stdin.readline().split())
height = int(math.ceil(math.log2(n)))
tree_size = 1 << (height+1)

n_arr = []
cmd = []
tree = [0] * (tree_size + 1)
n_arr.append(0)
for i in range(1, n+1):
    num = int(sys.stdin.readline())
    n_arr.append(num)
    update(1, 1, n, i, num)

for _ in range(m+k):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        n_arr[b] = c
        update(1, 1, n, b, c)
    elif a == 2:
        print(query(1, 1, n, b, c))

