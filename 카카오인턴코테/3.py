def solution(n, k, cmd):
    answer = ''
    alist = ['O'] * n

    stack = []
    idx = 0

    while idx < len(cmd):
        inst = cmd[idx]
        dk = 0
        while inst[0] != 'C':
            #Up
            if inst[0] == 'U':
                dk -= int(inst[2])
            #down
            elif inst[0] == 'D':
                dk += int(inst[2])
            #cancel
            elif inst[0] == 'Z':
                print('z:',stack)
                alist[stack.pop()] = 'O'
            idx += 1
            if idx == len(cmd):
                break
            inst = cmd[idx]

        if idx == len(cmd):
            break
        #delete
        if dk > 0:
            d = 1
        elif dk < 0:
            d = -1
        elif dk == 0:
            d = 0
        i = d
        while dk != 0:
            if alist[k + i] == 'X':
                i += d
            else:
                i += d
                dk -= d
        k = k + i - d
        stack.append(k)
        alist[k] = 'X'

        flag = False
        for aa in range(k+1,n):
            if alist[aa] == 'O':
                flag = True
                k = aa
                break
        
        if flag == False:
            for aa in range(k-1,-1,-1):
                if alist[aa] == 'O':
                    k = aa
                    break
        idx += 1

    answer = ''.join(alist)
    return answer

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(n,k,cmd))