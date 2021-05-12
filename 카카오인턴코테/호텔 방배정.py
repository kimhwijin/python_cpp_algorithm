def solution(k, room_number):
    answer = []
    request_room = room_number
    direction = {}
    
    
    for rr in request_room:
        if rr in direction.keys():
            nextkey = direction[rr][0]
            answer.append(nextkey)
            if nextkey + 1 in direction.keys():
                direction[rr] = direction[nextkey + 1]
            else:
                direction[rr][0] = nextkey + 1
                direction[nextkey + 1] = direction[rr]
        else:
            if rr + 1 not in direction.keys():
                direction[rr+1] = [rr+1]
            direction[rr] = direction[rr+1]
            answer.append(rr)
            
                
    return answer