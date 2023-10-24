# N과 M (1)
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

visited = [False] * (N+1)
answer = [] # 정답을 담을 stack

# 재귀 함수로 숫자 선택 반복
def dfs(n):
    # 종료조건
    if (len(answer) == M):
        for _ in answer : print(_, end=" ")
        print()
        return
    
    for i in range(1, N+1):
        if visited[i]: continue
        
        visited[i] = True
        answer.append(i)
        dfs(n+1) # 다음 꺼 뽑으러 다음 단계로
        answer.pop()
        visited[i] = False

dfs(0)




























# n, m = map(int, input().split())

# s = [] # m개의 수열 저장하는 리스트
# visited = [False] * (n+1)
# def dfs():
#     if len(s) == m: # 리스트에 m개가 append 되면 재귀 종료
#         print(' '.join(map(str, s)))
#         return

#     for i in range(1, n+1):
#         if visited[i]:
#             continue
#         visited[i] = True
#         s.append(i)
#         dfs()
#         s.pop()
#         visited[i] = False
# dfs()