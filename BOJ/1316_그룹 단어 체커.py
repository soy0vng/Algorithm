def check():
    global cnt
    arr = []
    for i in word:
        if i in arr and arr[-1] != i:
            break
        else:
            arr.append(i)

    if len(arr) == len(word):
        cnt += 1


n = int(input())
cnt = 0
for i in range(n):
    word = input()
    check()
print(cnt)