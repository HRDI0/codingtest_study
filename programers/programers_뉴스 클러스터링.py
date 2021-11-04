



# from collections import deque
# def mult_union(s_list1, s_list2):
#     s_list1 = deque(sorted(s_list1))
#     s_list2 = deque(sorted(s_list2))
#     union_result = []
#     while True:
#         if s_list1 and s_list2:
#             a = s_list1.popleft()
#             b = s_list2.popleft()
#             if a != b:
#                 union_result.append(a)
#                 union_result.append(b)
#             else:
#                 union_result.append(a)
#         elif s_list1 and (not s_list2):
#             for s in s_list1:
#                 union_result.append(s)
#             break
#         elif (not s_list1) and s_list2:
#             for s in s_list2:
#                 union_result.append(s)
#             break
#         else:
#             break
#     return union_result

# def mult_inter(s_list1, s_list2):
#     inter_result = []
#     s_list1 = deque(sorted(s_list1))
#     s_list2 = deque(sorted(s_list2))
#     while True:
#         if s_list1 and s_list2:
#             a = s_list1.popleft()
#             b = s_list2.popleft()
#             if a == b:
#                 inter_result.append(a)
#         else:
#             break
#     return inter_result

from collections import Counter

def correct(s):
    temp = []
    for i in range(len(s)-1):
        if s[i].isalpha() and s[i+1].isalpha():
            temp.append((s[i] + s[i+1]).lower())
    return temp


def solution(str1, str2):
    answer = 0
    s_list1 = correct(str1)
    s_list2 = correct(str2)
    c_list1 = Counter(s_list1)
    c_list2 = Counter(s_list2)
    union_set = list((c_list1 | c_list2).elements())
    inter_set = list((c_list1 & c_list2).elements())

    if (not union_set) and (not inter_set):
        return 65536
    answer = int((len(inter_set) / len(union_set)) * 65536)
    return answer

a,b = input().split()
print(solution(a,b))