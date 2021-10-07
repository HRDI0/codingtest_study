# 문제
# 준규는 숫자 카드 N장을 가지고 있다. 숫자 카드에는 정수가 하나 적혀있는데, 적혀있는 수는 -262보다 크거나 같고, 262보다 작거나 같다.

# 준규가 가지고 있는 카드가 주어졌을 때, 가장 많이 가지고 있는 정수를 구하는 프로그램을 작성하시오. 
# 만약, 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력한다.

# 입력
# 첫째 줄에 준규가 가지고 있는 숫자 카드의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개 줄에는 숫자 카드에 적혀있는 정수가 주어진다.

# 출력
# 첫째 줄에 준규가 가장 많이 가지고 있는 정수를 출력한다.

#################################
# n = int(input())
# num_list = []
# for i in range(n):
#     num_list.append(input())

# count_set = set(num_list)
# max_num = num_list[0]
# for j in range(len(count_set)):
#     if num_list.count(j) > num_list.count(max_num):
#         max_num = j
# print(max_num)

#################################
# n = int(input())
# num_list = []
# for i in range(n):
#     num_list.append(input())

# count_dict = {}
# for i in num_list:
#     count_dict[i] = count_dict.get(i, 0) + 1
# revers_dict = {v:k for k,v in count_dict.items()}
# print(revers_dict[max(count_dict.values())])

##################################
# n = int(input())
# count_dict = {}
# for i in range(n):
#     input_num = input()
#     count_dict[input_num] = count_dict.get(input_num, 0) + 1
# revers_dict = {v:k for k,v in count_dict.items()}
# print(revers_dict[max(count_dict.values())])

########################################################
from sys import stdin

n = int(stdin.readline())

count_dict = {}
for i in range(n):
    input_num = int(stdin.readline())
    if input_num in count_dict:
        count_dict[input_num] += 1
    else:
        count_dict[input_num] = 1
sort_dict = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
print(sort_dict[0][0])
