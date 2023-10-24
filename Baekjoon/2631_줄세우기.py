import sys

input = sys.stdin.readline

N = int(input())
arr = []

# 3 7 5 2 6 1 4
# 입력 초기화
for _ in range(N):
    arr.append(int(input()))

idx = 1
count = 0
for i in range(N-1, N//2, -1):
    print("i",arr[i])
    if arr[i] == idx:
        arr.remove(idx)
        arr.insert(idx-1, idx)
        count += 1

# 마지막 아이 줄 세우기        
for i in arr:
    if i == N+1:
        if arr[N+1] != i:
            arr.remove(i)
            arr.append(i)
            count += 1

print(arr)
print(count)