#study8-2.py
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 
# 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                del left[0]
            else:
                result.append(right[0])
                del right[0]
        elif len(left) > 0:
            result.append(left[0])
            del left[0]
        elif len(right)>0:
            result.append(right[0])
            del right[0]
    return result

def merge_sort(num_list):
    if len(num_list) <= 1:
        return num_list
    mid = len(num_list) // 2
    leftlist = num_list[:mid]
    rightlist= num_list[mid:]
    leftlist = merge_sort(leftlist)
    rightlist = merge_sort(rightlist)
    return merge(leftlist, rightlist)

size_of_num = int(input())
num_list = []
for i in range(size_of_num):
    num_list.append(int(input()))
sort_result = merge_sort(num_list)

for i in range(size_of_num):
    print(sort_result[i])
#################################################################
# size_of_num = int(input())
# num_list = []
# for i in range(size_of_num):
#     num_list.append(int(input()))

# for i in sorted(num_list):
#     print(i)