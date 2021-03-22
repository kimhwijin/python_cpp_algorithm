'''
10830번
제출
맞은 사람
숏코딩
재채점
채점 현황
내 제출
강의
질문 검색
행렬 제곱 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	9751	3342	2704	34.276%
문제
크기가 N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하시오. 수가 매우 커질 수 있으니, 
A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.

입력
첫째 줄에 행렬의 크기 N과 B가 주어진다. (2 ≤ N ≤  5, 1 ≤ B ≤ 100,000,000,000)

둘째 줄부터 N개의 줄에 행렬의 각 원소가 주어진다. 행렬의 각 원소는 1,000보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄부터 N개의 줄에 걸쳐 행렬 A를 B제곱한 결과를 출력한다.

예제 입력 1 
2 5
1 2
3 4
예제 출력 1 
69 558
337 406
예제 입력 2 
3 3
1 2 3
4 5 6
7 8 9
예제 출력 2 
468 576 684
62 305 548
656 34 412
예제 입력 3 
5 10
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
예제 출력 3 
512 0 0 0 512
512 0 0 0 512
512 0 0 0 512
512 0 0 0 512
512 0 0 0 512
'''
'''
a1 b1 c1
a2 b2 c2
a3 b3 c3

a1 = (a1a1 + b1a2 + c1a3)

'''
def mat_mul(mat1,mat2,shape):
    resultmat = [[0] * shape for _ in range(shape)]
    for i in range(shape):
        for j in range(shape):
            for k in range(shape):
                resultmat[i][j] += (mat1[i][k] * mat2[k][j])
            resultmat[i][j] %= 1000
    return resultmat
'''
def mat_add(mat1,mat2,shape):
    resultmat = [[0] * shape for _ in range(shape)]
    for i in range(shape):
        for j in range(shape):
            resultmat[i][j] = (mat1[i][j] + mat2[i][j]) % 1000
    return resultmat
'''
n , b = map(int,input().split())
B = bin(b)[2:]
matrix = [list(map(int,input().split())) for _ in range(n)]
result = [[1 if i == j else 0 for i in range(n)] for j in range(n)]

for i in range(len(B)):
    if B[-i-1] == '1':
        result = mat_mul(result,matrix, n)
    matrix = mat_mul(matrix,matrix,n)
for row in result:
    print(*row)

