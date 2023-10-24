import sys

input = sys.stdin.readline

def dfs(n,m,s, visited):
    global answer
    if m == M:
        print("n, m" , n, m)
        n, m = n + 1, 0
    # 종료 조건
    if n == N :
        answer = max(answer, s)
        print("answer :: ",answer)
        return

    # 4가지 방향에 대해 모양확인 후 다음으로 이동
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 움직일 수 있는 좌표
    right = [n + dx[0], m + dy[0]]
    left = [n + dx[2], m + dy[2]]
    up = [n + dx[3], m + dy[3]]
    down = [n + dx[1], m + dy[1]]
    # o o
    # o
    if (0 <= right[0] < N and 0 <= right[1] < M and not visited[right[0]][right[1]]) and (0 <= down[0] < N and 0 <= down[1] < M and not visited[down[0]][down[1]]) :
        visited[right[0]][right[1]] = True
        visited[down[0]][down[1]] = True
        visited[n][m] = True
        # print(i, j, "1 :: ", s + 2*arr[n][m] + arr[right[0]][right[1]] + arr[down[0]][down[1]])
        dfs(n, m+1, s + 2*arr[n][m] + arr[right[0]][right[1]] + arr[down[0]][down[1]], visited)
        visited[right[0]][right[1]] = False
        visited[down[0]][down[1]] = False
        visited[n][m] = False

    # o o
    #   o
    if (0 <= left[0] < N and 0 <= left[1] < M and not visited[left[0]][left[1]]) and (0 <= down[0] < N and 0 <= down[1] < M and not visited[down[0]][down[1]]) :
        visited[left[0]][left[1]] = True
        visited[down[0]][down[1]] = True
        visited[n][m] = True
        # print(i, j, "2 :: ", s + 2*arr[n][m] + arr[left[0]][left[1]] + arr[down[0]][down[1]])
        dfs(n, m+1, s + 2*arr[n][m] + arr[left[0]][left[1]] + arr[down[0]][down[1]], visited)
        visited[left[0]][left[1]] = False
        visited[down[0]][down[1]] = False
        visited[n][m] = False

    # o 
    # o o
    if (0 <= right[0] < N and 0 <= right[1] < M and not visited[right[0]][right[1]]) and (0 <= up[0] < N and 0 <= up[1] < M and not visited[up[0]][up[1]]) :
        visited[right[0]][right[1]] = True
        visited[up[0]][up[1]] = True
        visited[n][m] = True
        # print(i, j, "3 :: ", s + 2*arr[n][m] + arr[right[0]][right[1]] + arr[up[0]][up[1]])
        dfs(n, m+1, s + 2*arr[n][m] + arr[right[0]][right[1]] + arr[up[0]][up[1]], visited)
        visited[right[0]][right[1]] = False
        visited[up[0]][up[1]] = False
        visited[n][m] = False


    #   o
    # o o
    if (0 <= left[0] < N and 0 <= left[1] < M and not visited[left[0]][left[1]]) and (0 <= up[0] < N and 0 <= up[1] < M and not visited[up[0]][up[1]]) :
        visited[left[0]][left[1]] = True
        visited[up[0]][up[1]] = True
        visited[n][m] = True
        # print(i, j, "4 :: ", s + 2*arr[n][m] + arr[left[0]][left[1]] + arr[up[0]][up[1]])
        dfs(n, m+1, s + 2*arr[n][m] + arr[left[0]][left[1]] + arr[up[0]][up[1]], visited)
        visited[left[0]][left[1]] = False
        visited[up[0]][up[1]] = False
        visited[n][m] = False




N, M = map(int, input().split())
arr = []
visited = [[False] * M for _ in range(N)]
for i in range(N):
    arr.append(list(map(int, input().split())))

answer = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j] : 
            visited[i][j] = True
            print("***")
            dfs(i,j,answer,visited)
            visited[i][j] = False

print(answer)

