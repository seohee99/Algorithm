import sys
input = sys.stdin.readline

N, M = map(int, input().split())

train = [[False] * 20 for _ in range(N+1)]

for _ in range(M):
    order = list(map(int, input().split()))

    if order[0] == 1:
        if train[order[1]][order[2]-1] == False:
            train[order[1]][order[2]-1] = True

    elif order[0] == 2:
        if train[order[1]][order[2]-1] == True:
            train[order[1]][order[2]-1] = False

    elif order[0] == 3:
        for j in range(19,0,-1):
            train[order[1]][j] = train[order[1]][j-1]
        train[order[1]][0] = False

    elif order[0] == 4:
        for j in range(19):
            train[order[1]][j] = train[order[1]][j+1]
        train[order[1]][19] = False

# 정답 리스트에 기차 하나씩 넣기 
answer = []
for i in range(1,N+1):
    if train[i] not in answer:
        answer.append(train[i])
print(len(answer))

