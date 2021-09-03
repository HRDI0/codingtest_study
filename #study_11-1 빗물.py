# 2차원 세계에 블록이 쌓여있다. 비가 오면 블록 사이에 빗물이 고인다.

# 0 0 0 0 1 0 0 0        0 0 0 0 1 0 0 0
# 1 0 0 1 1 0 0 0   ->   1 2 2 1 1 0 0 0
# 1 0 1 1 1 0 0 1        1 2 1 1 1 2 2 1
# 1 1 1 1 1 1 1 1        1 1 1 1 1 1 1 1

# 비는 충분히 많이 온다. 고이는 빗물의 총량은 얼마일까?

# 입력
# 첫 번째 줄에는 2차원 세계의 세로 길이 H과 2차원 세계의 가로 길이 W가 주어진다. (1 ≤ H, W ≤ 500)
# 두 번째 줄에는 블록이 쌓인 높이를 의미하는 0이상 H이하의 정수가 2차원 세계의 맨 왼쪽 위치부터 차례대로 W개 주어진다.
# 따라서 블록 내부의 빈 공간이 생길 수 없다. 또 2차원 세계의 바닥은 항상 막혀있다고 가정하여도 좋다.

# 출력
# 2차원 세계에서는 한 칸의 용량은 1이다. 고이는 빗물의 총량을 출력하여라.
# 빗물이 전혀 고이지 않을 경우 0을 출력하여라.

h,w = map(int, input().split())
block_list = list(map(int, input().split()))


result = 0
for i in range(1,w-1):
    l_flag = False
    r_flag = False
    for raindrop in range(h - block_list[i],0,-1):
        for left in range(0,i):
            if block_list[left] >= raindrop + block_list[i]:
                l_flag = True
                break
        for right in range(i+1,w):
            if block_list[right] >= raindrop + block_list[i]:
                r_flag = True
                break
        if l_flag == True and r_flag == True:
            result += raindrop
            break
print(result)

# tall = block_list[0]
# second = block_list[0]
# count = 0
# m_block = 0
# result = 0
# for i in range(1,w):

#     if block_list[i] >= tall:
#         result += ((tall * count) - m_block)
#         m_block = 0
#         count = 0
#         tall = block_list[i]
#     else:
#         if i == (w -1):
#             result += ((block_list[i] * count) - m_block)
#         count += 1
#         m_block += block_list[i]
   
# print(result)