#출처 - https://programmers.co.kr/learn/courses/30/lessons/67260


def solution(n, path, order):
    	
    tree = [[] for _ in range(n)]
    for v1, v2 in path:
        tree[v1].append(v2)
        tree[v2].append(v1)
        
    orders =[0 for i in range(n)]
    for pre, post in order:
        orders[post] = pre
    
    
    num_visit = 0
    
    visited = [False for i in range(n)]
    q = [0]
    
    after ={}
    
    while q:
        here = q.pop(0)
        
        if orders[here] and not visited[orders[here]]:
            after[orders[here]] = here
            continue
        
        visited[here] = True
        num_visit +=1
    	
        for there in tree[here]:
            if not visited[there]:     
                q.append(there)
        
        if here in after:
            q.append(after[here])
                    
    return n == num_visit