import sys

input = sys.stdin.readline


def dfs(lotto, nums, visited):
    if len(lotto) == 6:
        for i in range(6):
            print(nums[lotto[i]], end=' ')
        print()
        return

    t_visited = visited[:]
    for i in range(len(t_visited)):
        if not t_visited[i]:
            t_visited[i] = True
            dfs(lotto + [i], nums, t_visited)


while True:
    nums = list(map(int, input().split()))
    if len(nums) == 1 and nums[0] == 0:
        break

    length = nums.pop(0)

    visited = [False] * len(nums)
    dfs([], nums, visited)
    print()
