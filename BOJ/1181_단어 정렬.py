n = int(input())
words = []
for _ in range(n):
    word = input()
    words.append((word, len(word)))

words = list(set(words))
words.sort(key=lambda x: (x[1], x[0]))

for i in words:
    print(i[0])
