# 2023 하반기 1번

# 거리 체크
def calculate_distance(r1, c1, r2, c2):
    return (r1 - r2) ** 2 + (c1 - c2) ** 2

# 루돌프가 움직일 좌표 구하기
def get_rudolf_move(Rr, Rc):
    ## 0. 방향 인덱스
    dRr = [-1, -1, -1, 0, 0, 1, 1, 1 ]
    dRc = [-1, 0, 1, -1, 1, -1, 0, 1]

    ## 1. 가장 가까운 산타 체크
    dist = {}
    for santa in santa_dict:
        # 각각 산타와 루돌프의 거리 계산 후 dist 배열에 넣기
        if santa_dict[santa][-1] == False:
            dist[santa] = calculate_distance(Rr, Rc, santa_dict[santa][0], santa_dict[santa][1])
    # 루돌프 이동할 곳 없으면
    if dist == {}:
        return None
    # 최솟값 찾기
    min_dist = min(dist.values())
    # 가장 가까운 산타 여러명이면
    near_santa = 0
    near_santa_count = 0
    for i in dist.values():
        if i == min_dist:
            near_santa_count += 1
    if near_santa_count > 1:
        santa_list = []
        # print(len(dist))
        for key, value in dist.items():
            if value == min_dist:
                santa_list.append(key)
        # print(santa_list)
        # r(다음 c)이 큰 산타 찾기 : board를 (N,N)부터 거꾸로 읽음
        for i in range(N,0,-1):
            for j in range(N,0,-1):
                if board[i][j] in santa_list:
                    near_santa = board[i][j]
                    break
            if near_santa>0:
                break
    else:
        for key, value in dist.items():
            if value == min_dist:
                near_santa = key
    # 산타와 가장 가까워지는 방향 찾기
    rudolf_move_list = {}
    for i in range(8):
        nRr = Rr + dRr[i]
        nRc = Rc + dRc[i]
        rudolf_move_list[calculate_distance(nRr, nRc, santa_dict[near_santa][0],santa_dict[near_santa][1])] = [nRr, nRc]
    # key(거리)를 기준으로 정렬
    new_rudolf = sorted(rudolf_move_list.items())[0][1]
    return new_rudolf

# 산타 움직일 좌표 구하기
def get_santa_move(Sr, Sc, Rr, Rc):
    # 좌 하 우 상
    dSr = [0, 1, 0, -1]
    dSc = [-1, 0, 1, 0]
    santa_move_list = {}
    # 현재 위치부터 루돌프까지 거리도 넣기
    santa_move_list[calculate_distance(Rr,Rc, Sr, Sc)] = [ Sr, Sc ]
    for i in range(4):
        nSr = Sr + dSr[i]
        nSc = Sc + dSc[i]
        # print(nSr, nSc, calculate_distance(Rr,Rc, nSr, nSc))
        if canMove(nSr, nSc) or (nSr == Sr and nSc == Sc):
            santa_move_list[calculate_distance(Rr,Rc, nSr, nSc)] = [ nSr, nSc ]
    santa_move_list = sorted(santa_move_list.items())
    # print(santa_move_list)
    for key, value in santa_move_list:

        if canMove(value[0], value[1]) or (value[0] == Sr and value[1] == Sc):
            new_santa = value
            # print(new_santa,"여기로 움직일 예정이에요")
            return new_santa
    return None
# 산타 움직일 수 있는 지 체크
def canMove(r, c):
    # 벽 아닌 경우
    if (r > 0 and r <= N and c > 0 and c <= N):
        # 움직이려는 곳에 산타 있으면 => X
        if board[r][c] > 0:
            return False
        else:
            return True
    # 벽인 경우
    else:
        return False

