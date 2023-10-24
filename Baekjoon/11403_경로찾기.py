import sys

input = sys.stdin.readline
N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int,input().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] and graph[k][j]:
                graph[i][j]=1

for r in graph:
    for c in r:
        print(c, end = " ")
    print()