import sys

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
arr.sort()

for i in arr:
    print(i)