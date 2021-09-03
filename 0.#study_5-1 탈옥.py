#study5-1 탈옥
# 상근이는 감옥에서 죄수 두 명을 탈옥시켜야 한다. 이 감옥은 1층짜리 건물이고, 상근이는 방금 평면도를 얻었다.
# 평면도에는 모든 벽과 문이 나타나있고, 탈옥시켜야 하는 죄수의 위치도 나타나 있다. 감옥은 무인 감옥으로 죄수 두 명이 감옥에 있는 유일한 사람이다.
# 문은 중앙 제어실에서만 열 수 있다. 상근이는 특별한 기술을 이용해 제어실을 통하지 않고 문을 열려고 한다. 하지만, 문을 열려면 시간이 매우 많이 걸린다. 
# 두 죄수를 탈옥시키기 위해서 열어야 하는 문의 개수를 구하는 프로그램을 작성하시오.

# 첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스의 수는 100개를 넘지 않는다.
# 첫째 줄에는 평면도의 높이 h와 너비 w가 주어진다. (2 ≤ h, w ≤ 100) 다음 h개 줄에는 감옥의 평면도 정보가 주어지며, 
# 빈 공간은 '.', 지나갈 수 없는 벽은 '*', 문은 '#', 죄수의 위치는 '$'이다.
# 상근이는 감옥 밖을 자유롭게 이동할 수 있고, 평면도에 표시된 죄수의 수는 항상 두 명이다.
#  각 죄수와 감옥의 바깥을 연결하는 경로가 항상 존재하는 경우만 입력으로 주어진다.
# 각 테스트 케이스마다 두 죄수를 탈옥시키기 위해서 열어야 하는 문의 최솟값을 출력한다.

test_case = int(input())
for k in range(test_case):
    h,w = map(int, input().split())
    escape = []
    for i in range(h):
        escape.append(list(input()))
    loc_x1, loc_y1, loc_x2, loc_y2 = 0,0,0,0
    for i in range(h):
        for j in range(w):
            if escape[i][j] == '$':
                if loc_x1 == 0:
                    loc_x1 = j
                    loc_y1 = i
                else:
                    loc_x2 = j
                    loc_y2 = i
    
    door_count = 0
    for i in range(h):
        for j in range(w):
            if loc_y1 < 0 or loc_x1 < 0 or loc_y1 >= h or loc_x1 >= w:
                continue
            if escape[loc_x1+1][loc_y1] == '.':
                loc_x1 +=1
            elif escape[loc_x1-1][loc_y1] == '.':
                loc_x1 -=1
            elif escape[loc_x1][loc_y1+1] == '.':
                loc_y1 +=1
            elif escape[loc_x1][loc_y1-1] == '.':
                loc_y1 -=1
                
            if loc_y1 < 0 or loc_x1 < 0 or loc_y1 >= h or loc_x1 >= w:
                continue
            if escape[loc_x1+1][loc_y1] == '#':
                loc_x1 +=1
                door_count+=1
            elif escape[loc_x1-1][loc_y1] == '#':
                loc_x1 -=1
                door_count+=1
            elif escape[loc_x1][loc_y1+1] == '#':
                loc_y1 +=1
                door_count+=1
            elif escape[loc_x1][loc_y1-1] == '#':
                loc_y1 -=1
                door_count+=1
    print(door_count)