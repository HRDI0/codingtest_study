# 문제
# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 
# 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 
# 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

# 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 
# 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

# 출력
# 첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.

sang_num = int(input())
sang_list = list(map(int,input().split()))

m_num = int(input())
m_list = list(map(int,input().split()))

##########################################
card_dict = {}
for s in sang_list:
    card_dict[s] = card_dict.get(s, 0) + 1
print(' '.join(str(card_dict[m]) if m in card_dict else '0' for m in m_list))


#sang_list.sort()

# card_num = [0 for i in range(m_num)]
# pre_card_index = 0
# for i in range(sang_num):
#     pre_card = sang_list[i-1]
#     if sang_list[i] != pre_card or i == 0:
#         for j in range(m_num):
#             if m_list[j] == sang_list[i]:
#                 card_num[j] += 1
#                 pre_card_index = j
#                 break
#     else:
#         card_num[pre_card_index] +=1
# print(card_num)




# card_num = [0 for i in range(m_num)]
# m_index = 0
# for i in range(sang_num):
#     pre_card = sang_list[i-1]
#     if sang_list[i] != pre_card or i == 0:
#         if sang_list[i] in m_list:
#             m_index = m_list.index(sang_list[i])
#             card_num[m_index] += 1
#     else:
#         card_num[m_index] +=1
# for i in card_num:
#     print(i,end=" ")




# intersection_card = list(set(m_list) & set(sang_list))

# count_list = [0 for _ in range(m_num)]

# for ic in intersection_card:
#     count_list[m_list.index(ic)] = sang_list.count(ic)
# for output in count_list:
#     print(output,end= ' ')




# intersection_card = list(set(m_list) & set(sang_list))

# for ic in intersection_card:
#     for m in m_list:
#         if ic == m:
#             print(sang_list.count(ic),end= ' ')
#             continue
#     print(0,end=' ')