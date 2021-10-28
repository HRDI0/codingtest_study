def solution(progresses, speeds):
    p_size = len(progresses)
    work_end = [0]*p_size
    day = 0
    while True:    
        for p in range(p_size):
            if p == 0:
                if progresses[p] >= 100:
                    if work_end[p] == 0:
                        work_end[p] = day
                else:
                    progresses[p] += speeds[p] 
            else:
                if work_end[p-1] != 0 and progresses[p] >= 100:
                    if work_end[p] == 0:
                        work_end[p] = day
                else:
                    progresses[p] += speeds[p]
        day += 1            
        if not 0 in work_end:
            break

    answer = {}
    for end in work_end:
        answer[end] = answer.get(end,0)+1
    result = []
    for r in answer.values():
        result.append(r)
    return result

progresses = list(map(int, input().split()))
speeds = list(map(int, input().split()))
print(solution(progresses,speeds))