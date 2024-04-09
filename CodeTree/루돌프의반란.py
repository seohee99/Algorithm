# 2023 하반기 1번

from collections import deque

# 게임판 크기(N), 게임 턴 수(M), 산타 수(P), 루돌프 힘(C), 산타 힘(D)
N, M, P, C, D = map(int, input().split())

# 게임판(가장자리 벽 세워줌)
board = [ [-1] * (N+2) for _ in range(N+2) ]

# 루돌프 초기 위치
Rr, Rc = map(int, input().split())
rudolf_dict = {0: [Rr, Rc]}
board[Rr][Rc] = 0

santa_dict = {}
# 산타 초기 위치 P만큼
for  _ in range(P):
    idx, Sr, Sc = map(int, input().split())
    santa_dict[idx] = [Sr, Sc, 0] # 위치 r, 위치 c, 점수
    board[Sr][Sc] = idx

# 거리 체크
def calculate_distance(r1, c1, r2, c2):
    return (r1 - r2) ** 2 + (c1 - c2) ** 2

# 루돌프가 움직일 좌표 구하기
def get_rudolf_move(Rr, Rc, santa_dict):

    ## 0. 방향 인덱스
    dRr = [-1, -1, -1, 0, 0, 1, 1, 1 ]
    dRc = [-1, 0, 1, -1, 1, -1, 0, 1]

    ## 1. 가장 가까운 산타 체크
    dist = [5001] * (P+1) # 가장 큰 값으로 초기화
    for santa in santa_dict:
        # 탈락한 산타(점수가 -1)인 산타 무시
        if santa_dict[santa][2] != -1:
            # 각각 산타와 루돌프의 거리 계산 후 dist 배열에 넣기
            dist[santa] = calculate_distance(Rr, Rc, santa_dict[santa][0], santa_dict[santa][1])

    # 최솟값 찾기
    min_dist = min(dist)
    # print(min_dist)
    # 가장 가까운 산타 여러명이면
    near_santa = 0
    if dist.count(min_dist) > 1:
        santa_list = []
        for i in range(len(dist)):
            if dist[i] == min_dist:
                santa_list.append(i)
        # r(다음 c)이 큰 산타 찾기 : board를 (N,N)부터 거꾸로 읽음
        for i in range(N,0,-1):
            for j in range(N,0,-1):
                if board[i][j] in santa_list:
                    near_santa = board[i][j]
                    break
            if near_santa>0:
                break
        # print(near_santa)

    ## 2. 루돌프 이동
    # 산타와 가장 가까워지는 방향으로 이동
    rudolf_move_list = {}
    for i in range(8):
        nRr = Rr + dRr[i]
        nRc = Rc + dRc[i]
        rudolf_move_list[ calculate_distance(nRr, nRc, santa_dict[near_santa][0],santa_dict[near_santa][1])] = [nRr, nRc]
    # key(거리)를 기준으로 정렬
    min_rudolf_move_dist = sorted(rudolf_move_list.items())[0][0]
    new_rudolf =  sorted(rudolf_move_list.items())[0][1]
    return new_rudolf

def get_santa_move(Sr, Sc, Rr, Rc):
    dSr = [-1, 1, 0, 0]
    dSc = [0, 0, -1, 0]
    santa_move_list = {}
    for i in range(4):
        nSr = Sr + dSr[i]
        nSc = Sc + dSc[i]
        santa_move_list[calculate_distance(Rr,Rc, nSr, nSc)] = [ nSr, nSc ]
    new_santa = sorted(santa_move_list.items())[0][1]
    return new_santa

def rufolf_conflict(Rr, Rc, santa_dict):
    return

def santa_conflict(Sr, Sc, santa_dict):
    return

# 이 함수를 분리해야겠군... 루돌프 / 산타로
def conflict(r, c, idx, dr, dc):

    # -1이 아니면 무언가 있다는 것
    old = board[r][c]
    print(old)
    if old != -1:
        # 루돌프가 움직여서 충돌이 난 경우
        if idx == 0:
            print("루돌프가 박았어요")
            # 루돌프 이동
            board[r][c] = idx
            # 산타 점수 C만큼 주기
            santa_dict[old][2] += C
            # 산타 C만큼 밀려남
            nr, nc = r + dr * C, c + dc * C
            if nr > 0 and nr <= N and nc > 0 and nc < N:
                print("이도잉요~")
                board[nr][nc] = old
                # 점수는 그대로, dict의 좌표 이동
                santa_dict[old] = [nr, nc, santa_dict[old][2]]
                # 또 산타 있으면 연쇄적 밀림 -> 상호작용...
                if board[nr][nc] > 0:
                    conflict(nr, nc, old, nr - r, nc - c)
            # 탈락
            else:
                del(santa_dict[old])
                print(old, "R.I.P")
        # 산타가 움직여서 충돌이 난 경우
        else:
            print(idx, "산타가 박았어요")
            # 이동한 산타
            board[r][c] = idx
            # 산타 점수 D만큼 주기
            santa_dict[old][2] += D
            # 산타 D만큼 밀려남
            nr, nc = r + dr * D, c + dc * D
            if nr > 0 and nr <= N and nc > 0 and nc < N:
                print("이동이요~")
                board[nr][nc] = old
                # 점수는 그대로, dict의 좌표 이동
                santa_dict[old] = [nr, nc, santa_dict[old][2]]
                # 또 산타 있으면 연쇄적 밀림
                if board[nr][nc] > 0:
                    conflict(nr, nc, old, nr - r, nc - c)
            # 탈락
            else:
                del(santa_dict[old])
                print(old, "R.I.P")
    else:
        # 종료 조건 : 충돌 안날때 까지
        print("충돌 안났어요")
        return
# 상호작용
def interaction():
    return
# 기절
def faint():
    # 한 턴 돌때마다 이동
    faint_list = {2 : [], 1 : []}
    return

def main():
    print(santa_dict)
    #### 1. 루돌프  옮기기
    Rr, Rc = rudolf_dict[0][0], rudolf_dict[0][1]
    new_rudolf_place = get_rudolf_move(Rr, Rc, santa_dict)
    # 이전 루돌프 좌표 벽으로 만들고
    board[Rr][Rc] = -1
    # 루돌프 옮기기
    # ㅅㅂ 충돌 체크
    conflict(Rr, Rc, 0, new_rudolf_place[0] - Rr, new_rudolf_place[1] - Rc)
    rudolf_dict[0][0], rudolf_dict[0][1] = new_rudolf_place[0], new_rudolf_place[1]
    Rr, Rc = rudolf_dict[0][0], rudolf_dict[0][1]
    # board[Rr][Rc] = 0

    #### 2. 산타 차례로 옮기기
    for santa in santa_dict:
        print(santa, "옮길 위치 구합니다!")
        new_santa_place = get_santa_move(santa_dict[santa][0],santa_dict[santa][1],Rr,Rc)
        print(new_santa_place)

        conflict(santa_dict[santa][0],santa_dict[santa][1], santa, new_santa_place[0] - santa_dict[santa][0], new_santa_place[1] - santa_dict[santa][1])
        board[santa_dict[santa][0]][santa_dict[santa][1]] = -1
    print(santa_dict)

main()