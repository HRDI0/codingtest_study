def uv(p):
    left = 0
    right = 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        elif p[i] == ')':
            right +=1
        if left == right:
            u = p[:i+1]
            if i+1 < len(p):
                v = p[i+1:]
                break
            else:
                v = ""
                break
    return u,v

def correct(p):
    s = []
    for c in p:
        if c == '(':
            s.append(c)
        else:
            if not len(s):
                return False
            elif s[-1] == '(':
                s.pop()
    if len(s):
        return False
    else:
        return True

def solution(p):
    answer = ''
    if not len(p):
        return answer 
    elif correct(p):
        return p
    u,v = uv(p)
    if correct(u):
        answer = u + solution(v)
    else:
        temp = "("
        temp += solution(v)
        temp +=")"
        u = u[1:-1]
        for c in u:
            if c == '(':
                temp += ")"
            elif c == ')':
                temp += "("
        answer += temp       
    return answer

s = input()
print(solution(s))