m, h, n = map(int, input().split())
visit = [ [False] * m+1 for _ in range(n+1) ]
result = [] # 양 옆에 사다리가 있으면 사다리를 놓을 수 없기 때문에 사다리를 놓여질 수 있는 후보 리스트
answer = 4
#visit에 이미 있는 사다리 방문 처리
for i in range(h):
    a, b = map(int, input().split())
    visit[a][b] = True

for i in range(1, n+1):
    for j in range(1, m):
        if not visit[i][j-1] and not visit[i][j] and not visit[i][j+1]:
            result.append([i, j])
# 모든 열에 대해 현재 i 번째 열이 사다리를 이돟애서 i 번째에 도학할 수 있는지 확인
# 해당 열에 대해 왼쪽에 사다리가 놓였다면 왼쪽으로 이동(now - 1), 현재 위치에 있다면 오른쪽으로 이동(now+1)
# 처음 출발한 열의 번호와 now(이동된 값)비교 후 True/False 반환
def check():
    for i in range(1, n+1):
        now = i
        for j in range(1, h+1):
            if visit[j][now-1]:
                now -= 1
            elif visit[j][now]:
                now += 1
        if now != i:
            return False
    return True

def dfs(depth, idx):
    global answer
    # 종료 조건
    if depth >= answer:
        return
    # 종료 조건
    if check():
        answer = depth
        return
    for c in range(idx, len(result)):
        x, y = result[c]
        if not visit[x][y-1] and not visit[x][y+1]:
            visit[x][y] = True
            dfs(depth+1, c+1)
            visit[x][y] = False

answer = 4
dfs(0, 0)