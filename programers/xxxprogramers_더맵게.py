
import heapq
from sys import stdin
input = stdin.readline


def solution(scoville, K):
    low_scov = []
    low_plus = 0
    answer = 0
    for scov in scoville:
        heapq.heappush(low_scov,scov)
    while low_scov:
        low1 = heapq.heappop(low_scov)
        if low_scov:
            low2 = heapq.heappop(low_scov)
        else:
            break
        # if low_scov:
        #     low2 = heapq.heappop(low_scov)
        # else:
        #     answer = -1
        #     break
        if low1 < K or low2 < K:
            low_plus = low1 + (low2 * 2)
        if low_plus < K:
            heapq.heappush(low_scov,low_plus)
            answer +=1
        else:
            answer +=1
    return answer - 1

scoville = list(map(int,input().split()))
K = int(input())
print(solution(scoville, K))
