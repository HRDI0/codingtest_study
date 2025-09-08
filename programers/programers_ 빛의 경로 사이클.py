#출처 - https://programmers.co.kr/learn/courses/30/lessons/86052

def goto(grid, visited, start):
    x, y, way = start
    direction = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    length = 0
    while True:
        if visited[x][y][way]:
            break
        
        visited[x][y][way] = True
        length += 1
        
        if grid[x][y] == 'S':
            pass
        elif grid[x][y] == 'L':
            way = (way + 1) % 4
        elif grid[x][y] == 'R':
            way = (way - 1) % 4
        
        x = (x + direction[way][0]) % len(grid)
        y = (y + direction[way][1]) % len(grid[0])

    return length
 
def solution(grid):
    answer = []
    visited = [[[False] * 4 for _ in range(len(grid[0]))] for __ in range(len(grid))]
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in range(4):
                if visited[i][j][k] == False:
                    answer.append(goto(grid, visited, [i, j, k]))
                    
    answer.sort()
    return answer