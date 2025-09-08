"""근성은 나무에 관심이 많다.

평소 나무를 깨끗이 관리해 온 근성은 그 능력을 인정받아 북구청 청소행정과에 근무하게 되었다. 어느 날, 민규는 근성을 일하게 하기 위해 나무가 있는 위치에 쓰레기를 버리려고 한다. 나무는 수직선과 같은 일직선상에 있고 근성의 현재 위치는 원점이다. 아래의 두 가지 쿼리를 수행할 때 근성의 총 이동거리를 구하는 프로그램을 작성하시오.

1 x : 민규가 정수 좌표 x에 있는 나무에 쓰레기를 버린다.
2 : 근성은 현재 위치에서 시작하여 쓰레기가 있는 나무 중 가장 가까운 나무로 이동하여 쓰레기를 수거하고, 모든 쓰레기를 수거할 때까지 이 행동을 반복한다. 만약 현재 위치에서 가장 가까운 나무가 두 그루 이상이라면, 좌표가 가장 작은 나무로 이동한다.


입력
첫 번째 줄에 쿼리의 개수 
N이 주어진다.

두 번째 줄부터 
N개의 줄에 걸쳐 본문에 주어진 것과 같은 형식의 쿼리가 한 줄에 하나씩 주어진다.

출력
근성의 총 이동거리를 출력한다.

제한

1 <= N <= 200,000
-10^8 <= x <= 10^8
입력으로 주어지는 모든 수는 정수이다.
2번 쿼리가 하나 이상 주어진다.

예제 입력
7
1 4
1 2
1 -2
2
1 0
2
1 5

예제 출력
12



4
1 3
1 3
1 3
2
"""
# import sys
# input = sys.stdin.readline

# now = 0
# low = 10**8
# high = -10**8
# trash = 0
# n = int(input())
# answer = 0
# for i in range(n):
#     input_query = list(map(int,input().split()))
    
#     if input_query[0] == 1:
#         x = input_query[1]
#         low = min(low, x)
#         high = max(high, x)
    
#     if input_query[0] == 2:
#         nl = abs(now -low)
#         nh = abs(now - high)
#         if nl >= nh:
#             answer += high - low + nh
#             now = low
#             high,low = -10**8,10**8
#         if nl < nh:
#             answer += high - low + nl
#             now = high
#             high,low = -10**8,10**8
# print(answer)
    
# import sys
# input = sys.stdin.readline

# now = 0
# low = 10**8
# high = -10**8
# trash = 0
# n = int(input())
# answer = 0
# for i in range(n):
#     input_query = list(map(int,input().split()))
    
#     if input_query[0] == 1:
#         x = input_query[1]
#         low = min(low, x)
#         high = max(high, x)
#         trash+=1
    
#     if input_query[0] == 2 and trash !=0:
#         nl = abs(now -low)
#         nh = abs(now - high)
#         if nl >= nh:
#             answer += high - low + nh
#             now = low
#             high,low = -10**8,10**8
#         if nl < nh:
#             answer += high - low + nl
#             now = high
#             high,low = -10**8,10**8
#         trash = 0
# print(answer)

# import sys
# input = sys.stdin.readline

# def solve(n):
#     now = 0
#     low = 10**8+1
#     high = -10**8-1
#     trash = 0
#     answer = 0
    
#     for i in range(n):
#         input_query = list(map(int,input().split()))
        
#         if input_query[0] == 1:
#             x = input_query[1]
#             low = min(low, x)
#             high = max(high, x)
#             trash+=1
        
#         if input_query[0] == 2 and trash !=0:
#             nl = abs(now - low)
#             nh = abs(now - high)
#             if nl > nh:
#                 answer += high - low + nh
#                 now = low
#             elif nl <= nh:
#                 answer += high - low + nl
#                 now = high
#             high,low = -10**8-1,10**8+1
#             trash = 0
#     return answer

# n = int(input())
# print(solve(n))



import sys, random
input = sys.stdin.readline
sys.setrecursionlimit(1 << 25)

# --- Treap 노드 정의 ---
class Node:
    __slots__ = ("key", "prio", "l", "r")
    def __init__(self, key):
        self.key = key
        self.prio = random.randrange(1 << 30)  # 무작위 우선순위
        self.l = None  # 왼쪽 자식
        self.r = None  # 오른쪽 자식

# --- 회전 연산 ---
def rotR(p):  # 우회전
    q = p.l
    p.l = q.r
    q.r = p
    return q

def rotL(p):  # 좌회전
    q = p.r
    p.r = q.l
    q.l = p
    return q

# --- 삽입 ---
def insert(p, k):
    if not p:
        return Node(k)
    if k == p.key:
        return p  # 중복은 무시 (문제 조건상 x는 겹칠 수 있음)
    if k < p.key:
        p.l = insert(p.l, k)
        if p.l.prio < p.prio:  # heap 성질 위반 시 우회전
            p = rotR(p)
    else:
        p.r = insert(p.r, k)
        if p.r.prio < p.prio:  # heap 성질 위반 시 좌회전
            p = rotL(p)
    return p

# --- 삭제 ---
def erase(p, k):
    if not p:
        return None
    if k < p.key:
        p.l = erase(p.l, k)
    elif k > p.key:
        p.r = erase(p.r, k)
    else:  # 해당 노드 삭제
        if not p.l and not p.r:
            return None
        if not p.l:  # 왼쪽이 없음 → 좌회전
            p = rotL(p)
            p.l = erase(p.l, k)
        elif not p.r:  # 오른쪽이 없음 → 우회전
            p = rotR(p)
            p.r = erase(p.r, k)
        else:  # 양쪽 다 있음 → 우선순위 낮은 쪽으로 회전
            if p.l.prio < p.r.prio:
                p = rotR(p)
                p.r = erase(p.r, k)
            else:
                p = rotL(p)
                p.l = erase(p.l, k)
    return p

# --- 보조 함수: floor/ceil ---
def floor_key(p, x):
    """x 이하 최대값"""
    cur, ans = p, None
    while cur:
        if x < cur.key:
            cur = cur.l
        else:
            ans = cur.key
            cur = cur.r
    return ans

def ceil_key(p, x):
    """x 이상 최소값"""
    cur, ans = p, None
    while cur:
        if x > cur.key:
            cur = cur.r
        else:
            ans = cur.key
            cur = cur.l
    return ans

# --- 메인 풀이 ---
def solve():
    n = int(input())
    root = None  # Treap 루트
    now = 0      # 현재 근성 위치
    total = 0    # 전체 이동 거리

    for _ in range(n):
        q = input().split()
        if q[0] == '1':  # 쓰레기 추가
            x = int(q[1])
            root = insert(root, x)
        else:  # q[0] == '2' → 쓰레기 전부 수거
            while root is not None:
                L = floor_key(root, now)  # 현재 위치 기준 왼쪽 가장 가까운
                R = ceil_key(root, now)   # 오른쪽 가장 가까운

                # 가까운 쪽 선택 (같으면 더 작은 좌표 L)
                if L is None:
                    target = R
                elif R is None:
                    target = L
                else:
                    dL = now - L
                    dR = R - now
                    target = L if dL <= dR else R

                # 이동 거리 누적 & 위치 갱신
                total += abs(now - target)
                now = target
                # 해당 쓰레기 제거
                root = erase(root, target)

    print(total)

if __name__ == "__main__":
    solve()
