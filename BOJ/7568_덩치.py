def check(weight, height):
    global cnt
    w, h = weight, height
    for i in range(n):
        if w < info[i][0] and h < info[i][1]:
            cnt += 1
    print(cnt, end=" ")


n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    cnt = 1
    check(info[i][0], info[i][1])