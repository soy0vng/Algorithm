import sys

n = int(input())
numbers = list(map(int, sys.stdin.readline().split()))

for i in sorted(set(numbers)):
    print(i, end=" ")

