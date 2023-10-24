import sys
input = sys.stdin.readline

N = int(input())
seat = [ [0,0] for _ in range(N+1) ]
student = []
visited = [False] * (N+1)
for i in range(N*N):
    student.append(list(map(int, input().split())))

for i in student:
    