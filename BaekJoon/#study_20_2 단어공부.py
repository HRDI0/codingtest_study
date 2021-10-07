# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 2 초	128 MB	120644	47411	37902	39.148%
# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

# 예제 입력 1 
# Mississipi
# 예제 출력 1 
# ?

# 예제 입력 2 
# zZa
# 예제 출력 2 
# Z

# 예제 입력 3 
# z
# 예제 출력 3 
# Z

# 예제 입력 4 
# baaa
# 예제 출력 4 
# A

word = input().upper()
char_list = dict()
for c in word:
    if c in char_list:
        char_list[c] += 1
    else:
        char_list[c] = 1

sort_dict = sorted(char_list.items(), key=lambda x:x[1],reverse=True)   #딕셔너리 values 기준 정렬 

if len(sort_dict) > 1:                          #처리된 문자열이 여러개였을 경우 조건문
    if sort_dict[0][1] != sort_dict[1][1]:      #문자의 갯수가 같은 것이 있는 경우 조건문
        print(sort_dict[0][0].upper())
    else:
        print('?')                              #조건문에 걸리면 ? 출력
else:
    print(sort_dict[0][0].upper())              #남은 문자가 하나인 경우 그냥 그거 출력
