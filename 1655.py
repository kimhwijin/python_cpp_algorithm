'''
가운데를 말해요 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
0.1 초 (하단 참고)	128 MB	15680	4487	3486	32.179%
문제
수빈이는 동생에게 "가운데를 말해요" 게임을 가르쳐주고 있다. 수빈이가 정수를 하나씩 외칠때마다 동생은 지금까지 수빈이가 말한 수 중에서 중간값을 말해야 한다. 
만약, 그동안 수빈이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.

예를 들어 수빈이가 동생에게 1, 5, 2, 10, -99, 7, 5를 순서대로 외쳤다고 하면, 동생은 1, 1, 2, 2, 2, 2, 5를 차례대로 말해야 한다. 수빈이가 외치는 수가 주어졌을 때, 
동생이 말해야 하는 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 수빈이가 외치는 정수의 개수 N이 주어진다. N은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수이다. 그 다음 N줄에 걸쳐서 수빈이가 외치는 정수가 차례대로 주어진다. 
정수는 -10,000보다 크거나 같고, 10,000보다 작거나 같다.

출력
한 줄에 하나씩 N줄에 걸쳐 수빈이의 동생이 말해야하는 수를 순서대로 출력한다.

예제 입력 1 
7
1
5
2
10
-99
7
5
예제 출력 1 
1
1
2
2
2
2
5
'''


import sys
import heapq
N = int(sys.stdin.readline().replace("\n", ""))
min_heap = []
max_heap = []
for _ in range(N):
    now = int(sys.stdin.readline().replace("\n", ""))

    if len(min_heap) == len(max_heap):
        heapq.heappush(max_heap, (-1 * now, now))
    else:
        heapq.heappush(min_heap, (now, now))
    if min_heap and min_heap[0][1] < max_heap[0][1]:
        temp_a = heapq.heappop(min_heap)[1]
        temp_b = heapq.heappop(max_heap)[1]
        heapq.heappush(min_heap, (temp_b, temp_b))
        heapq.heappush(max_heap, (-1*temp_a, temp_a))
    print(max_heap[0][1])

'''코딩해설 : 우선순위 큐 heapq 및 sys.stdin.readlin()
지속적인 중앙값구하기위해서,
min heap에 중앙값보다 큰값을 계속 넣어준다.
max heap에 중앙값보다 작은 값을 계속 넣어준다.
min heap 과 max heap 의 꼭대기를 관찰하면 중앙값을 알수있다.
'''

