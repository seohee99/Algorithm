dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, chance):
    global MAX, visit
    MAX = max(MAX, visit[r][c])

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if not(0 <= nc < n and 0 <= nr < n) or visit[nr][nc]:
            continue
        if A[r][c] > A[nr][nc]:
            visit[nr][nc] = visit[r][c] + 1
            dfs(nr, nc, chance)
            visit[nr][nc] = 0
        elif chance and A[nr][nc] - K < A[r][c]:
            temp = A[nr][nc]
            A[nr][nc] = A[r][c] - 1
            visit[nr][nc] = visit[r][c] + 1
            dfs(nr, nc, chance - 1)
            visit[nr][nc] = 0
            A[nr][nc] = temp # 되돌려놓기

# main
T = int(input())
for tc in range(T):
    n, K = map(int, input().split())
    A = []
    top = 0
    for i in range(n):
        A.append(list(map(int, input().split())))
        for j in range(n):
            if A[i][j] > top:
                top = A[i][j]
    MAX = 0
    visit = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if A[i][j] == top:
                visit[i][j] = 1
                dfs(i, j, 1)
                visit[i][j] = 0

    print("#{} {}".format(tc + 1, MAX))