import sys
input = sys.stdin.readline


def dfs(n, s, m):
    global answer

    if n == N:
        answer = min(answer, s+arr[m][0])
        return

    for k in range(1,N):
        if arr[m][k] > 0 and not visited[k]:
            visited[k] = True 
            dfs(n+1, s+arr[m][k], k)
            visited[k] = False



T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [ [0] * (N) for _ in range(N) ]
    # 입력 초기화
    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(N):
            arr[i][j] = temp[j]
    
    visited = [False] * (N+1)
    
    answer = 100000 # max init
    dfs(1,0,0) # n, sum, start
    print(answer)

    
