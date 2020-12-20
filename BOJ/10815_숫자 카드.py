import sys


def binary_search(target):
    start = 0
    end = n-1
    while start <= end:
        mid = (start+end) // 2
        if cards[mid] == target:
            return 1
        elif cards[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0


n = int(input())
cards = list(map(int, sys.stdin.readline().split()))
m = int(input())
find_list = list(map(int, sys.stdin.readline().split()))

cards.sort()
for i in find_list:
    print(binary_search(i), end=" ")