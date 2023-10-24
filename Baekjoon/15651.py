# N과 M (1)
n, m = list(map(int, input().split()))

s = [] # m개의 수열 저장하는 리스트
visited = [False] * (n+1)
def dfs():
    if len(s) == m: # 리스트에 m개가 append 되면 재귀 종료
        print(' '.join(map(str, s)))
        return

    for i in range(1, n+1):
        s.append(i)
        dfs()
        s.pop()


dfs()