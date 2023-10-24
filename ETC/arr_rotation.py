# 목적지와 원래 배열의 좌표를 비교
def rotate(arr):
    result_arr = [[0] * N for _ in range(N)] # 회전한 값 저장할 배열 초기화

    for i in range(N):
        for j in range(N):
            result_arr[i][j] = arr[N-1-j][i] # 90도 회전할때 마다 x 좌표는 n - 1 -y좌표 ,y좌표는 x좌표로 바뀐다는 규칙성

    return result_arr
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr1 = rotate(arr)
    arr2 = rotate(arr1)
    arr3 = rotate(arr2)

    for a,b,c in zip(arr1, arr2, arr3):
        print(f'{"".join(map(str,a))} {"".join(map(str,b))} {"".join(map(str,c))}')
