import sys
input = sys.stdin.readline

def dfs(n, sum):
    global count
    # 종료 조건
    if n == N :
        if sum == S:
            count += 1
        return
    
    
    dfs(n+1, sum) # 선택 X
    dfs(n+1, sum + arr[n]) # 선택
 
    

N, S = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
dfs(0, 0)
if S == 0:
    print(count-1)
else:
    print(count)