def rudolf_move(Rr, Rc):
    # 루돌프가 이동할 좌표 찾음
    new_rudolf_place = get_rudolf_move(Rr, Rc)
    if new_rudolf_place == None:
        return
    nRr, nRc = new_rudolf_place[0], new_rudolf_place[1]
    # print("루돌프 좌표",Rr, Rc, nRr, nRc)
    # 충돌 처리하고
    direction = [nRr - Rr, nRc - Rc]  # 이동할 방향 벡터
    conflict(nRr, nRc, direction, 0, C)   # 충돌 먼저 처리
    # 루돌프 이동
    board[Rr][Rc], board[nRr][nRc] = -1, 0 # 보드에 표시하고
    rudolf_dict[0], rudolf_dict[1] = nRr, nRc # 루돌프 정보 업데이트
    return

def santa_move(Sr, Sc, santa):
    # print(santa, "움직입니다", santa_dict)
    # 움직일 산타 위치 찾기
    new_santa_place = get_santa_move(Sr, Sc, rudolf_dict[0], rudolf_dict[1])
    if new_santa_place == None:
        # print("못움직이므로 종료")
        return
    nSr, nSc = new_santa_place[0], new_santa_place[1]
    # print(nSr, nSc, board[3][2])
    # 움직일 수 있어도 루돌프랑 가까워질 수 있는 방법 없으면 움직이지 않음
    if (nSr == Sr) and (nSc == Sc):
        # print("가까워질 방법 없어 종료")
        return
    else:
        direction = [nSr - Sr, nSc - Sc]
        conflict(nSr, nSc, direction, santa, D)
        # 산타 옮기기
        # 만약 이동할 곳에 루돌프 있다면, 이동할 산타가 반대로 밀려남 => conflict 안에서 처리하고 이 함수에서는 처리 안함
        if board[nSr][nSc] == 0:
            return
        else:
            board[Sr][Sc], board[nSr][nSc] = -1, santa
            santa_dict[santa][0], santa_dict[santa][1] = nSr, nSc
            return
# 산타와 루돌프가 같이 있다면 충돌!
def conflict(r, c, d, idx, power):

    # 충돌 체크
    if board[r][c] == -1:
        # print("충돌 안남")
        return

    # 루돌프가 달려왔다면
    if idx == 0:
        # 해당 산타 C 만큼 점수 얻어
        santa_dict[board[r][c]][2] += C
        # print(board[r][c], santa_dict[board[r][c]], "충돌일어남")
        # 기절
        santa_stun_list[2].append(board[r][c])
        # print(santa_stun_list)
        # 산타가 이동해온 방향으로 C칸 밀려나
        nSr, nSc = r + d[0] * C, c + d[1] * C
        if (nSr > 0 and nSr <= N and nSc > 0 and nSc <= N):
            # 상호작용 체크하고
            interaction(nSr, nSc, board[nSr][nSc], [d[0], d[1]])
            # 산타 이동
            santa_dict[board[r][c]][0], santa_dict[board[r][c]][1] = nSr, nSc
            board[nSr][nSc] = board[r][c]
            # 루돌프 이동
            board[r][c], board[rudolf_dict[0]][rudolf_dict[1]] = 0, -1
            rudolf_dict[0], rudolf_dict[1]= r, c
            return
        else:
            # 산타 탈락
            santa_dict[board[r][c]][-1], santa_dict[board[r][c]][0], santa_dict[board[r][c]][1] = True, 0, 0
            # print(board[r][c], "산타가 게임판 밖으로 밀려나서 탈락했습니다.")
            board[r][c] = -1
    # 산타가 달려왔다면
    else:
        # print(idx, "산타 -> 루돌프 충돌이요~")
        # 해당 산타 D 만큼 점수 얻어
        santa_dict[idx][2] += D
        # print(santa_dict[idx]) # OK
        # 기절
        santa_stun_list[2].append(idx)
        # print(santa_stun_list) # OK
        # 산타 이동해 온 반대 방향으로 D 만큼 밀려나
        nSr, nSc = r - d[0] * D, c - d[1] * D
        # print(D, "만큼 여기로 밀려납니다ㅠㅠ", nSr, nSc) # OK

        if (nSr > 0 and nSr <= N and nSc > 0 and nSc <= N):
            # 상호작용 체크하고
            # print("이제 상호작용 체크합니다")
            board[santa_dict[idx][0]][santa_dict[idx][1]] = -1
            interaction(nSr, nSc, board[nSr][nSc],[-d[0], -d[1]])
            santa_dict[idx][0], santa_dict[idx][1] = nSr, nSc
            board[nSr][nSc] = idx
            # 산타 이동
            # print("WHHHH",board)
            return
        else:
            # 산타 탈락
            santa_dict[idx][-1] = True
            # print(idx, "산타가 게임판 밖으로 밀려나서 탈락했습니다.")
            board[santa_dict[idx][0]][santa_dict[idx][1]] = -1
            santa_dict[idx][0], santa_dict[idx][1] = 0, 0
