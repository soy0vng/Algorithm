from itertools import combinations

n = int(input())
ability = [list(map(int, input().split())) for _ in range(n)]

# 팀 후보
members = list(range(n))
candidate = []
for team in list(combinations(members, n//2)):
    candidate.append(team)

result = 987654321
for i in range(len(candidate)//2):
    # 스타트
    start = candidate[i]
    ability_start = 0
    for j in range(n//2):
        member = start[j]
        for k in start:
            ability_start += ability[member][k]

    # 링크
    link = candidate[-1-i]
    ability_link = 0
    for j in range(n//2):
        member = link[j]
        for k in link:
            ability_link += ability[member][k]

    result = min(result, abs(ability_start - ability_link))

print(result)