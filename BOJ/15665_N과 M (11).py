from itertools import product

n, m = map(int, input().split())
nums = list(map(int, input().split()))
result = []
for i in product(nums, repeat=m):
    result.append(i)

for j in sorted(set(result)):
    print(*j)