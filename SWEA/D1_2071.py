T = int(input())

for tc in range(1,T+1):
    arr = list(map(int, input().split()))
    sum, mean = 0, 0

    for i in arr:
        sum += i
    mean = round(sum/10)
    print(f'#{tc} {mean}')
