INF = int(1e9) # 무한을 의미, 10억

n = int(input())
m = int(input())
graph = [ [INF] * (n+1) for _ in range(n+1) ] # 2차원 그래프, INF로 초기화

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j: graph[i][j] = 0 # 자기 -> 자기는 0으로 초기화

# 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split()) # a에서 b로가는 비용 c
    graph[a][b] = c

# 플로이드 워셜 알고리즘
# k는 시작 노드
for k in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if graph[a][b] == 1e9:
            print("INFINITY", end=" ")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[a][b], end=" ")
    print()