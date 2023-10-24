import sys
input = sys.stdin.readline

N, M = map(int, input().split())

route = []

for i in range(N):
    route.append(list(map(int, input().split())))


