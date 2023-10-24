import sys
import heapq

def get_distance(x1, y1, x2, y2):
    return (abs(x1-x2)**2 + abs(y1-y2)**2)**0.5

def Dijkstra(start):    
    q = []
    heapq.heappush(q, [0, 1])
    distances[start] = 0

    while q:
        cur_cost, cur_node = heapq.heappop(q)

        # 이미 입력되어있는 값이 현재 노드까지 거리보다 작으면, 이미 방문한 노드이므로 넘어감
        if distances[cur_node] < cur_cost: continue

        # 연결된 노드 검색
        for next_node, next_cost in graph[cur_node]:
            if distances[next_node] > cur_cost + next_cost: # 기존에 입력되어있는 값보다 크면
                distances[next_node] = cur_cost + next_cost
                heapq.heappush(q, [cur_cost + next_cost, next_node])
                
    return int(distances[N]*1000)

input = sys.stdin.readline
INF = 10e9
N, W = map(int, input().split())
M = float(input())

plant = [[0, 0]]
graph = [ [] for _ in range(N+1) ]
distances = [INF for _ in range(N+1)]

for _ in range(N):
    a, b = map(int, input().split())
    plant.append([a, b])

# 두 발전소 사이 거리(가중치)를 구해서 넣음
for i in range(1, N+1):
    for j in range(i+1, N+1):
        dist = get_distance(plant[i][0], plant[i][1], plant[j][0], plant[j][1])
        if dist <= M:
            graph[i].append([j, dist])
            graph[j].append([i, dist])

# 이미 존재하는 전선에 대해 가중치 0으로 설정
for _ in range(W):
    a, b = map(int,input().split())
    graph[a].append([b, 0])
    graph[b].append([a, 0])

ans =Dijkstra(1)
print(ans)