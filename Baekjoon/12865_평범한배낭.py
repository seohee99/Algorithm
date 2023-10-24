import sys

input = sys.stdin.readline

N, K = map(int, input().split())

W_arr = []
V_arr = []

for i in range(N):
    W, V = map(int, input().split())
    for idx, j in enumerate(W_arr):
        if j + W <= K :
            V_arr[idx] += V
            W_arr[idx] += W
    W_arr.append(W)
    V_arr.append(V)


print(max(V_arr))
