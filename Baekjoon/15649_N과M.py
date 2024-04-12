import sys
input = sys.stdin.readline()

N, M = map(int, input.split())

visited = [False] * (N+1)
answer = [] # 정답을 담을 stack

def dfs():
    if len(answer) == M:
        for i in answer:
            print(i, end=' ')
        print()
        return

    for i in range(1, N+1):
        if visited[i] == True:
            continue
        visited[i] = True
        answer.append(i)
        dfs()
        answer.pop()
        visited[i] = False
dfs()