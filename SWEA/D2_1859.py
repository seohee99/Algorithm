T = int(input())

for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    price = arr[-1] # 초기값
    total = 0
    for i in range(len(arr)-1,-1,-1):
        if arr[i] <= price:
            total += price - arr[i]
        elif arr[i] > price :
            price = arr[i]
    print(f'#{tc} {total}')