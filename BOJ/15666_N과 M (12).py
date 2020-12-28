from itertools import combinations_with_replacement as cwr

n, m = map(int, input().split())
nums = list(map(int, input().split()))
result = []
for i in cwr(sorted(nums), m):
    result.append(i)

for j in sorted(set(result)):
    print(*j)