# 문제
# 젠가를 하는 컴퓨터 프로그램을 작성하고 있는데, 먼저 어떤 보드가 유효한지 알아내야 합니다! 가능한 젠가 보드 세트가 주어졌을 때, 각 보드가 서 있는지 아니면 넘어졌는지 판별하세요. 한 행(열이 아님)에서 두 개의 연속된 블록이 모두 없으면(맨 윗줄 포함) 보드가 넘어집니다. 맨 윗줄에서 두 개의 연속된 블록이 모두 없으면 탑이 "넘어졌다"고 가정합니다.

# 입력
# 입력의 첫 번째 줄은 다음에 오는 테스트 케이스의 개수입니다.

# 각 입력 케이스는 젠가 탑의 높이를 나타내는 단일 정수로 시작합니다. 탑의 각 행은 한 줄에 나타나며, 해당 행의 보드에 현재 남아 있는 블록을 나타냅니다. '1'은 블록이 존재함을, '0'은 제거된 블록을 나타냅니다.

# 1~100개의 테스트 케이스가 있으며, 각 케이스에는 높이 1~20 사이의 젠가 보드가 하나씩 있습니다.

# 출력
# 각 사례에 대해 "Case x:" 줄을 출력합니다. 여기서 x는 사례 번호이며, 한 줄 뒤에 공백 한 개와 "Fallen" 또는 "Standing"이라는 단어가 옵니다.

# 예제 입력 1 
# 4
# 8
# 111
# 111
# 111
# 100
# 101
# 111
# 010
# 111
# 4
# 111
# 111
# 101
# 101
# 5
# 000
# 111
# 111
# 111
# 101
# 8
# 111
# 010
# 111
# 011
# 100
# 101
# 101
# 111
# 예제 출력 1 
# 사례 1: Fallen
# 사례 2: Standing
# 사례 3: Fallen
# 사례 4: Fallen


import sys
input = sys.stdin.readline

num_of_task = int(input())
answer_list = []
for i in range(num_of_task):
    nos = int(input()) # num of steps
    answer = 'Standing'
    for i in range(nos):
        steps = input()
        if '00' in steps or '000' in steps:
            answer = 'Fallen'
    answer_list.append(answer)
for i in range(len(answer_list)):
    print(f'Case {i+1}: {answer_list[i]}')
            