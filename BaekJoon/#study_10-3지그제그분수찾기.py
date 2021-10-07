#study_10-3.py
# 무한히 큰 배열에 다음과 같이 분수들이 적혀있다.

# 1/1	1/2	1/3	1/4	1/5	…
# 2/1	2/2	2/3	2/4	…	…
# 3/1	3/2	3/3	…	…	…
# 4/1	4/2	…	…	…	…
# 5/1	…	…	…	…	…
# …	…	…	…	…	…
# 이와 같이 나열된 분수들을 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2 -> … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.

# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

# def div_counting(input_num):
#     a,b = 1,1
#     plus_a = 0
#     plus_b = 1
#     max_n = 2
#     if input_num == 1:
#         return '1/1'
#     else:
#         for i in range(input_num-1):
#             b +=plus_b
#             a +=plus_a
#             if b == max_n:
#                 max_n +=1
#                 plus_a = 1
#                 plus_b = -1
#             if a == max_n:
#                 max_n +=1
#                 plus_a = -1
#                 plus_b = 1
#             if a == 0:
#                 a+=1
#             if b == 0:
#                 b+=1
#         return a,b

def div_counting(input_num):
    max_n = 0
    line_n = 0
    while input_num > max_n:
        line_n +=1
        max_n += line_n
    dif = max_n - input_num
    if line_n % 2 == 0:
        a = line_n - dif
        b = dif + 1
    else:
        a = dif +1
        b = line_n - dif

    return a,b        

n = int(input())
r_a,r_b = div_counting(n)
print('{0}/{1}'.format(r_a,r_b))