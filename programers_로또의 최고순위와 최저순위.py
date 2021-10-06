def solution(lottos, win_nums):
    same = 7                    #지워진 번호가 모두 틀렸을 경우
    z_same = 7                  #지워진 번호가 모두 맞았을 경우
    answer = []
    for n in lottos:            #현재 번호들이 당첨번호에 포함 되는가
        if n != 0 and (n in win_nums):  #0이 아닌 번호중 당첨번호가 있을 때
            same -= 1
            z_same -=1
        if n == 0:                      #0이 모두 당첨번호라고 판단
            z_same -=1
    if z_same == 7:                     #당첨번호가 0개인 경우 처리
        z_same -=1
    if same == 7:                       #당첨번호가 0개인 경우 처리
        same -=1
    answer.append(same)
    answer.append(z_same)
    answer.sort()
    return answer

loto = [0, 0, 0, 0, 0, 0]
win = [38, 19, 20, 40, 15, 25]	
solution(loto,win)


# def solution(lottos, win_nums):

#     rank=[6,6,5,4,3,2,1]

#     cnt_0 = lottos.count(0)
#     ans = 0
#     for x in win_nums:
#         if x in lottos:
#             ans += 1
#     return rank[cnt_0 + ans],rank[ans]