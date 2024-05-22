import sys

input = sys.stdin.readline

N = int(input())

dp = [0] * 301 # 계단의 개수는 300개까지이므로 301개로 초기화
stairs = [0] * 301

for i in range(1, N+1):
    stairs[i] = int(input())

dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]

for i in range(3, N+1):
    dp[i] = max(dp[i-2], dp[i-3] + stairs[i-1]) + stairs[i] # 2번째 전 + 현재 or 3번째 전 +  1번째 전 + 현재 => max값 찾기

print(dp[N])


# 참고
# https://velog.io/@highcho/Algorithm-baekjoon-2579