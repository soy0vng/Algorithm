from itertools import combinations

n, m = map(int, input().split())
nums = list(map(int, input().split()))
result = []
for i in combinations(sorted(nums), m):
    result.append(i)

for j in sorted(set(result)):
    print(*j)