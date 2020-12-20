import sys

n, m = map(int, input().split())
arr_n = list(sys.stdin.readline().rstrip() for _ in range(n))
arr_m = list(sys.stdin.readline().rstrip() for _ in range(m))

# 교집합
common = set(arr_n) & set(arr_m)
result = list(sorted(common))
print(len(result))
for i in result:
    print(i)