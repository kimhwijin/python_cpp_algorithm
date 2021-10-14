#dfs -> false 인 방은 stack 밑바닥에 재배치한다.
#9	[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]	[[8,5],[6,7],[4,1]]	true

def solution(n, path, order):
    max_room = n
    max_room += 1
    is_path = [[False for _ in range(max_room)] for _ in range(max_room)]
    is_locked_room = [False for _ in range(max_room)]
    is_released_room = [False for _ in range(max_room)]
    is_visited_room = [False for _ in range(max_room)]

    for r1, r2 in path:
        is_path[r1][r2] = True
        is_path[r2][r1] = True
    for _order in order:
        locked_room = _order[1] 
        is_locked_room[locked_room] = True
        release_room = _order[0]
        is_released_room[release_room] = locked_room
    stack = [0]

    while stack:
        room_num = stack.pop()
        is_visited_room[room_num] = True
        if is_locked_room[room_num]:
            stack.insert(0,room_num)
            continue
        
        if is_released_room[room_num] != False:
            is_locked_room[is_released_room[room_num]] = False
        for i in range(max_room):
            if is_path[room_num][i] and is_visited_room[i] == False:
                stack.append(i)

        if len(stack) == 0:
            answer = True
            break

        false_check = 1
        for _stack in stack:
            false_check *= is_locked_room[_stack]
        if false_check:
            answer = False
            break

    return answer
    
print(solution(9,[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],[[4,1],[8,7],[6,5]]))