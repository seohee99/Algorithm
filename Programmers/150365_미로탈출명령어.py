import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
direction = ['d', 'l', 'r', 'u']
answer = "z"


# dfs(격자n, 격자m, 출발위치x,출발위치y, 도착위치r, 도착위치c, 이동경로, 이동횟수, 거리k)
def dfs(n, m, x, y, r, c, route, cnt, k):
    global answer
    # 현재 이동횟수와 남은 거리가 k보다 크면 return
    if k < cnt + abs(x - r) + abs(y - c):
        return

    # 종료 조건
    if x == r and y == c and cnt == k:
        answer = route
        return

    # 4방향 돌리기
    for i in range(4):
        # 이동경로가 최적(사전순으로 가장 빠른 경로)이 되도록 조건 설정
        if (1 <= x + dx[i] and x + dx[i] <= n and 1 <= y + dy[i] and y + dy[i] <= m) and route < answer:
            dfs(n, m, x + dx[i], y + dy[i], r, c, route + direction[i], cnt + 1, k)


def solution(n, m, x, y, r, c, k):
    dist = abs(x - r) + abs(y - c)
    # 출발지점, 도착지점의 거리가 k 보다 크거나 k-dist가 홀수인 경우 impossible
    # 안해주면 시간초과남..
    if dist > k or (k - dist) % 2 == 1:
        return "impossible"

    dfs(n, m, x, y, r, c, "", 0, k)

    return answer
