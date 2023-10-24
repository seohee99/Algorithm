import sys
from collections import deque
input = sys.stdin.readline

def bfs(r,c):
    global count, flag
    q = deque([[r,c]])    
    
    move = [ [r,c] ]
    sum = ground[r][c]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    visited[r][c] = True

    while q:
        tr, tc = q.popleft()
        for i in range(4):
            nr = tr + dr[i]
            nc = tc + dc[i]

            if (0 <= nr < N and 0 <= nc < N) and not visited[nr][nc]:
                if L <= abs(ground[tr][tc] - ground[nr][nc]) <= R:
                    move.append([nr, nc])
                    visited[nr][nc] = True
                    q.append([nr,nc])
                    sum += ground[nr][nc]
                    
    
    if len(move) > 1:
        # 인구이동
        new_pop = sum // len(move)
        for i,j in move:
            ground[i][j] = new_pop
        flag = True

N, L, R = map(int, input().split())
ground = []
for i in range(N):
    ground.append(list(map(int, input().split())))


# 언제 인구이동을 할지랑, visited 배열을 잘 쓰자 ... 하..
count = 0
while 1:
    flag = False
    visited= [ [False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i,j)

    if flag == True:
        count += 1
    else : 
        break
print(count)