def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver = 0  # 남은 배달 가능 개수
    pick = 0  # 남은 수거 가능 개수

    # 먼 집부터 모든 배달, 수거 처리
    for i in range(n - 1, -1, -1):
        # 물류 창고에 다녀오는 수 카운트
        cnt = 0
        while deliver < deliveries[i] or pick < pickups[i]:
            cnt += 1
            deliver += cap
            pick += cap

        # 배달, 수거 처리
        deliver -= deliveries[i]
        pick -= pickups[i]

        answer += (i + 1) * cnt
    return answer * 2