# PyPy3
import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start, end = 0, max(trees)
result = 0
while start <= end:
    tree_len = 0
    mid = (start+end) // 2
    for i in trees:
        if i > mid:
            tree_len += i - mid
    if tree_len < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)