import sys

n = int(input())
cards = list(map(int, sys.stdin.readline().split()))
m = int(input())
find_list = list(map(int, sys.stdin.readline().split()))

cards_cnt = {}
for card in cards:
    if card in cards_cnt:
        cards_cnt[card] += 1
    else:
        cards_cnt[card] = 1

for target in find_list:
    if target in cards_cnt:
        print(cards_cnt[target], end=" ")
    else:
        print(0, end=" ")