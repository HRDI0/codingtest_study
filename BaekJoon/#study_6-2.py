#study_6-2

input = int(input())
i = 0
pre_i = 1
a = 1
k = 0

while(1):
    i = pre_i + (6 * k)
    if(pre_i <= input <= i):
        print(a)
        break
    else:
        k += 1
        pre_i = i
        a += 1