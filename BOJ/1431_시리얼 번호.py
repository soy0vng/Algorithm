n = int(input())
guitar_list = []
for _ in range(n):
    cnt = 0
    guitar = input()
    for i in guitar:
        if i.isdigit():
            cnt += int(i)
    guitar_list.append((guitar, cnt))

guitar_list.sort(key=lambda x: (len(x[0]), x[1], x[0]))
for g in guitar_list:
    print(g[0])