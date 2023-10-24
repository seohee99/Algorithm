T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    max_num = 0

    for i in arr:
        if i > max_num:
            max_num = i

    print(f'#{tc} {max_num}')