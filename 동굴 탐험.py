from collections import deque

def solution(n, path, order):
    visited = [False for _ in range(n)]
    locked = [i for i in range(n)]
    locked_reverse = [i for i in range(n)]
    blocked = set()

    for fst, snd in order:
        if snd == 0:
            return False
        locked[snd] = fst
        locked_reverse[fst] = snd
        
    n_path = [[] for _ in range(n)]
    for r1, r2 in path:
        n_path[r1].append(r2)
        n_path[r2].append(r1)
        
    queue = deque()
    queue.append(0)

    while queue:
        room = queue.popleft()
        if locked[room] != room:
            if visited[locked[room]] != True:
                blocked.add(room)
                continue
                
        visited[room] = True
        if locked_reverse[room] in blocked:
            blocked.remove(locked_reverse[room])
            queue.append(locked_reverse[room])
        for rn in n_path[room]:
            if visited[rn] != True:
                queue.append(rn) 
    
    if False in visited:
        answer = False
    else:
        answer = True
    
    return answer