'''
11401번
제출
맞은 사람
숏코딩
재채점
채점 현황
내 제출
강의
질문 검색
이항 계수 3 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	10076	3959	2831	44.604%
문제
자연수 과 정수 가 주어졌을 때 이항 계수 
를 1,000,000,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 과 가 주어진다. (1 ≤  ≤ 4,000,000, 0 ≤  ≤ )

출력
 
를 1,000,000,007로 나눈 나머지를 출력한다.

예제 입력 1 
5 2
예제 출력 1 
10
'''
import sys

MOD = 1000000007

def power(x, y):
    ans = 1
    while y > 0:
        if y % 2 == 1:
            ans = (ans*x) % MOD
        x = (x*x) % MOD
        y //= 2
    return ans


def fac(n):
    ans = 1
    for i in range(2, n+1):
        ans = (ans*i) % MOD
    return ans



n, k = map(int, input().split())
if n == k or k == 0:
    print(1)
    exit(0)


a, b, c = fac(n), fac(k), fac(n-k)

print((a*power(b*c, MOD-2)) % MOD)







