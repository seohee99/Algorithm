# N과 M (1)
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

visited = [False] * (N+1)
answer = [] # 정답을 담을 stack

# 재귀 함수로 숫자 선택 반복
def dfs(n):
    # 종료조건
    if (len(answer) == M): # M개만큼 뽑았으면 정답 출력
        for _ in answer : print(_, end=" ")
        print()
        return
    
    for n in range(n, N+1): # for문의 범위를 n부터 해서 중복 방지 **
        if visited[n]: continue # 이미 고른 숫자라면 continue
        
        visited[n] = True
        answer.append(n)
        dfs(n+1) # 다음 꺼 뽑으러 다음 단계로
        answer.pop() # answer에 넣은 숫자는 pop해줘야 다음 숫자를 담을 수 있음!
        visited[n] = False

dfs(1)

























# s = [] # m개의 수열 저장하는 리스트
# visited = [False] * (n+1)
# def dfs():
#     if len(s) == m: # 리스트에 m개가 append 되면 재귀 종료
#         print(' '.join(map(str, s)))
#         return

#     for i in range(1, n+1):
#         if visited[i]:
#             continue
#         if len(s) > 0:
#             if s[-1] > i:
#                 continue
#         visited[i] = True
#         s.append(i)
#         dfs()
#         s.pop()
#         visited[i] = False


# dfs()