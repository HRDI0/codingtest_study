def solution(numbers, target):
    answer = 0
    n_size = len(numbers)
    q = [[numbers[0],0], [-numbers[0],0]]
    while q:
        result, idx = q.pop()
        idx +=1
        if idx < n_size:
            q.append([result + numbers[idx], idx])
            q.append([result - numbers[idx], idx])
        else:
            if result == target:
                answer +=1
    return answer