# 상호작용
def interaction(r, c, santa, d):
    # print(r, c,"에있는", santa,"상호작용 시작, 방향",d)
    # 연쇄 밀림
    # 충돌 체크(연쇄할 거 없으면 return : 종료 조건)
    if board[r][c] == -1:
        return
    # 연쇄(재귀)
    direction = d
    interaction(r + d[0], c + d[1], board[r + d[0]][c + d[1]], direction)
    santa_dict[santa][0], santa_dict[santa][1] = r + d[0], c + d[1]
    board[r+d[0]][c+d[1]] = santa
    # print(santa, santa_dict[santa],board[r+d[0]][c+d[1]],r+d[0],c+d[1],"연쇄 이동완.")
    # print(board)

def main():
    global santa_dict, board, rudolf_dict, santa_stun_list, N, M, P, C, D, board
    # 게임판 크기(N), 게임 턴 수(M), 산타 수(P), 루돌프 힘(C), 산타 힘(D)
    N, M, P, C, D = map(int, input().split())

    # 게임판(가장자리 벽 세워줌)
    board = [[-1] * (N + 2) for _ in range(N + 2)]

    # 루돌프 초기 위치
    Rr, Rc = map(int, input().split())
    rudolf_dict = [Rr, Rc]
    board[Rr][Rc] = 0

    # 산타 초기 위치 P만큼
    santa_dict = {}
    for _ in range(P):
        idx, Sr, Sc = map(int, input().split())
        santa_dict[idx] = [Sr, Sc, 0, False]  # 위치 r, 위치 c, 점수, isSurvived
        board[Sr][Sc] = idx

    santa_stun_list = {2: [], 1: []}
    santa_dict = dict(sorted(santa_dict.items()))

    for c in range(1,M+1):
        # print(c, "#################################################333")
        ### 0. 한 턴이 돌때마다 기절 산타 상태 바꿔주기
        santa_stun_list[1] = santa_stun_list[2]
        santa_stun_list[2] = []
        #### 1. 루돌프  옮기기
        rudolf_move(rudolf_dict[0], rudolf_dict[1])
        # print("루돌프 움직였어요 ::", rudolf_dict)
        #### 2. 산타 차례로 옮기기
        for santa in santa_dict:
            # print("======================", santa, "=============")
            if santa_dict[santa][-1] == True:
                # print(santa, "탈락산타")
                continue
            if santa not in (santa_stun_list[1]) and santa not in (santa_stun_list[2]):
                # print(santa, "움직임")
                Sr, Sc = santa_dict[santa][0], santa_dict[santa][1]
                santa_move(Sr, Sc, santa)
                # print(santa_dict)
                # print(Sr, Sc, "에서", santa_dict[santa][0], santa_dict[santa][1]," 여기로")

        ### 4. 모두 탈락했다면 종료 / 매턴 이후 탈락하지 않은 산타 1점 부여
        if len(santa_dict) == 0:
            # print("모든 산타가 탈락하여 종료합니다.")
            break
        else:
            for santa in santa_dict:
                if santa_dict[santa][-1] == False:
                    santa_dict[santa][2] += 1

        # print("****한 턴 결과****")
        # print(santa_dict)
        # print(santa_stun_list)
        # for i in range(1,len(board)-1):
        #     for j in range(1,len(board[i])-1):
        #         print(board[i][j], end=' ')
        #     print()
        # print("****************")
    answer = 0
    if len(santa_dict) > 0:
        for santa in santa_dict:
            print(santa_dict[santa][2], end=' ')
    # print("SANTA", santa_dict)
main()