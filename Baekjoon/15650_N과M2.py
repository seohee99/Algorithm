# N과 M (2)
# 자연수 N, M이 주어졌을 때, 1부터 N까지 자연수 중에서 중복없이 M개를 고른 수열 출력(오름차순)
import sys
input = sys.stdin.readline()

N, M = map(int, input.split())

visited = [False] * (N+1)
answer = [] # 정답을 담을 stack

def dfs(n):
    if len(answer) == M:
        for i in answer:
            print(i, end=' ')
        print()
        return

    for i in range(n, N+1): # 이전 자릿수보다 크게
        if visited[i] == True:
            continue
        visited[i] = True
        answer.append(i)
        dfs(i+1) # i+1
        answer.pop()
        visited[i] = False
dfs(1)

