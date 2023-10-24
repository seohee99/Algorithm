import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))

answer = "mixed"
if arr[0] == 1:
    flag = True
    for idx,i in enumerate(arr):
        if (i != (idx + 1)) : 
            flag = False
            break
    if flag == True:
        answer = "ascending"
else :
    flag = True
    for idx,i in enumerate(arr):
        if (i != (8 - idx)) : 
            flag = False
            break
    if flag == True:
        answer = "descending"
print(answer)
    