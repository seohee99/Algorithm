dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, sm, depth):
    global ans

    # 종료 조건
    if depth == 3:
        ans = max(ans, sm)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 넘어가면 continue
        # if nx < 0 or nx >= n or ny < 0 or ny >= m:
        #     continue

        if (0 <= nx < n) and (0 <= ny < m) and visit[nx][ny] == 0:
            if depth == 1:
                visit[nx][ny] = 1
                dfs(x, y, sm + graph[nx][ny], depth + 1)
                visit[nx][ny] = 0
            visit[nx][ny] = 1
            dfs(nx, ny, sm + graph[nx][ny], depth + 1)
            visit[nx][ny] = 0

n, m = map(int, input().split())
graph = [ list(map(int, input().split())) for _ in range(n)]
ans = 0
visit = [ [0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        visit[i][j] = 1
        dfs(i, j, graph[i][j], 0)
        visit[i][j] = 0

print(ans)