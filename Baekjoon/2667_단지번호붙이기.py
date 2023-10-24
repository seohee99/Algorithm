# import sys
# input = sys.stdin.readline
from collections import deque

def bfs(i,j):
    q = deque()
    visited[i][j] = True
    q.append((i,j))
    cnt = 1

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if (0 <= nx < n and 0 <= ny < n) and not visited[nx][ny] and (graph[nx][ny] ==1):
                visited[nx][ny] = True
                cnt += 1
                q.append((nx, ny))


    return cnt


n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(graph[0][1])
visited = [ [False] * n for _ in range(n) ]
answer = []

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(n):
    for j in range(n):
        if graph[i][j] > 0 and not visited[i][j]:
            answer.append(bfs(i,j))

print(len(answer))
print(answer)