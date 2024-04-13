# 포탑부수기

from collections import deque
# 공격자 선정
def min_attack_select():
    # 공격력 가장 낮은 : temp1
    power = 5001 # max power
    temp1, temp2, temp3, temp4 = [], [], [], []
    # 최소 공격력 구하고
    for key, value in top_dict.items():
        if value['power'] == 0:
            continue
        if value['power'] < power:
            power = min(power, value['power'])
    # 최소인 값 temp1에 넣기
    for key, value in top_dict.items():
        if power == value['power']:
            temp1.append(key)
    # 가장 최근 공격 : temp2
    attackAt = -1
    if len(temp1) > 1:
        # print("2, temp1 : ", temp1)
        # 가장 최근 공격 시기 구하고
        for top in temp1:
            if top_dict[top]['attackAt'] > attackAt:
                attackAt = max(attackAt, top_dict[top]['attackAt'])
        # temp2 배열에 넣기
        for top in temp1:
            if top_dict[top]['attackAt'] == attackAt:
                temp2.append(top)
    else:
        return temp1.pop()
    # 행 + 열 합 max : temp3
    nm_sum = -1
    if len(temp2) > 1:
        # print("3, TEMP2 ", temp2)
        for top in temp2:
            if sum(top) > nm_sum:
                nm_sum = sum(top)
        for top in temp2:
            if sum(top) == nm_sum:
                temp3.append(top)
    else:
        return temp2.pop()

    # 열 값 max : temp4
    max_m = -1
    if len(temp3) > 1:
        # print("4, temp3 : ", temp3)
        for top in temp3:
            if top[1] > max_m:
                max_m = top[1]
        for top in temp3:
            if top[1] == max_m:
                return top
    else:
        return temp3.pop()

def max_attack_select(from_attacker):
    # 공격력 가장 높은 : temp1
    power = -1 # min power
    temp1, temp2, temp3 = [], [], []
    # 최대 공격력 구하고
    for key, value in top_dict.items():
        # 자신 제외
        if key == from_attacker:
            continue
        if value['power'] > power:
            power = max(power, value['power'])
    # 최대인 값 temp1에 넣기
    for key, value in top_dict.items():
        if power == value['power']:
            temp1.append(key)
    # 가장 오래된 공격 : temp2
    attackAt = 1001
    if len(temp1) > 1:
        # print("2, temp1 : ", temp1)
        # 가장 오래된 공격 시기 구하고
        for top in temp1:
            if top_dict[top]['attackAt'] < attackAt:
                attackAt = min(attackAt, top_dict[top]['attackAt'])
        # temp2 배열에 넣기
        for top in temp1:
            if top_dict[top]['attackAt'] == attackAt:
                temp2.append(top)
    else:
        return temp1.pop()
    # 행 + 열 합 min : temp3
    nm_sum = N+M
    if len(temp2) > 1:
        # print("3, TEMP2 ", temp2)
        for top in temp2:
            if sum(top) < nm_sum:
                nm_sum = sum(top)
        for top in temp2:
            if sum(top) == nm_sum:
                temp3.append(top)
    else:
        return temp2.pop()

    # 열 값 min : temp4
    min_m = 11
    if len(temp3) > 1:
        # print("4, temp3 : ", temp3)
        for top in temp3:
            if top[1] < min_m:
                min_m = top[1]
        for top in temp3:
            if top[1] == min_m:
                return top
    else:
        return temp3.pop()

def attack(from_attacker, to_attacker, k):
    # print(from_attacker,top_dict[from_attacker]['power'],"에서", to_attacker, top_dict[to_attacker]['power'],"로 공격")
    road = laser_attack(from_attacker, to_attacker)
    top_dict[from_attacker]['attack'] = True
    top_dict[to_attacker]['attack'] = True

    # print(from_attacker, top_dict[from_attacker], to_attacker ,top_dict[to_attacker])
    if road == None:
        # print(k,"턴 레이저 공격 실패, 포탄 해야됨")
        # for i in range(1, N+1):
        #     print(board[i])
        road = bomb_attack(from_attacker, to_attacker)
        road.append(to_attacker) # 하 스발 여기다
        for r in road:
            top_dict[r]['attack'] = True
            # print(top_dict[r])
            if r == from_attacker:
                continue
            elif r == to_attacker:
                board[to_attacker[0]][to_attacker[1]] -= top_dict[from_attacker]['power']
                top_dict[to_attacker]['power'] -= top_dict[from_attacker]['power']
            else:
                board[r[0]][r[1]] -= (top_dict[from_attacker]['power']) // 2
                top_dict[r]['power'] -= (top_dict[from_attacker]['power']) // 2
    else:
        # print("레이저")
        # print(road)
        for r in road:
            if r == from_attacker:
                continue
            elif r == to_attacker:
                top_dict[r]['attack'] = True
                board[to_attacker[0]][to_attacker[1]] -= top_dict[from_attacker]['power']
                top_dict[to_attacker]['power'] -= top_dict[from_attacker]['power']
            else:
                top_dict[r]['attack'] = True
                board[r[0]][r[1]] -= (top_dict[from_attacker]['power']) // 2
                top_dict[r]['power'] -= (top_dict[from_attacker]['power']) // 2
    # print(top_dict)
    return

