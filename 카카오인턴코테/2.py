def solution(places):
    answer = []
    no_checkPos = [(1,0),(0,1),(-1,0),(0,-1)]
    checkPos1 = [(1,1),(-1,1),(-1,-1),(1,-1)]
    checkPos2 = [(2,0),(-2,0),(0,2),(0,-2)]


    for i in range(5):
        table = places[i]
        stack = []
        for j in range(5):
            for k in range(5):
                if table[k][j] == 'P':
                    stack.append((j,k))

        flag = False
        print(stack)
        for x, y in stack:
            for dx , dy in no_checkPos:
                checkx = x + dx
                checky = y + dy
                if checkx < 0 or checkx > 4 or checky < 0 or checky > 4:
                    continue
                if table[checky][checkx] == 'P':
                    flag = True
                    break
            if flag == True:
                break
            for dx , dy in checkPos2:
                checkx = x + dx
                checky = y + dy
                if checkx < 0 or checkx > 4 or checky < 0 or checky > 4:
                    continue
                if table[checky][checkx] == 'P':
                    midx = x + int(dx / 2)
                    midy = y + int(dy / 2)
                    if table[midy][midx] != 'X':
                        flag = True
                        break
            if flag == True:
                break
            
            for dx, dy in checkPos1:
                checkx = x + dx
                checky = y + dy
                if checkx < 0 or checkx > 4 or checky < 0 or checky > 4:
                    continue
                if table[checky][checkx] == 'P':
                    midx1 = x
                    midy1 = y + dy

                    midx2 = x + dx
                    midy2 = y
                    if table[midy1][midx1] != 'X' or table[midy2][midx2] != 'X':
                        flag = True
                        break
            if flag == True:
                break

        if flag == True:
            answer.append(0)
        else:
            answer.append(1)

    return answer


arr = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(arr))