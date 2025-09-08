#출처 - https://programmers.co.kr/learn/courses/30/lessons/72414

def stoi(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def itos(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s

def solution(play_time, adv_time, logs):
    play_time = stoi(play_time)        
    adv_time = stoi(adv_time)               
    all_time = [0 for i in range(play_time + 1)]

    for l in logs:                           
        start, end = l.split('-')
        start = stoi(start)
        end = stoi(end)
        all_time[start] += 1
        all_time[end] -= 1

    for i in range(1, len(all_time)):      
        all_time[i] = all_time[i] + all_time[i - 1]

    for i in range(1, len(all_time)):      
        all_time[i] = all_time[i] + all_time[i - 1]

    most_view = 0                          
    max_time = 0                          
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < all_time[i] - all_time[i - adv_time]:
                most_view = all_time[i] - all_time[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < all_time[i]:
                most_view = all_time[i]
                max_time = i - adv_time + 1

    return itos(max_time)