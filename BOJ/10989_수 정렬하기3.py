import sys

n = int(input())
count = [0 for _ in range(100001)]
for i in range(n):
    count[int(sys.stdin.readline())] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i)