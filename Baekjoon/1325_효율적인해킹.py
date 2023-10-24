import sys
from collections import deque
input = sys.stdin.readline

def bfs(n):
    q = deque([n])
    visited = [False] * (N+1)
    visited[n] = True

    while q:
        t = q.popleft()
        for i in graph[t]:
            if not visited[i] :
                visited[i] = True
                q.append(i)
                trust[n] += 1 # 신뢰할 수 있는 컴퓨터의 개수 +1
 
N, M = map(int, input().split())
graph = [ [] for _ in range(N+1) ] 
trust = [1] * (N+1)

# 입력 값 인접 리스트로 초기화
for _ in range(M):
    t = list(map(int,input().split()))
    graph[t[1]].append(t[0])

# N개의 컴퓨터에 대해 bfs 수행
for i in range(1,N+1):
    bfs(i)

# Max값에 대해 오름차순 출력
max_trust = max(trust)
for i in range(1, N+1):
    if trust[i] == max_trust:
        print(i, end="")
