def solution(lines):
    answer = 0
    log_list = get_log(lines)
    size = len(log_list)
    
    for i in range(size):
        pcount = 1
        a_end = log_list[i][1]
        
        for j in range(size):
            if j == i:
                continue
            
            b_start = log_list[j][0]
            b_end = log_list[j][1]
            
            if a_end <= b_start < a_end + 1000:
                pcount +=1
            elif a_end <= b_end < a_end + 1000:
                pcount +=1
            elif b_start <= a_end and a_end + 1000 <= b_end:
                pcount +=1
                
        answer = max(answer,pcount)
    return answer

def get_log(lines):
    time_list = []
    for line in lines:
        date,tt,pts = line.split()
        hh,mm,ss = tt.split(':')
        
        ss1,ss2 = ss.split('.')
        ss = (int(ss1) * 1000) + int(ss2)
        
        end_time = (int(hh)*3600000) + (int(mm)*60000) + ss
        
        pts = int(float(pts[:-1]) * 1000)
        
        start_time = end_time - pts + 1
        time_list.append((start_time,end_time))
    return time_list
        

test_case = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]

test_case2 = [
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]
print(solution(test_case))