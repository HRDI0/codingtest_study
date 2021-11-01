# def solution(s):
#     answer = -1
#     double_case = ['aa','bb','cc','dd','ee',
#     'ff','gg','hh','ii','jj','kk','ll',
#     'mm','nn','oo','pp','qq','rr','ss',
#     'tt','uu','ww','vv','xx','yy','zz']
#     if len(s) %2 != 0:
#         answer = 0
#         return answer
#     for i in range(26):
#         s = s.replace(double_case[i],"")
#     if not s:
#         answer = 1
#     else:
#         answer = 0
#     return answer

def solution(s):
    answer = -1
    stack = []
    for data in s:
        if len(stack) == 0:
            stack.append(data)
        elif stack[-1] == data:
            stack.pop(-1)
        else:
            stack.append(data)
    if not stack:
        answer = 1
    else:
        answer = 0
    return answer

print(solution(input()))