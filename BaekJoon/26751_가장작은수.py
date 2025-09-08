# 세자리 숫자(꼭 다를 필요는 없음)가 주어졌을 때, 가장 작은 세 자리 숫자가 되도록 순서대로 배열하세요. 이 숫자는 앞에 0이 올 수 없습니다.(0으로 시작 불가)

#입력 : 입력의 첫 번째(유일한) 줄에는 세 개의 음이 아닌 정수 X,Y, Z(0<= X,Y,Z<=9) 가 주어지면 적어도 이중 하나는 항상 양수입니다.

#출력 : 프로그램에서는 입력된 숫자를 문자열로 배열하여 얻을 수 있는 가장 작은 세자리 숫자(앞에 0이 붙지 않은)를 출력해야 합니다.

# 예제 입력 1 
# 5 2 0
# 예제 출력 1 
# 205
# 예시 설명: 답은 025가 될 수 없습니다. 025는 유효한 세 자리 숫자가 아니기 때문입니다. 숫자 앞에 0이 포함됩니다.

# 예제 입력 2 
# 1 2 3
# 예제 출력 2 
# 123

# import sys
# input = sys.stdin.readline

# num = input().split()

# a1 = int(num[0]+num[1]+num[2])
# a2 = int(num[0]+num[2]+num[1])
# b1 = int(num[1]+num[0]+num[2])
# b2 = int(num[1]+num[2]+num[0])
# c1 = int(num[2]+num[0]+num[1])
# c2 = int(num[2]+num[1]+num[0])

# min_n = 10000
# for i in [a1,a2,b1,b2,c1,c2]:
#     if i>=100 and i<=min_n:
#         min_n = i
# print(min_n)

import sys
from itertools import permutations

input = sys.stdin.readline
nums = input().split()               # 이미 문자열이므로 그대로 두고
candidates = (int(''.join(p))        # 각 순열을 문자열로 이어 붙인 뒤 int로
              for p in permutations(nums, 3))

# 100 이상인 값만 골라 최소값
valid = [v for v in candidates if v >= 100]

if not valid:                        # 엣지 케이스: 조건을 만족하는 게 없을 때
    print("no number >= 100")
else:
    print(min(valid))
