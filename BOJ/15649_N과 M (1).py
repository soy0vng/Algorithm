from itertools import permutations

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]
for num in list(permutations(nums, m)):
    print(*num)