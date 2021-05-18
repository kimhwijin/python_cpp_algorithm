answer = ''
def split(w):
    u = ''
    v = ''
    global answer
    if len(w) == 0:
        return ''
    vaild = 0
    is_vaild = True
    balance = 0
    for i in range(len(w)):
        if w[i] == '(':
            vaild += 1
            balance += 1
        elif w[i] == ')':
            vaild -= 1
            if vaild < 0:
                is_vaild = False
            balance -= 1
            
        if balance == 0:
            u = w[:i+1]
            v = w[i+1:]
            break
    
    if is_vaild:
        answer += u + split(v)
        return answer
    else:
        u_str = ''
        for j in range(1,len(u)-1):
            if u[j] == '(':
                u_str += ')'
            elif u[j] == ')':
                u_str += '('
        
        answer += '(' + split(v) + ')' + u_str
        return answer
        

def solution(p):
    global answer    
    split(p)

    return answer