
def split(w):
    vaild = 0
    is_vaild = False
    balance = 0
    for i in range(len(w)):
        if w[i] == '(':
            vaild += 1
            balance += 1
        elif w[i] == ')':
            vaild -= 1
            balance -= 1
            
        if balance == 0:
            if vaild == 0:
                is_vaild = True
            return w[:i] , w[i:], is_vaild
        
        
def solution(p):
    answer = ''
    while True:
        u , v , is_vaild = split(p)
        if is_vaild:
            if len(v) == 0:
                return u
            else:
                answer += u
                p = v
        else:
            

    return answer