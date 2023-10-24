T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())
    ans = ''
    if a > b :
        ans = '>'
    elif a < b:
        ans = '<'
    else:
        ans = '='
    print(f'#{tc} {ans}')