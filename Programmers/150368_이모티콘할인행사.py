data = [10, 20, 30, 40]
discount = []

## 이모티콘 할인율 구하기
# 모든 할인 조합 dfs로 구해서 discount 배열에 저장
def dfs(temp, depth):
    if depth == len(temp):
        discount.append(temp[:])
        return

    for d in data:
        temp[depth] += d
        dfs(temp, depth + 1)
        temp[depth] -= d


def solution(users, emoticons):
    answer = [0, 0]

    dfs([0] * len(emoticons), 0)

    # 모든 할인 리스트에 대해 탐색
    for d in range(len(discount)):
        join, price = 0, [0] * len(users) # integer
        for e in range(len(emoticons)):
            for u in range(len(users)):
                # 할인율을 만족하면 구매
                if users[u][0] <= discount[d][e]:
                    price[u] += emoticons[e] * (100 - discount[d][e]) / 100

        # 사용자가 설정한 가격보다 크면 이모티콘 플러스 가입
        for u in range(len(users)):
            if price[u] >= users[u][1]:
                join += 1
                price[u] = 0

        # 최대 가입자, 구매 금액 갱신
        if join >= answer[0]:
            if join == answer[0]:
                answer[1] = max(answer[1], sum(price))
            else:
                answer[1] = sum(price)
            answer[0] = join

    return answer