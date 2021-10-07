#study_10-1.py
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, 
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

def group_checker(input_str):
    again_str = 0
    for index in range(len(input_str)-1):
        if input_str[index] != input_str[index + 1]:
            dif_word = input_str[index + 1:]
            if dif_word.count(input_str[index]) != 0:
                again_str +=1
    if again_str == 0:
        return True

n = int(input())
word = []
group_count = 0
for i in range(n):
    word.append(list(input()))

for i in word:
    if group_checker(i):
        group_count +=1

print(group_count)
