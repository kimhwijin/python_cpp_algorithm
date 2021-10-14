'''
14002번
제출
맞은 사람
숏코딩
재채점 결과
채점 현황
내 제출
강의
질문 검색
가장 긴 증가하는 부분 수열 4 스페셜 저지
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	16645	6442	4882	39.295%
문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

둘째 줄에는 가장 긴 증가하는 부분 수열을 출력한다. 그러한 수열이 여러가지인 경우 아무거나 출력한다.

예제 입력 1 
6
10 20 10 30 20 50
예제 출력 1 
4
10 20 30 50
'''
import sys
n = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)

j = 1
max_dp = max(dp)
j = max_dp
ans = []
print(max_dp)
for i in reversed(range(n)):
    if dp[i] == j:
        ans.append(A[i])
        j -= 1

for i in ans[::-1]:
    print(i, end=' ')
print()
