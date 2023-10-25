import sys

input = sys.stdin.readline

N = int(input())
arr = []
dp = [1] * N

# 입력 초기화
for i in range(N):
    arr.append(int(input()))

# LIS, 최장 증가 수열
for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))


