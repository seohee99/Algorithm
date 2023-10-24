T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [ [0] * N for _ in range(N)]

    # # 오른쪽 -> 아래 -> 왼쪽 -> 위
    dx = [0, 1, 0, -1] # 세로
    dy = [1, 0, -1, 0] # 가로
    d = 0 # 이동방향
    num = 1 # 채울 숫자
    x, y = 0, -1 # 초기 좌표

    while num <= N*N:
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0 :
            arr[nx][ny] = num
            x = nx
            y = ny
            num += 1
        else: # 범위 나가면
            d = (d + 1) % 4

    print(f'#{tc}')
    for i in arr:
        for j in i:
            print(j, end=' ')
        print()