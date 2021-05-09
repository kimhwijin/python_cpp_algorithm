def solution(n, k, cmd):
    answer = ''
    alist = ['O'] * n
    nlist = list(range(n))

    stack = []
    idx = 0
    while idx < len(cmd):
        inst = cmd[idx]
        if inst[0] == 'U':
            k -= int(inst[2])
        elif inst[0] == 'D':
            k += int(inst[2])
        elif inst[0] == 'C':
            tmp = nlist.pop(k)
            stack.append((tmp,k))
            alist[tmp] = 'X'
            if k == len(nlist):
                k -= 1

        elif inst[0] == 'Z':
            aidx, nidx = stack.pop()
            alist[aidx] = 'O'
            if nidx <= k:
                k += 1
            nlist.insert(nidx,aidx)
        idx += 1

    answer = ''.join(alist)
    return answer

n = 8
k = 7
cmd = ["C","C","C","C","C","C","C","C","Z"]
print(solution(n,k,cmd))