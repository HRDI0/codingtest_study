def solution(s):
    answer = ''
    #글자와 숫자를 바꿔주기 위한 딕셔너리
    num_dict = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    ast = ''                #s에서 key 값을 뽑아내기 위한 문자열
    for word in s:          #s에서 숫자가 아닌경우 한 글자씩 추출하여 문자열에 붙이고
        if word.isalpha():
            ast += str(word)
            if ast in (num_dict):           #만들어진 문자열이 딕셔너리에 존재한다면 answer에 value 를 추가하고 ast 초기화
                answer += str(num_dict[ast])
                ast = ''
        elif word.isdigit():                #숫자일 경우 그냥 str타입으로 추가
            answer += word
    return int(answer)                      #return 값 조건이 int값이라 int타입으로 변환



#모범 답안
#이렇게도 되네..
# num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

# def solution(s):
#     answer = s
#     for key, value in num_dic.items():
#         answer = answer.replace(key, value)
#     return int(answer)
    

print(solution("one4seveneight"))