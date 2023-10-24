T = int(input())
## 아이디어 : 완전탐색으로 모든 자리를 바꿔본 후 최댓값 찾기

def dfs(chance):
    global answer
    # 종료 조건
    if chance == 0:
        answer = max(ans_list)
        return

    # 재귀
    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            # 스와핑
            num_list[i], num_list[j] = num_list[j], num_list[i]
            # 중복되지 않게 넣어주기
            if (''.join(num_list)) not in ans_list:
                ans_list.add(''.join(num_list))
                # 재귀
                dfs(chance-1)
            # 원상복귀
            num_list[i], num_list[j] = num_list[j], num_list[i]


for tc in range(1, T+1):
    answer = 0
    num, chance = map(int, input().split())
    num_list = list(str(num))
    visited = {}
    ans_list = set()
    dfs(chance)

    print(f'#{tc} {answer}')