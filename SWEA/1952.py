def dfs(month, sum):
    global result # 결과 값 변수 글로벌 처리

    # 종료 조건
    if month > 12:
        result = min(sum, result)
        return result  # 최솟값 비교
    # 재귀
    dfs(month+1, sum + day * month_list[month])
    dfs(month+1, sum + mon)
    dfs(month+3, sum + mon3)


T = int(input())
for test_case in range(1, T + 1):
    day, mon, mon3, year = map(int, input().split())
    month_list = [0] + list(map(int, input().split()))

    #결과를 출력할 변수(최댓값으로 초기화)
    result = 3000*12

    ans = dfs(1, 0) # 1월부터 시작이므로 1고정, 0으로 sum 초기화

    if result > year:
        result = year
    # 결과값 출력
    print(f'#{test_case} {result}')