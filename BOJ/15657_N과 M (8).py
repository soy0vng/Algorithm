from itertools import combinations_with_replacement as cwr

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
for i in cwr(nums, m):
    print(*i)