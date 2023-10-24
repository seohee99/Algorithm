from collections import deque

    
def solution(n, edge):
    
    # 간선 정보 인접 리스트로 저장(양방향)
    node = [ [] for _ in range(n+1) ]
    visited = [False] * (n+1)
    distance = [0] * (n+1)
    for v in edge:
        a, b = v[0], v[1]  
        node[a].append(b)
        node[b].append(a)
        
    
    
    # bfs
    def bfs(n):
        # 방문 정보 저장 
        visited[n] = True
        q = deque()
        q.append(n)
        
        # q에 노드 있으면 진행
        while(q):
            c = q.popleft()
            
            for i in node[c]:
                # 방문한 적 없다면 q에 넣고&방문 정보 업데이트
                if not visited[i]:
                    q.append(i)
                    
                    # 방문할 때 distance + 1
                    visited[i] = True
                    distance[i] = distance[c] + 1
                    
                    
                    
    # node 1에서 bfs 시작
    bfs(1)
    
    answer = 0
    for i in distance:
        if i == max(distance):
            answer += 1
            
    return answer