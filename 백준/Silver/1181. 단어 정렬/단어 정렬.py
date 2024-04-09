cases = int(input())
arr = {input() for _ in range(cases)}
words = list(arr)
words.sort()
words.sort(key=lambda x: len(x))

for i in words:
    print(i)
