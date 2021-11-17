def solution(N, number):
    answer = -1
    calc_list = []
    for i in range(1,9):
        calc = set()
        calc.add(int(str(N)*i))
        for j in range(0,i-1):
            for a in calc_list[j]:
                for b in calc_list[-j-1]:
                    calc.add(a-b)
                    calc.add(a+b)
                    calc.add(a*b)
                    if b != 0:
                        calc.add(a//b)
        if number in calc:
            answer = i
            break
        calc_list.append(calc)                    
    return answer

print(solution(2,11))