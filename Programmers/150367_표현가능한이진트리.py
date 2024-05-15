import math

# 자식과 부모 확인
# parent : 부모 존재 여부
def child_parent(num,parent):
    if num == '':
        return True
    mid = len(num)//2
    me = num[mid]
    # 내가 1인데 부모가 0이면
    if me == '1' and parent =='0':
        return False
    else:
        # 나의 자식 확인
        return child_parent(num[:mid],me) and child_parent(num[mid+1:],me)

# 2. 표현 가능한가?
def check(num):
    if num == 1:
        return 1
    # 2진수로 바꾸기
    num = bin(num)[2:]
    # 포화 이진 트리로 만들기 -> len(num)을 2**n-1로 만들기
    digit = 2 ** (int(math.log(len(num), 2)) + 1) - 1
    # 0추가
    num = "0" * (digit - len(num)) + num
    
    # 자식 중 1이 있다면 부모 노드는 항상 1이어야 한다.
    if num[len(num)//2] == '1' and child_parent(num,True):
        return 1
    else:
        return 0

# 1.
def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(check(num))
    return answer