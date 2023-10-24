from collections import deque
def solution(n, results):
    game = [ [] for _ in range(n+1)]
    rank = [ [] for _ in range(n+1)]

    
    # 게임 결과 저장(방향O 인접 리스트)
    for result in results:
        a, b = result[0], result[1]
        game[a].append(b)
        
    # bfs
    # 각 선수에 대해 경기 정보를 가지고 있는 선수들을 리스트에 넣었음
    def bfs(N):
        visited = [False] * (n+1)
        print(visited)
        q = deque()
        q.append(N)
        
        visited[N] = True
        
        
        while(q):
            c = q.popleft()
            
            for i in game[c]:
                
                if visited[i] == False:
                    if i not in rank[N] : rank[N].append(i)
                    if N not in rank[i] : rank[i].append(N)
                    q.append(i)
                    visited[i] = True
                
    
    # 각 선수에 대해 경기 정보 정리
    for i in range(1,n+1):
        bfs(i)
        
    # 자기 자신 제외하고 모든 경기 정보를 가지고 있으면 answer + 1
    answer = 0
    for i in rank:
        if len(i) == (n-1) :
            answer += 1
    
    return answer