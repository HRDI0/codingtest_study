
import heapq
from sys import stdin
input = stdin.readline


def solution(scoville, K):
    low_scov = []
    low_plus = 0
    answer = 0
    for scov in scoville:
        heapq.heappush(low_scov,scov)
    while len(low_scov) != 1:
        low1 = heapq.heappop(low_scov)
        low2 = heapq.heappop(low_scov)

        if low1 < K or low2 < K:
            low_plus = low1 + (low2 * 2)
            heapq.heappush(low_scov,low_plus)
            answer +=1
        else:
            heapq.heappush(low_scov,low1)
            heapq.heappush(low_scov,low2)
            break
    if heapq.heappop(low_scov) < K:
        return -1
    else:
        return answer

scoville = list(map(int,input().split()))
K = int(input())
print(solution(scoville, K))
