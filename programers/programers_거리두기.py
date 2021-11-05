# 두 테이블 T1, T2가 행렬 (r1, c1), (r2, c2)에 각각 위치하고 있다면, 
# T1, T2 사이의 맨해튼 거리는 |r1 - r2| + |c1 - c2| 입니다. ↩
# https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-%EA%B1%B0%EB%A6%AC%EB%91%90%EA%B8%B0-%ED%99%95%EC%9D%B8%ED%95%98%EA%B8%B0-Python
from collections import deque

def bfs(places, start):
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for s in start:
        visited = [[False] * 5 for _ in range(5)]
        distans = [[0]*5 for _ in range(5)]
        q = deque([s])
        visited[s[0]][s[1]] = True
        
        while q:
            y, x = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<5 and 0<=ny<5 and visited[ny][nx] == False:
                    if places[ny][nx] == 'O':
                        q.append([ny,nx])
                        visited[ny][nx] = True
                        distans[ny][nx] = distans[y][x] +1

                    if places[ny][nx] == 'P' and distans[y][x] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []
    start = []
    for p in places:
        for i in range(5):
            for j in range(5):
                if p[i][j] == 'P':
                    start.append([i,j])
        answer.append(bfs(p,start))
        start.clear()

    return answer

p = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(p))