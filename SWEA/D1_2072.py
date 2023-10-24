T = int(input())

for tc in range(1,T+1):
    arr = list(map(int, input().split()))
    sum = 0
    for i in arr:
        if (i % 2) == 0:
            continue
        else:
            sum += i
    print(f'#{tc} {sum}')