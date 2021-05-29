'''
                  10 

            /         \ 

           4             9

        /     \         /     \ 

       3       1       2      7 

     /   \

    5     6
'''
from collections import deque
graph = {}
start_node = 10
graph[10] = [4,9]
graph[4] = [3,1]
graph[9] = [2,7]
graph[3] = [5,6]
graph[1] = []
graph[2] = []
graph[7] = []
graph[5] = []
graph[6] = []

def bfs(graph):
    print('bfs start')
    queue = deque()
    queue.append(start_node)
    while queue:
        n = queue.popleft()
        print(n,end='->')
        for node in graph[n]:
            queue.append(node)

def dfs(graph, stack):
    if len(stack) == 0:
        return
    n = stack.pop()
    print(n,end='->')
    for node in graph[n]:
        stack.append(node)
        dfs(graph, stack)

print('\ngraph : ', graph, '\n')
bfs(graph)
print('end')
stack = [start_node]
print('dfs start')
dfs(graph, stack)
print('end')
