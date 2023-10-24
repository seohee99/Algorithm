V, E = map(int, input().split())

distance = [ [1e9] * (V + 1) for _ in range(V + 1) ]

for _ in range(E):
    x, y, c = map(int, input().split())
    distance[x][y] = c

# 경유지 k, 출발지 i, 도착지 j로 3중 for문
for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

answer = 1e9
for i in range(1, V+1):
    answer = min(answer, distance[i][i]) # 사이클은 출발지와 도착지가 같으므로 i->i를 확인

if answer == 1e9 : print(-1)
else : print(answer)