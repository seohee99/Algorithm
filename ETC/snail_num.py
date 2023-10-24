# 범위 이내, visit == 0인경우 x,y좌표 바꿈
# else 방향 전환

T = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for test_case in range(1, T+10):
    n = int(input())
    arr = [[0] * n for _ in range(n)]

    i, j, cnt, dr = 0, 0, 1, 0 # 초기화 d: 방향벡터(0,1,2,3)
    arr[i][j] = cnt # arr값 채우기
    cnt += 1

    while cnt <= n*n:
        ni,nj = i + dx[dr], i + dy[dr]
        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 0: # 범위 내에 있으면 방향에 맞게 좌표 업데이트해서 값 넣어주기
            i, j = ni, nj
            arr[i][j] = cnt
            cnt += 1
        else: # 범위 밖으로 나가면
            dr = (dr + 1) % 4 # 방향 바꿔주고 4로 나눈 나머지로 dr 업데이트


