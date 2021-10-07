
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 2 초	512 MB	12225	5635	4214	44.744%
# 문제
# 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

# 입력
# 첫째 줄에 N이 주어진다.

# 둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

# 출력
# 첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.

# 제한
# 1 ≤ N ≤ 1,000,000
# -109 ≤ Xi ≤ 109


# n = int(input())
# num_list = list(map(int,input().split()))
# sort_list = num_list.copy()
# sort_list.sort()
# zip_num = 0
# for i in sort_list:
#     if sort_list.count(i) == 1:
#         num_list[num_list.index(i)] = zip_num
#         zip_num +=1
#     else:
#         while(num_list.count(i)):
#             num_list[num_list.index(i)] = zip_num
#             del sort_list[sort_list.index(i)]
#         zip_num +=1
# print(num_list)

# n = int(input())
# num_list = list(map(int,input().split()))
# sort_list = num_list.copy()
# sort_list.sort()
# zip_num = 0
# for i in range(len(sort_list)):
#     for j in range(len(num_list)):
#         if num_list[j] == sort_list[i]:
#             num_list[j] = zip_num
#     if sort_list[i] != sort_list[i - 1]:
#         zip_num +=1
# print(num_list)

n = int(input())
num_list = list(map(int,input().split()))
sort_list = sorted(set(num_list))
sort_dict = {i:j for j,i in enumerate(sort_list)}
for i in num_list:
    print(sort_dict[i],end=' ')
