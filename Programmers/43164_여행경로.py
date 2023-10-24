"""
참고 사이트
https://wwlee94.github.io/category/algorithm/bfs-dfs/travel-route/
https://scarletbreeze.github.io/articles/2019-07/pythonKit%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4%287%29%28DFS,BFS%29%EC%97%AC%ED%96%89%EA%B2%BD%EB%A1%9C
"""
from collections import defaultdict

def solution(tickets):
    # 티켓 정보 초기화 (dict)
    routes = defaultdict(list)
    for key, value in tickets:
        routes[key].append(value)
        
    # 여행 경로 알파벳 역순으로 정렬(pop할 때 알파벳 순으로)
    for route in routes:
        routes[route].sort(reverse=True)
    
    def dfs():
        # ICN부터 시작 
        stack = ["ICN"]
        path = []
        while stack:
            c = stack[-1]
            if (c not in routes) or (len(routes[c]) == 0):
                path.append(stack.pop())
            else:
                # 방문할 수 있는 경로(routes에서 pop()해서 알파벳 순으로) stack에 넣음
                # 방문한 경로는 pop
                stack.append(routes[c].pop())
        return path[::-1]
    
    answer = dfs()      

    return answer