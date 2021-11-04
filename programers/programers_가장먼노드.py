import heapq

def solution(n, edge):
    answer = 0
    INF = int(1e9)
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)
    for a,b in edge:
        graph[a].append((b,1))
        graph[b].append((a,1))
    
    q = []
    heapq.heappush(q,(1,0))
    distance[1] = 0

    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(i[0],cost))
    count = sorted(list(set(distance)),reverse= True)
    answer = distance.count(count[1])
    return answer

a = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(6,a))