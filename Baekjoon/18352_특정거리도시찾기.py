import sys
from collections import deque

# 모든 간선이 1이므로 bfs 수행
def bfs(n):
    q = deque([n])
    visited[n] = True
    distance[n] = 0
    answer = []

    while q:
        c = q.popleft()
        for i in graph[c]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                distance[i] = distance[c] + 1
                if distance[i] == K:
                    answer.append(i)
    return answer

input = sys.stdin.readline
N, M, K, X = map(int, input().split())
graph = [ [] for _ in range(N+1) ]
distance = [0] * (N+1)
visited = [False] * (N+1)

# 도로 정보 초기화
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

# 출발도시 X에 대해 BFS 수행
ans = bfs(X)

# 정답 출력, 단 최단 거리가 K인 도시가 하나도 없으면 -1 출력
if len(ans) == 0:
    print(-1)
else:
    for i in sorted(ans):
        print(i)

