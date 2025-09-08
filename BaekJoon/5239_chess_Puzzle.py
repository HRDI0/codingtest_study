# 문제
# Jake and Sully are playing around with a chessboard one night after working with their avatars all day. They decide it would be interesting to place some rooks on the chessboard in a way that no rook can threaten another rook. Since rooks move along rows and columns, this means two rooks may not be on the same row or column. Your goal is to write a program to determine whether any rooks are threatened.

# 입력
# Chessboards are 8x8 boards with positions between (1,1) and (8,8). The input begins with the number of chess boards. Each chessboard is on a separate line and begins with the number of rooks, followed by the column and row positions of each rook.

# 출력
# For each chessboard, your program should output the words ”SAFE” or ”NOT SAFE” on a single line.

# 출력 형식
# 정확한 출력 형식은 제출에서 언어를 Java로 설정하면 확인할 수 있다.

# 예제 입력 1 
# 2
# 3 1 1 2 6 8 8
# 2 2 3 1 3
# 예제 출력 1 
# SAFE
# NOT SAFE

"""
문제가 영어라 잘 이해는 안되지만 추정하건데, 첫 입력은 case 수 N, 각 case의 첫 번째 양수는 rook의 수 K, 그 다음 부터는 K개만큼의 rook의 i,j 형식의 좌표 값이 주어진다.
모든 룩을 배치했을 때, 룩이 서로 잡을 수 있는 상태라면 NOT SAFE, 룩이 서로 잡을 수 없는 상태라면 SAFE를 출력한다.


단순히 행과 열이 겹치는 지만 비교하면 될거 라고 생각해서 모든 값을 set()로 묶어 남은 수의 갯수가 전체 룩 수 *2 보다 적다면 not safe라고 구현했으나, 행과 열이 같은 경우를 간과했다. 행과 열 set(), 행, 열, 세 가지 set()를 만들어 그 수가 num_of_rooks 보다 작지 않은지 확인해 문제를 해결했다.
"""

import sys
input = sys.stdin.readline

case = int(input())
answer_list = []
for i in range(case):
    answer = 'SAFE'
    rook_info = list(map(int,input().split()))
    num_of_rooks = rook_info[0]
    rook_info = rook_info[1:]
    rook_info = list(zip(rook_info[0::2],rook_info[1::2]))
    
    rows = set()
    cols = set()
    pairs = set()
    for r,c in rook_info:
        rows.add(r)
        cols.add(c)
        pairs.add((r,c))
    if num_of_rooks > len(rows) or num_of_rooks > len(cols) or num_of_rooks > len(pairs):
        answer = 'NOT SAFE'
    answer_list.append(answer)

for i in answer_list:
    print(i)