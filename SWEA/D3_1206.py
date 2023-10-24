T = 10

# 아이디어 : 건물의 양쪽 2개씩 층수 확인 후 4개의 건물 중 가장 높은 건물의 층 뺌
for tc in range(1,T+1):
    n = int(input())
    building_list = list(map(int, input().split()))

    answer = 0
    for i in range(2, n-2):
        max_height = max(building_list[i-2],building_list[i-1],building_list[i+1],building_list[i+2])
        if building_list[i] - max_height >= 0:
            answer += (building_list[i] - max_height)

    print(f'#{tc} {answer}')