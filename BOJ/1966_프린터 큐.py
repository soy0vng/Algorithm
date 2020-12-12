for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    importance = list(map(int, input().split()))
    idx = list(range(len(importance)))
    idx[m] = 'target'
    cnt = 0

    while True:
        if importance[0] == max(importance):
            cnt += 1
            if idx[0] == 'target':
                print(cnt)
                break
            else:
                importance.pop(0)
                idx.pop(0)
        else:
            importance.append(importance.pop(0))
            idx.append(idx.pop(0))






