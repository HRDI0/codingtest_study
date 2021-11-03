def solution(rows, columns, queries):
    INF = int(1e9)
    answer = []
    input_list = [[0 for _ in range(columns)] for _ in range(rows)]
    a = 1
    for i in range(rows):
        for j in range(columns):
            input_list[i][j] = a
            a+=1
    for q in queries:
        q = [x-1 for x in q]
        temp = input_list[q[0]][q[1]]
        min_num = temp
        #left
        for i in range(q[0]+1, q[2] +1):
            input_list[i-1][q[1]] = input_list[i][q[1]]
            min_num = min(min_num,input_list[i-1][q[1]])
        #bottom
        for i in range(q[1]+1, q[3] +1):
            input_list[q[2]][i-1] = input_list[q[2]][i]
            min_num = min(min_num,input_list[q[2]][i])
         # right
        for i in range(q[2]-1, q[0]-1, -1):
            input_list[i+1][q[3]] = input_list[i][q[3]]
            min_num = min(min_num,input_list[i][q[3]])
        # top
        for i in range(q[3]-1, q[1]-1, -1):
            input_list[q[0]][i+1] = input_list[q[0]][i]
            min_num = min(min_num,input_list[q[0]][i])

        input_list[q[0]][q[1]+1] = temp
        answer.append(min_num)
    return answer

row,column = map(int,input().split())
querie = [[1,1,100,97]]
# [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
# [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]


print(solution(row,column,querie))