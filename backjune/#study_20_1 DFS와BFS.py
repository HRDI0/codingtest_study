# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 2 초	128 MB	149910	52071	30548	34.198%
# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 
# 입력으로 주어지는 간선은 양방향이다.

# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

# 예제 입력 1 
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 예제 출력 1 
# 1 2 4 3
# 1 2 3 4

# 예제 입력 2 
# 5 5 3
# 5 4
# 5 2
# 1 2
# 3 4
# 3 1
# 예제 출력 2 
# 3 1 2 5 4
# 3 1 4 2 5

# 예제 입력 3 
# 1000 1 1000
# 999 1000
# 예제 출력 3 
# 1000 999
# 1000 999

from collections  import deque

n,line,start = map(int, input().split())
graph = [[] for _ in range(n+1)]        #노드 갯수만큼 리스트 생성

for i in range(line):                   #양방향 간선이니까 양쪽 다 연결 기록
    g = list(map(int,input().split()))
    graph[g[0]].append(g[1])
    graph[g[1]].append(g[0])

for i in graph:                         #기본적으로 dfs bfs 는 작은 번호의 노드순으로
    i.sort()

visited_d = [False] * (n + 1)           #각 알고리즘별 방문 확인 리스트
visited_b = [False] * (n + 1)

def dfs(graph, start, visited):         #dfs 가장 작은 번호를 가진 미방문 노드를 쭉쭉 탐색
    visited[start] = True
    print(start,end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph,i,visited)


def bfs(graph, start, visited):        #현재 노드와 연결된 모든 노드를 일단 큐에 넣고 방문처리
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()                #큐에 가장 앞에 있는 노드와 연결된 노드도 다 큐에 넣고 방문처리
        print(v,end=' ')                #더 이상 미방문 노드가 없을 때까지 반복.
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

dfs(graph,start,visited_d)
print()
bfs(graph,start,visited_b)