def laser_attack(from_attacker, to_attacker):
    # 우 하 좌 상
    dn = [0, 1, 0, -1]
    dm = [1, 0, -1, 0]
    visited = [[False] * (M+2) for _ in range(N+2)]

    queue = deque([(from_attacker, [from_attacker])])
    visited[from_attacker[0]][from_attacker[1]] = True

    while(queue):
        (current_n, current_m), path = queue.popleft()
        if current_n == to_attacker[0] and current_m == to_attacker[1]:
            # print(path)
            return path

        for i in range(4):
            next_n, next_m = current_n + dn[i], current_m + dm[i]
            if ( 0 < next_n <= N) and (0 < next_m <= M):
                # 부서진 포탑은 pass
                if board[next_n][next_m] == 0:
                    continue
                # 일반적으로 방문할 수 있는 경우
                if visited[next_n][next_m] == False:
                    queue.append(( (next_n,next_m), path + [(next_n,next_m)] ))
                    visited[next_n][next_m] = True

            # 가장자리라면 반대편으로 !
            else:
                if next_n == N + 1:
                    next_n = 1
                elif next_n == 0:
                    next_n = N
                if next_m == M + 1:
                    next_m = 1
                elif next_m == 0:
                    next_m = M
                if board[next_n][next_m] == 0:
                    continue

                # 다시 일반적으로 방문할 수 있는 경우
                if visited[next_n][next_m] == False:
                    queue.append(( (next_n,next_m), path + [(next_n,next_m)] ))
                    visited[next_n][next_m] = True
    return None
def bomb_attack(from_attacker, to_attacker):
    direction = [ (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1) ]
    path = []
    for dn, dm in direction:
        next_n, next_m = to_attacker[0] + dn, to_attacker[1] + dm
        if (0 < next_n <= N) and (0 < next_m <= M):
            # 부서진 포탑은 pass
            if board[next_n][next_m] == 0:
                continue
            path.append((next_n, next_m))
            # 가장자리라면 반대편으로 !
        else:
            if next_n == N + 1:
                next_n = 1
            elif next_n == 0:
                next_n = N
            if next_m == M + 1:
                next_m = 1
            elif next_m == 0:
                next_m = M
            if board[next_n][next_m] == 0:
                continue
            path.append((next_n, next_m))


    return path

def main():
    global N, M, K, board, top_dict

    N, M, K = map(int, input().split())

    board = [[0] * (M + 2) for _ in range(N + 2)]

    for i in range(1, N + 1):
        temp = list(map(int, input().split()))
        for j in range(1, M + 1):
            board[i][j] = temp[j-1]

    top_dict = {}
    for i in range(1, N+1):
        for j in range(1, M+1):
            top_dict[(i,j)] = {'power':board[i][j], 'attackAt':0, 'attack' : False}
    for k in range(1,K+1):
        # print(board)
        # 부서지지 않은 포탑 1개 되면 종료
        count_top = 0
        for top in top_dict.values():
            if top['power'] == 0:
                count_top += 1
        if count_top >= N*M -1:
            # print("부서지지 않은 포탑 1개 이하 되어 종료")
            break

        # 공격자 선정
        from_attacker = min_attack_select()
        # 공격 대상 선정
        to_attacker = max_attack_select(from_attacker)
        # 공격자 강화
        top_dict[from_attacker]['power'] += N + M
        board[from_attacker[0]][from_attacker[1]] += N + M
        top_dict[from_attacker]['attackAt'] = k
        # print("attacker 강화 완.",top_dict[from_attacker])
        # 공격자 공격
        attack(from_attacker, to_attacker, k)
        # 공격력 0되면 부서짐
        for i in range(1, N+1):
            for j in range(1,M+1):
                if top_dict[(i,j)]['attack'] == True and top_dict[(i,j)]['power'] < 0:
                    # print(i, j, "부서짐")
                    top_dict[(i, j)]['power'] = 0
                    board[i][j] = 0
                    # print(board)
        # 포탑 정비
        for i in range(1, N+1):
            for j in range(1,M+1):
                if top_dict[(i,j)]['attack'] != True and top_dict[(i,j)]['power'] != 0:
                    top_dict[(i, j)]['power'] += 1
                    board[i][j] += 1

                top_dict[(i,j)]['attack'] = False
                    # print(i,j)
        # print(k,"턴 종료")
        # for i in range (1, N+1):
        #     for j in range(1, M+1):
        #         print(board[i][j], end=' ')
        #     print()
        # # print(board)
        # print(top_dict)
        # print("===========")
    power = 0  # min power
    for key, value in top_dict.items():
        if value['power'] > power:
            power = max(power, value['power'])
    print(power)
    return

main()