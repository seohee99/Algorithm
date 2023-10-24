T = int(input())
for test_case in range(1, T):
    n, m, c = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    graph = [list(map(int, input().split())) for _ in range(n)]

    ans = mx = sm1 = 0
    mem = [ [0] * n for _ in range(n) ]

    def dfs(n, cnt, sm, ci, cj):
        global mx
        if cnt > c:
            return # 합친 꿀의 양이 c보다 큰 경우

        if n == m :
            mx = max(mx, sm)
            return

        # 선택하는 경우 sm 업데이트
        dfs(n+1, cnt+graph[cj][cj+n], sm + graph[ci][cj+n], ci,cj)
        # 선택하지 않는 경우 n만 증가시켜 종료 조건 맞추고 종료하게끔
        dfs(n+1, cnt, sm , ci,cj)


    for i in range(n):
        for j in range(n-m+1):
            mx = 0
            dfs(0, 0, 0, i, j)
            mem[i][j] = mx

    for i1 in range(n):
        for i2 in range(n-m+1): # 연속으로 n개 선택해야하는데 범위를 넘어가면 안되므로 n-m+1까지만 갈 수 있도록
            for j1 in range(i1, n): # i1이 끝나는 열에서부터 시작
                sj = j1 + m if i1 == i2 else 0
                for j2 in range(sj, n-m+1):
                    ans = max(ans, mem[i1][j1] + mem[i2][j2])