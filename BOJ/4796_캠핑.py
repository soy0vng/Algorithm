n = 0
while True:
    # 연속하는 p일 중, l일 동안만 사용 가능
    l, p, v = map(int, input().split())
    if l == 0:
        break
    result = (v // p) * l
    remain = v % p
    if remain > l:
        result += l
    else:
        result += remain
    n += 1
    print(f"Case {n}: {result}")