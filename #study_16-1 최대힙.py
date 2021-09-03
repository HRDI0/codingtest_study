# 문제
# 널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

# 배열에 자연수 x를 넣는다.
# 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

# 입력
# 첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 
# 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 
# 입력되는 자연수는 2^31보다 작다.

# 출력
# 입력에서 0이 주어진 회수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 가장 큰 값을 출력하라고 한 경우에는 0을 출력하면 된다.

import heapq
import sys
input=sys.stdin.readline

n = int(input())
e_list = []


for _ in range(n):
    e_list.append(int(input()))

heap_list = []
heapq.heapify(heap_list)
for i in e_list:
    if i == 0 and len(heap_list) == 0:
        print(0)
    elif i == 0:
        print(abs(heapq.heappop(heap_list)))
    else:
        heapq.heappush(heap_list,-i)


# n = int(input())
# max_hip = [0]

# def hip_in(input_num):
#     max_hip.append(input_num)
#     i = len(max_hip) - 1
#     while i != 1 and input_num > max_hip[i//2]:
#         max_hip[i], max_hip[i//2] = max_hip[i//2], max_hip[i]
#         i //= 2
        

# def hip_out(input_num):
#     if len(max_hip) -1 == 0:
#         print(0)
#     else:
#         print(max_hip[1])
#         max_hip[1],max_hip[-1] = max_hip[-1],max_hip[1]
#         del max_hip[-1]

#         i = 1
#         while i <= len(max_hip) - 2:
#             if max_hip[i] < max_hip[i+1] and i+1 <= len(max_hip) - 1:
#                 max_hip[i], max_hip[i+1] = max_hip[i+1], max_hip[i]
#                 i +=1

#             elif max_hip[i] < max_hip[i+2] and i+2 <= len(max_hip) - 2:
#                 max_hip[i], max_hip[i+2] = max_hip[i+2], max_hip[i]
#                 i+=2
            
#             else:
#                 break

# for _ in range(n):
#     comend = int(input())
#     if comend == 0:
#         hip_out(comend)
#     else:
#         hip_in(comend)
        