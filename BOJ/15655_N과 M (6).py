from itertools import combinations

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
for i in combinations(nums, m):
    print(*i)