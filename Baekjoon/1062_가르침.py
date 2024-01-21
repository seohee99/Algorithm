import sys
input = sys.stdin.readline

def dfs(start, cnt):
    global ans

    if cnt == k - 5:    # 5개 글자(a, c, i, n, t)는 이미 배웠음
        tmp = 0
        for word in words:
            is_contain = True # 배운 글자로 해당 단어를 읽을 수 있는지 확인
            for c in word:
                if not check[ord(c) - ord('a')]:    # 해당 단어에 배우지 않은 글자가 있는 경우
                    is_contain = False
                    break

            # 해당 단어를 읽을 수 있는 경우
            if is_contain:
                tmp += 1

        ans = max(ans, tmp)
        return
    
    for i in range(start, 26):
        if not check[i]:
            check[i] = True
            dfs(i, cnt + 1)
            check[i] = False

n, k = map(int, input().split())

# set을 활용하여 중복을 제거함으로써 해당 단어를 읽는데 필요한 최소한의 글자를 구함
words = [set(input().rstrip()) for _ in range(n)]
check = [False] * 26
ans = 0

# 가르칠 글자의 수가 5(a, n, t, i, c)보다 작은 경우
if k < 5:
    print(0)    # 읽을 수 있는 단어가 없음
    exit(0)
# 가르칠 글자의 수가 26(a, b, c, ..., z)인 경우
elif k == 26:
    print(n)    # 모든 단어를 읽을 수 있음
    exit(0)

# a, c, i, n, t 는 무조건 배워야 함
for c in ('a', 'c', 'i', 'n', 't'):
    check[ord(c) - ord('a')] = True

dfs(0, 0)
print(ans)