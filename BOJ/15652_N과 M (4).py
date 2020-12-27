from itertools import combinations_with_replacement as cwr

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]
for num in list(cwr(nums, m)):
    print(*num)