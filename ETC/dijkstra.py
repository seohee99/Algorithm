n,m = map(int, input().split())
k = int(input())
INF = 1e8

graph = [ [] for _ in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v,w)) # 거리와 노드 정보 입력

import heapq

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start)) # 우선순위, 값 형태
    distance[start] = 0 # 시작 노드의 거리는 0

    while q:
        dist, now = heapq.heappop(q) # 우선순위가 가장 낮은 값(가장 작은 거리)이 pop

        if distance[now] < dist: # 이미 입력되어있는 값이 현재 노드까지 거리보다 작으면, 이미 방문한 노드이므로 넘어감
            continue

        for i in graph[now]: # 연결된 모든 노드 검색
            if dist + i[1] < distance[i[0]]: # 기존에 입력되어있는 값보다 크면
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist + i[1], i[0]))

dijkstra(k)
print(distance)

"""
5 6
1
5 1 1
1 2 1
1 3 3
2 3 1
2 4 5
3 4 2

"""
