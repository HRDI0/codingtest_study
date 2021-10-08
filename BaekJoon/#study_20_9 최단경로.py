# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 1 초	256 MB	105196	29080	14136	23.744%
# 문제
# 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 
# 단, 모든 간선의 가중치는 10 이하의 자연수이다.

# 입력
# 첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. 
# (1≤V≤20,000, 1≤E≤300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다. 
# 둘째 줄에는 시작 정점의 번호 K(1≤K≤V)가 주어진다. 
# 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다. 
# 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다. 
# 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.

# 출력
# 첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 
# 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.

# 예제 입력 1 
# 5 6
# 1
# 5 1 1
# 1 2 2
# 1 3 3
# 2 3 4
# 2 4 5
# 3 4 6
# 예제 출력 1 
# 0
# 2
# 3
# 7
# INF

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)                      #distance 초기화를 위한 무한
V,E = map(int, input().split())     #노드와 간선의 개수
start = int(input())                #시작점
graph = [[] for _ in range(V+1)]    #각노드와 인접한 노드의 거리를 넣기 위한 이차리스트 / 노드 번호에 맞춰 입력하기 위해 V+1
distance = [INF] * (V+1)            #최단 거리를 입력하기 위한 리스트 / 마찬가지로 번호 맞춰 입력하기 위해 V+1
for i in range(E):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))          #a 에서 b 까지의 비용(거리) c

def dijkstra(start):
    q = []                          #우선순위 heapq은 트리구조로 항상 오름차순으로 정렬되어 들어간다.
    heapq.heappush(q,(0,start))     #최소 비용 순으로 pop하기 위한 우선순위 heapq
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:    #이미 방문한(최단거리가 입력된) 노드라면 통과
            continue
        for g in graph[now]:        
            cost = dist + g[1]      #현재 노드에서 인접한 노드로 가는 비용
            if cost < distance[g[0]]:   #만약 위 비용이 입력되어 있는 비용보다 적다면
                distance[g[0]] = cost   #최단거리 비용을 갱신한다.
                heapq.heappush(q,(cost,g[0]))   #해당 인접노드를 처리하기 위해 heapq에 heappush
dijkstra(start)

for i in range(1,V+1):          #시작 노드에서 각노드로 가는 최단 거리 출력
    if distance[i] == INF:
        print('INF')            #시작노드에서 갈수 없다면 'INF' 출력
    else:
        print(distance[i])
