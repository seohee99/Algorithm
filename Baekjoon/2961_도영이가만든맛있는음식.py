import sys
input = sys.stdin.readline

gradient = []
N = int(input())
for i in range(N):
    flavor = list(map(int, input().split()))
    gradient.append(flavor)

answer = 1000000000

def dfs(n, S, B):
    global answer
    
    # 종료 조건
    if n == N:
        if B > 0 and answer > abs(S-B):
            answer = abs(S-B)
        return 
    
    
    dfs(n+1, S * gradient[n][0], B + gradient[n][1])
    dfs(n+1, S, B)
    

dfs(0, 1, 0)
print(answer)