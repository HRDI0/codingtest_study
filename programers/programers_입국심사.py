def solution(n, times):
    answer = 0
    times = sorted(times)
    start,end =1, times[-1] * n
    while start <= end:
        mid = (start + end) // 2
        p = 0
        for time in times:
            p += mid // time
            if p >= n:
                break
        if p < n:
            start = mid + 1
        elif p >= n:
            answer = mid
            end = mid - 1
    return answer

print(solution(6,[7,10]))