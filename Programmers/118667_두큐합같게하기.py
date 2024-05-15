from collections import deque


def solution(queue1, queue2):
    answer = 0

    q1, q2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)

    # 홀수인 경우
    if (sum1 + sum2) % 2 != 0:
        return -1

    while True:
        # 종료 조건(안하면 시간 초과남)
        if answer == 4 * len(queue1):
            return -1
        # sum1이 크면 q1에서 pop, q2로 insert
        if sum1 > sum2:
            value = q1.popleft()
            q2.append(value)
            sum1 -= value
            sum2 += value
        # sum2가 크면 q2에서 pop, q1로 insert
        elif sum1 < sum2:
            value = q2.popleft()
            q1.append(value)
            sum1 += value
            sum2 -= value
        else:
            return answer
        answer += 1