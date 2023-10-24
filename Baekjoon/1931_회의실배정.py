import sys
input = sys.stdin.readline

N = int(input())
meetings = []

for i in range(N):
    meeting = list(map(int, input().split()))
    meetings.append(meeting)
meetings.sort(key=lambda x:(x[1], x[0]))

answer = 1
end_time = meetings[0][1] # 가장 첫번째 회의 끝나는 시간
for i in range(1,N):
    if meetings[i][0] >= end_time:
        answer += 1
        end_time = meetings[i][1]
print(answer)


