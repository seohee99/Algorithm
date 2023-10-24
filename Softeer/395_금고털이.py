import sys
 
input = sys.stdin.readline

W, N = map(int, input().split())

metal = []
for i in range(N):
    m, p = map(int, input().split())
    metal.append([m,p])

# 무게당 가격(p) 기준으로 정렬
metal.sort(key=lambda x: x[1], reverse=True)

# 완전 탐색으로 가격 구하기
answer = 0
for weight, price in metal:
    if W <= weight : 
        answer += W * price
        break
    else:
        answer += weight * price
        W -= weight
print(answer)